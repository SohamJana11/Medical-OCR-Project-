import sys
import os

# Add parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parser_patient_details import PatientDetailsParser
import pytest

@pytest.fixture()
def doc_1_kathy():
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

    Migraine
    '''

    return PatientDetailsParser(document_text)


@pytest.fixture()
def doc_2_jerry():
    document_text = '''
    Patient Medical Record

    Patient Information
    Jerry Lucas

    (279) 920-8204

    4218 Wheeler Ridge Dr
    Buffalo, New York, 14201
    United States

    In Case of Emergency

    -_ OCC OO eee

    Joe Lucas

    Home phone

    General Medical History



    Chicken Pox (Varicelia):
    IMMUNE
    Have you had the Hepatitis B vaccination?

    Yes”

    Birth Date
    May 2 1998

    Weight:
    57

    Height:
    170

    4218 Wheeler Ridge Dr
    Buffalo, New York, 14201
    United States

    Work phone

    Measles: .

    NOT IMMUNE

    List any Medical Problems (asthma, seizures, headaches):

    N/A
        '''
    return PatientDetailsParser(document_text)

def test_get_patient_name(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_patient_name() == 'Kathy Crawford'
    assert doc_2_jerry.get_patient_name() == 'Jerry Lucas'

def test_get_patient_phone_number(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_patient_phone_number() == '(737) 988-0851'
    assert doc_2_jerry.get_patient_phone_number() == '(279) 920-8204'


def test_get_hepatitis_b_vaccination(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_hepatitis_b_vaccination() == 'No'
    assert doc_2_jerry.get_hepatitis_b_vaccination() == 'Yes'


def test_get_medical_problems(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_medical_problems() == 'Migraine'
    assert doc_2_jerry.get_medical_problems() == 'N/A'

def test_parse(doc_1_kathy, doc_2_jerry):
    record_kathy = doc_1_kathy.parse()
    assert record_kathy['patient_name'] == 'Kathy Crawford'
    assert record_kathy['phone_number'] == '(737) 988-0851'
    assert record_kathy['medical_problems'] == 'Migraine'
    assert record_kathy['hepatitis_b_vaccination'] == 'No'



#line 1 - 'sys' provides access to some variables used or maintained by the Python interpreter and 
#         to functions that interact with the interpreter. 
#line 2 - 'os' provides a portable way of using operating system-dependent functionality.
#line 5 - This line adds the parent directory of the current file to the Python path. 
#         This is done to ensure that Python can locate modules or packages located in the parent directory.
#line 7 - This line imports the PatientDetailsParser class from a module named parser_patient_details located in the src directory. 
#         This class is responsible for parsing patient details documents.
#line 8 - This line imports the pytest library, which is a testing framework for Python.
#         It allows for writing simple and scalable tests for Python code.
#line 10 - This is a decorator provided by pytest for defining fixtures, 
#          which are functions that provide test data or set up the environment for tests.
#line 11 - This line defines a fixture named doc_1_kathy. Fixtures are functions that provide data or set up the test environment. 
#          This fixture returns a PatientDetailsParser instance initialized with a predefined document_text representing details for a patient named Kathy.
#The next few lines define similar fixtures doc_2_jerry, each returning a PatientDetailsParser instance initialized with different document_text representing details for a patient named Jerry.
#line 106 - This line defines a test function named test_get_patient_name that takes the doc_1_kathy and doc_2_jerry fixtures as arguments. 
#           This test function tests the get_patient_name method of PatientDetailsParser for extracting patient names.
#Similar test functions are defined for testing other methods (get_patient_phone_number, get_hepatitis_b_vaccination, get_medical_problems, and parse) of the PatientDetailsParser class.
#The tests assert various properties of the parsed data, ensuring that the PatientDetailsParser class behaves as expected for different input scenarios.
    
#This script sets up fixtures representing different patient details documents, and then defines test functions to verify the correctness of the PatientDetailsParser class methods for parsing and extracting information from these documents.