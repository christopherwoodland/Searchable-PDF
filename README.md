# Searchable PDF

This project demonstrates how to use Azure Document Intelligence to analyze and convert a PDF document into a searchable PDF using Python.

## Prerequisites

* Python 3.x
* An Azure subscription with Document Intelligence service enabled
* Required Python packages listed in [requirements.txt](vscode-file://vscode-app/c:/Users/cwoodland/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)

## Installation

1. Clone the repository:

   **git **clone** <**repository-ur**l>**

   **cd <**repository-director**y>**
2. Install the required packages:

   **pip **install** **-r** **requirements.txt

## Configuration

1. Replace the placeholders in [searchable-pdf.py](vscode-file://vscode-app/c:/Users/cwoodland/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) with your actual Azure Document Intelligence service URL and subscription key:

   **url = **"**https://{YOUR_DOC-INTEL-URL**}/documentintelligence/documentModels/prebuilt-rea**d:analyze"**

   **headers = **{

   **    **"Ocp-Apim-Subscription-Key"**: **"YOUR_DOC-INTEL-KEY"

   **}**

## Usage

1. Place the PDF file you want to convert in the project directory and update the [pdf_path](vscode-file://vscode-app/c:/Users/cwoodland/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) variable in [searchable-pdf.py](vscode-file://vscode-app/c:/Users/cwoodland/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) with the path to your PDF file:

   **pdf_path = **r**"scansmp3.pdf"**  **# Replace with the path to your PDF file**
2. Run the script:

   **python **searchable-pdf.py
3. The script will encode the PDF file in base64, call the Azure Document Intelligence API to analyze the document, and download the resulting searchable PDF.

## Functions

* [encode_pdf_base64(pdf_path)](vscode-file://vscode-app/c:/Users/cwoodland/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html): Encodes the PDF file in base64.
* [call_api(encoded_pdf)](vscode-file://vscode-app/c:/Users/cwoodland/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html): Calls the Azure Document Intelligence API to analyze the document.
* [poll_status(request_id, pdf_path)](vscode-file://vscode-app/c:/Users/cwoodland/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html): Polls the status of the document analysis.
* [get_file(request_id, pdf_path)](vscode-file://vscode-app/c:/Users/cwoodland/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html): Downloads the resulting searchable PDF.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
