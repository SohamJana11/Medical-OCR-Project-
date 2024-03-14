from pdf2image import convert_from_path
import pytesseract
import util

from parser_prescription import PrescriptionParser
from parser_patient_details import PatientDetailsParser

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

def extract(file_path, file_format):
    # step 1: extracting text from pdf file
    pages = convert_from_path(file_path)
    document_text = ''

    if len(pages)>0:
        # Process the first page
        page = pages[0] 
        processed_image = util.preprocess_image(page) # Preprocess the image
        text = pytesseract.image_to_string(processed_image, lang='eng') # Perform OCR on the processed image
        document_text = '\n' + text # Add the extracted text to the document_text variable

    # step 2: extract fields from text
    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()
    elif file_format == 'patient_details':
        extracted_data = PatientDetailsParser(document_text).parse()
    else:
        # Raise an exception for invalid document format
        raise Exception(f"Invalid document format: {file_format}")

    return extracted_data

if __name__ == '__main__':
    data = extract('/Users/sohamjana/Downloads/source_code/4_project_medical_data_extraction/backend/resources/patient_details/pd_2.pdf', 'patient_details')
    print(data)



#line 1 - This function is used to convert a PDF file into a list of PIL (Python Imaging Library) Image objects.
#line 2 - This imports the pytesseract library, which is used for Optical Character Recognition (OCR) in Python. 
#         It allows us to extract text from images.
#line 3 - This imports a module named util, which contains utility functions used within this script.
#line 5 - This line imports the PrescriptionParser class from a module named parser_prescription. 
#         This class is responsible for parsing prescription documents.
#line 6 - This line imports the PatientDetailsParser class from a module named parser_patient_details.
#         This class handles parsing of patient details documents.
#line 8 - This line sets the path for the Tesseract executable. 
#         Tesseract is the OCR engine used by pytesseract to perform text recognition. 
#         This line specifies the path to the Tesseract executable.
#line 10 - This line defines a function named extract that takes two parameters: 
#          file_path (the path to the PDF file) and file_format (a string indicating the type of document to extract).
#line 12 - This line converts the PDF file specified by file_path into a list of PIL Image objects using the convert_from_path function imported earlier.
#line 13 - This line initializes an empty string named document_text which will be used to store the extracted text from the PDF.
#line 15 - This line checks if there are pages extracted from the PDF. If there are pages present, it proceeds to extract text.
#line 17 - This line selects the first page from the list of extracted pages.
#line 18 - This line preprocesses the image of the page using a function called preprocess_image from the util module. 
#          Preprocessing typically involves enhancing the image to improve OCR accuracy.
#line 19 - This line uses the image_to_string function from pytesseract to perform OCR on the processed image. 
#          It extracts text from the image using the English language ('eng').
#line 20 - This line appends the extracted text from the page to the document_text variable, 
#          adding a newline character before the extracted text.
#line 23 - The following lines check the file_format parameter to determine which parser to use 
#          (PrescriptionParser or PatientDetailsParser) to extract data from the text.
#line 29 -  If the file_format parameter is neither 'prescription' nor 'patient_details', 
#           this line raises an exception indicating an invalid document format.
#line 33 - This line checks if the script is being run directly as the main program.
#line 34 - This line calls the extract function with the path to a PDF file and the format 'patient_details'. 
#          It extracts data from the PDF and assigns it to the variable data.
#line 35 - This line prints the extracted data to the console.

