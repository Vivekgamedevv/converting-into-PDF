File Conversion Tool

This is a simple Python script that provides functionality for converting HTML files and DOCX files to PDF format. The script uses WeasyPrint for HTML to PDF conversion and LibreOffice in headless mode for DOCX to PDF conversion.
Features

    HTML to PDF Conversion
    Convert an HTML file to a PDF using WeasyPrint.

    DOCX to PDF Conversion
    Convert a DOCX file to a PDF using LibreOffice in headless mode.

Requirements

The script requires the following Python libraries and tools:

    WeasyPrint: A Python library for converting HTML files to PDF.

    LibreOffice: A free and open-source office suite that provides conversion tools for various document formats, including DOCX to PDF.

Python Libraries

    WeasyPrint: Can be installed via pip.

    subprocess: Part of Python’s standard library, so no additional installation is required.

    os: Part of Python’s standard library, no installation required.

System Dependencies

    LibreOffice: Must be installed on the system, as it is used to convert DOCX files to PDF.

Installation
1. Install Required Libraries

Use the following command to install WeasyPrint:

pip install weasyprint

2. Install LibreOffice

You must have LibreOffice installed on your system to convert DOCX files to PDF. On Ubuntu, you can install it using the following command:

sudo apt update
sudo apt install libreoffice

You can verify that LibreOffice is correctly installed by running:

libreoffice --version

Usage

After setting up the environment, you can use the script to convert DOCX and HTML files to PDF.
1. Running the Script

Run the script using Python:

python file_converter.py

You will be presented with two options:

    1: Convert an HTML file to PDF.

    2: Convert a DOCX file to PDF.

2. Conversion Process

    For HTML to PDF:

        When prompted, enter the path to the HTML file you want to convert.

        The script will generate the PDF and save it as output.pdf.

    For DOCX to PDF:

        When prompted, enter the path to the DOCX file you want to convert.

        The script will use LibreOffice in headless mode to convert the DOCX file into a PDF with the same name as the DOCX file but with a .pdf extension.

Example

Here’s how it works:

    Run the script:

python file_converter.py

Choose an option (1 or 2):

1.HTML code to pdf convertor
2.DOCX file to pdf convertor
Select the options: 2

Provide the path to the DOCX file (e.g., sample.docx):

Enter the DOCX file: /path/to/your/sample.docx

If successful, you will see:

    PDF successfully created: /path/to/your/sample.pdf

Error Handling

    If you provide an incorrect file path, the script will catch the FileNotFoundError and display an appropriate message.

    If LibreOffice or the conversion command fails, a subprocess.CalledProcessError will be raised and handled.

    Other unexpected errors are also caught by a generic exception handler.

Troubleshooting

    LibreOffice Not Found:
    If you encounter an error that LibreOffice is not found, ensure it is installed and properly configured in your system’s PATH.

    WeasyPrint Issues:
    If you encounter errors related to WeasyPrint, ensure that the necessary system dependencies for WeasyPrint are installed:

        On Ubuntu, you may need to install the following:

        sudo apt install libpango1.0-dev libcairo2-dev

    File Not Found:
    Make sure you provide the correct file path when prompted for the input file.

License

This script is open-source and free to use, modify, and distribute. Please feel free to contribute to improving it!
