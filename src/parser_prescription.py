import re
from parser_generic import MedicalDocParser

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        # Call the constructor of the parent class MedicalDocParser
        MedicalDocParser.__init__(self, text) 

    def parse(self):
        # Parse the document text and return a dictionary of parsed fields
        return {
            'patient_name': self.get_field('patient_name'),
            'patient_address': self.get_field('patient_address'),
            'medicines': self.get_field('medicines'),
            'directions': self.get_field('directions'),
            'refills': self.get_field('refills')
        }

    def get_field(self, field_name):
        # Define patterns for extracting different fields from the document text
        pattern_dict = {
            'patient_name': {'pattern': 'Name:(.*)Date', 'flags': 0},
            'patient_address': {'pattern': 'Address:(.*)\n', 'flags': 0},
            'medicines': {'pattern': 'Address[^\n]*(.*)Directions', 'flags': re.DOTALL},
            'directions': {'pattern': 'Directions:(.*)Refill', 'flags': re.DOTALL},
            'refills': {'pattern': 'Refill:(.*)times', 'flags': 0},
        }

        # Get the pattern for the specified field
        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            # Find all matches for the pattern in the document text
            matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
            if len(matches) > 0:
                # Return the first match (trimmed of whitespace)
                return matches[0].strip()

if __name__ == '__main__':
    # Example document text
    document_text = '''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222
Name: Marta Sharapova Date: 5/11/2022
Address: 9 tennis court, new Russia, DC

Prednisone 20 mg
Lialda 2.4 gram
Directions:
Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks -
Lialda - take 2 pill everyday for 1 month
Refill: 3 times
'''
    # Create an instance of PrescriptionParser and parse the document text
    pp = PrescriptionParser(document_text)
    # Print the parsed result
    print(pp.parse())


#line 1 - Regular expressions are powerful tools for pattern matching and text processing.
#         RegEx can be used to check if a string contains the specified search pattern.
#line 2 - This line imports a class named MedicalDocParser from the module parser_generic. 
#line 4 - This line defines a new class named PrescriptionParser, which inherits from the MedicalDocParser class. 
#         This means that PrescriptionParser will have all the methods and properties of MedicalDocParser, 
#         in addition to any new methods or properties defined within PrescriptionParser.
#line 5 - This line defines the constructor method __init__ for the PrescriptionParser class, which takes one argument text. 
#         The constructor initializes an instance of PrescriptionParser with the provided text.
#line 7 - This line calls the constructor of the parent class MedicalDocParser using MedicalDocParser.__init__(self, text). 
#         It passes the text argument to the constructor of the parent class, initializing the PrescriptionParser instance with the provided text.
#line 9 - This line defines the 'parse' method, which is responsible for parsing the document text and returning a dictionary of parsed fields.
#line 11 - This block of code returns a dictionary containing parsed fields extracted from the document text using the get_field method. 
#line 19 - This line defines a method named get_field within the PrescriptionParser class. 
#          This method takes one argument field_name, which represents the name of the field to extract from the document text.
#line 21 - It defines a dictionary named pattern_dict that maps field names to patterns used for extracting those fields from the document text (Using RegEx). 
#          Each pattern is specified as a string, and additional flags are provided for certain patterns to enable features like multiline matching.
#line 30 - This line retrieves the pattern corresponding to the specified field_name from the pattern_dict dictionary and assigns it to the variable pattern_object.
#line 33 - This line of code is using a regular expression pattern to search for all occurrences of a specific pattern in the document text (self.text). 
#          're.findall()' - This is a function from the re module in Python, used for finding all occurrences of a pattern in a string.
#          'pattern_object['pattern']' - This retrieves the regular expression pattern from the pattern_dict dictionary using the field_name. 
#                                        The pattern_dict dictionary contains predefined patterns for different fields in the document.
#          'self.text' - This refers to the text of the document that is being parsed. 
#                        'self' - It is a reference to the current instance of the class, and 
#                        'text' - It is an attribute of that instance which holds the document text.
#          'flags=pattern_object['flags']' - This parameter specifies any optional flags that modify the behavior of the regular expression pattern matching. 
#                                            These flags control aspects such as case sensitivity, multiline matching, and more. 
#                                            The pattern_object['flags'] value is retrieved from the pattern_dict dictionary based on the specified field.
#line 34 - If matches are found for the specified pattern, this block of code returns the first match after stripping leading and trailing whitespace.
#          If no matches are found, the method returns None.
#line 38 - It checks if the script is being run directly (as opposed to being imported as a module). If it is being run directly, the code within the if block will be executed.
#line 40 - This block of code defines an example document text as a multi-line string, containing sample prescription information.
#line 56 - This line creates an instance of the PrescriptionParser class named pp, passing the document_text as an argument to the constructor.
#line 58 - This line calls the parse method on the pp instance of PrescriptionParser and prints the parsed result, which is a dictionary containing extracted fields from the document text.
    
#####  The leading dot (.) in line 2 indicates a relative import from the same package.
#      i.e., -     from .parser_generic import MedicalDocParser
#####  It must be added while running the test_prescription_parser.py