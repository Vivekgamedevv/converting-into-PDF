# used for conversion of HTML file into pdf file
from weasyprint import HTML
# used for conversion of DOCX file into pdf file
import subprocess
import os

def convert_docx_to_pdf():
    docxfile = input("Enter the DOCX file: ")
    try:
        if not os.path.isfile(docxfile):
            raise FileNotFoundError(f"The file {docxfile} does not exist.")
        
        # Use unoconv to convert DOCX to PDF
        subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", docxfile], check=True)        
        output_pdf = docxfile.replace(".docx", ".pdf")
        print(f"PDF successfully created: {output_pdf}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during conversion: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




def convert_html_to_pdf():
    htmlfile = input("Enter the HTML file: ")
    try:
        if not os.path.isfile(htmlfile):
            raise FileNotFoundError(f"The file {htmlfile} does not exist.")
        HTML(htmlfile).write_pdf('output.pdf')
        print("PDF successfully created: output.pdf")
    except FileNotFoundError as e:
        print(f"Error: {e}")


print("1.HTML code to pdf convertor")
print("2.DOCX file to pdf convertor")
choice = input("Select the options:")

if choice == "1":
    convert_html_to_pdf()
elif choice == "2":
     convert_docx_to_pdf()
else:
    print("Entered the wrong choice")
    print("TRY AGAIN!!!")

