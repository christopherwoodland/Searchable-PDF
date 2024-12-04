#https://learn.microsoft.com/en-us/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v4.0%20(2024-07-31-preview)&tabs=HTTP
#https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/concept/add-on-capabilities?view=doc-intel-4.0.0&tabs=sample-code#searchable-pdf
#https://learn.microsoft.com/en-us/rest/api/aiservices/document-models/get-analyze-result-pdf?view=rest-aiservices-v4.0%20(2024-07-31-preview)&tabs=HTTP

import base64
import requests
import time
import os

def encode_pdf_base64(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read()).decode('utf-8')
    return encoded_string

def call_api(encoded_pdf):
    url = "https://{YOUR_DOC-INTEL-URL}/documentintelligence/documentModels/prebuilt-read:analyze"
    params = {
        "_overload": "analyzeDocument",
        "output": "pdf",
        "api-version": "2024-07-31-preview"
    }
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": "YOUR_DOC-INTEL-KEY"  # Replace with your actual subscription key
    }
    body = {
        "base64Source": encoded_pdf
    }
    response = requests.post(url, headers=headers, params=params, json=body)
    if response.status_code == 202:
        request_id = response.headers.get('apim-request-id')
        return poll_status(request_id, pdf_path)
    return response.json()

def poll_status(request_id, pdf_path):
    status_url = f"https://{YOUR_DOC-INTEL-URL}/documentintelligence/documentModels/prebuilt-read/analyzeResults/{request_id}?api-version=2024-07-31-preview"
    headers = {
        "Ocp-Apim-Subscription-Key": "YOUR_DOC-INTEL-KEY"  # Replace with your actual subscription key
    }
    while True:
        response = requests.get(status_url, headers=headers)
        result = response.json()
        if result.get("status") == "succeeded":
            return get_file(request_id, pdf_path)
        time.sleep(10)

def get_file(request_id, pdf_path):
    file_url = f"https://{YOUR_DOC-INTEL-URL}/documentintelligence/documentModels/prebuilt-read/analyzeResults/{request_id}/pdf?api-version=2024-07-31-preview"
    headers = {
        "Ocp-Apim-Subscription-Key": "YOUR_DOC-INTEL-KEY"  # Replace with your actual subscription key
    }
    response = requests.get(file_url, headers=headers)
    if response.status_code == 200:
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        output_file = f"{base_name}_op.pdf"
        with open(output_file, "wb") as file:
            file.write(response.content)
        return f"File downloaded successfully as {output_file}"
    return response.json()

if __name__ == "__main__":
    pdf_path = r"C:\temp\Redacted_Signature.pdf"  # Replace with the path to your PDF file
    encoded_pdf = encode_pdf_base64(pdf_path) # Encode the PDF with BASE64
    result = call_api(encoded_pdf)
    print(result)