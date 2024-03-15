import re
from parser_generic import MedicalDocParser

class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        # Call the constructor of the parent class MedicalDocParser
        MedicalDocParser.__init__(self, text)

    def parse(self):
        # Parse the document text and return a dictionary of parsed patient details
        return {
            'patient_name': self.get_patient_name(),
            'phone_number': self.get_patient_phone_number(),
            'medical_problems': self.get_medical_problems(),
            'hepatitis_b_vaccination': self.get_hepatitis_b_vaccination()
        }

    def get_patient_name(self):
        # Extract patient name from the document text
        pattern = 'Patient Information(.*?)\(\d{3}\)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        name = ''
        if matches:
            name = self.remove_noise_from_name(matches[0])
        return name

    def get_patient_phone_number(self):
        # Extract patient phone number from the document text
        pattern = 'Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0][-1]

    def remove_noise_from_name(self, name):
        # Remove noise (e.g., birth date) from patient name
        name = name.replace('Birth Date', '').strip()
        date_pattern = '((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
        date_matches = re.findall(date_pattern, name)
        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date, '').strip()
        return name

    def get_hepatitis_b_vaccination(self):
        # Check if patient has had Hepatitis B vaccination
        pattern = 'Have you had the Hepatitis B vaccination\?.*(Yes|No)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0].strip()

    def get_medical_problems(self):
         # Extract patient's medical problems from the document text
        pattern = 'List any Medical Problems .*?:(.*)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0].strip()

if __name__ == '__main__':
    # Example document text
    document_text = '''
    Patient Medical Record . : :

    Patient Information


    Birth Date
    Kathy Crawford May 6 1972
    (737) 988-0851 Weight:
    9264 Ash Dr 95
    New York City, 10005 a
    United States Height:
    190
    In Case of Emergency
    ee oe
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    Home phone United States
    (990) 375-4621
    Work phone
    Genera! Medical History
    I i
    Chicken Pox (Varicella): Measies:
    IMMUNE IMMUNE

    Have you had the Hepatitis B vaccination?

    No

    List any Medical Problems (asthma, seizures, headaches):

    Migraine'''
    # Create an instance of PatientDetailsParser and parse the document text
    pp = PatientDetailsParser(document_text)
    # Print the parsed patient details
    print(pp.parse())


#line 1 - Import Regular expressions module, which are patterns used to match character combinations in strings.
#line 2 - This line imports the MedicalDocParser class from the parser_generic module. 
#         The leading dot (.) indicates a relative import from the same package.
#line 4 - This line defines a new class named PatientDetailsParser, which inherits from the MedicalDocParser class. 
#         This means that PatientDetailsParser will have all the methods and properties of MedicalDocParser, 
#         in addition to any new methods or properties defined within PatientDetailsParser.
#line 5 - This line defines the constructor method __init__ for the PatientDetailsParser class, which takes one argument text. 
#         The constructor initializes an instance of PatientDetailsParser with the provided text.
#line 7 - This line calls the constructor of the parent class MedicalDocParser using MedicalDocParser.__init__(self, text). 
#         It passes the text argument to the constructor of the parent class, initializing the PatientDetailsParser instance with the provided text.
#line 9 - This method is responsible for parsing the document text and returning a dictionary of parsed patient details.
#line 11 - This block of code returns a dictionary containing parsed patient details extracted using different methods defined within the PatientDetailsParser class.
#line 18 - This method is responsible for extracting the patient's name from the document text.
#line 20 - This line defines a regular expression pattern to extract the patient's name from the document text. 
#line 21 - This line uses the re.findall() function to find all matches of the pattern in the document text (self.text). 
#          The flags=re.DOTALL flag is used to make the dot (.) in the regular expression match any character, including newline characters.
#line 23 - If matches are found for the pattern, this block of code extracts the first match and passes it to the remove_noise_from_name method 
#          to remove any noise, such as birth date, from the extracted name.
#line 27 - This method is responsible for extracting the patient's phone number from the document text.
#line 29 - It captures the text between "Patient Information" and the phone number.
#line 30 - This line uses the re.findall() function to find all matches of the pattern in the document text (self.text). 
#          The flags=re.DOTALL flag is used to make the dot (.) in the regular expression match any character, including newline characters.
#line 32 - If matches are found for the pattern, this block of code returns the last element of the first match, which represents the patient's phone number.
#line 34 - This method is responsible for removing noise, such as birth date, from the extracted patient name.
#line 36 - This line removes the text "Birth Date" from the extracted name and strips any leading or trailing whitespace.
#line 37 - This line defines a regular expression pattern to match dates in various formats (e.g., "Jan 1", "February 10", etc.).
#line 38 - This line uses the re.findall() function to find all matches of the date pattern in the extracted name.
#line 39 - If date matches are found, this block of code extracts the date from the name and removes it.
#Similar approaches continue for the remaining methods.
#line 58 - This block at the end of the script is used to demonstrate the usage of the PatientDetailsParser class by parsing an example document text 
#          and printing the parsed patient details.
 

#####  The leading dot (.) in line 2 indicates a relative import from the same package.
#       i.e., -      from .parser_generic import MedicalDocParser
#####  It must be added while running the test_prescription_parser.py
   
   