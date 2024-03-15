import sys
import os

# Add parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parser_prescription import PrescriptionParser
import pytest

@pytest.fixture()
def doc_1_maria():
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
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_2_virat():
    document_text = '''
Dr John >mith, M.D

2 Non-Important street,
New York, Phone (900)-323- ~2222

Name:  Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

Omeprazole 40 mg

Directions: Use two tablets daily for three months
Refill: 3 times
'''
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_3_empty():
    return PrescriptionParser('')

def test_get_name(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_field('patient_name') == 'Marta Sharapova'
    assert doc_2_virat.get_field('patient_name') == 'Virat Kohli'
    assert doc_3_empty.get_field('patient_name') == None

def test_get_address(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_field('patient_address') == '9 tennis court, new Russia, DC'
    assert doc_2_virat.get_field('patient_address') == '2 cricket blvd, New Delhi'
    assert doc_3_empty.get_field('patient_address') == None

def test_get_address(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_field('patient_address') == '9 tennis court, new Russia, DC'
    assert doc_2_virat.get_field('patient_address') == '2 cricket blvd, New Delhi'
    assert doc_3_empty.get_field('patient_address') == None

def test_get_medicines(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_field('medicines') == 'Prednisone 20 mg\nLialda 2.4 gram'
    assert doc_2_virat.get_field('medicines') == 'Omeprazole 40 mg'
    assert doc_3_empty.get_field('medicines') is None

def test_get_directions(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_field('directions') == 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks -\nLialda - take 2 pill everyday for 1 month'
    assert doc_2_virat.get_field('directions') == 'Use two tablets daily for three months'
    assert doc_3_empty.get_field('directions') is None

def test_parse(doc_1_maria, doc_2_virat, doc_3_empty):
    record_maria = doc_1_maria.parse()
    assert record_maria['patient_name'] == 'Marta Sharapova'
    assert record_maria['patient_address'] == '9 tennis court, new Russia, DC'
    assert record_maria['medicines'] == 'Prednisone 20 mg\nLialda 2.4 gram'
    assert record_maria['directions'] == 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks -\nLialda - take 2 pill everyday for 1 month'
    assert record_maria['refills'] == '3'

    record_virat = doc_2_virat.parse()
    assert record_virat == {
        'patient_name': 'Virat Kohli',
        'patient_address': '2 cricket blvd, New Delhi',
        'medicines': 'Omeprazole 40 mg',
        'directions': 'Use two tablets daily for three months',
        'refills': '3'
    }

    record_empty = doc_3_empty.parse()
    assert record_empty == {
        'patient_name': None,
        'patient_address': None,
        'medicines': None,
        'directions': None,
        'refills': None
    }


#line 1 - 'sys' provides access to some variables used or maintained by the Python interpreter and 
#         to functions that interact with the interpreter. 
#line 2 - 'os' provides a portable way of using operating system-dependent functionality.
#line 5 - This line adds the parent directory of the current file to the Python path. 
#         This is done to ensure that Python can locate modules or packages located in the parent directory.
#line 7 - This line imports the PrescriptionParser class from a module named parser_prescription located in the src directory. 
#         This class is responsible for parsing prescription documents.
#line 8 - This line imports the pytest library, which is a testing framework for Python.
#         It allows for writing simple and scalable tests for Python code.
#line 10 - This is a decorator provided by pytest for defining fixtures, 
#          which are functions that provide test data or set up the environment for tests.
#line 11 - This line defines a fixture named doc_1_maria. Fixtures are functions that provide data or set up the test environment. 
#          This fixture returns a PrescriptionParser instance initialized with a predefined document_text.
#The next several lines define similar fixtures doc_2_virat and doc_3_empty, each returning a PrescriptionParser instance initialized with different document_text.
#line 52 - This line defines a test function named test_get_name that takes the doc_1_maria, doc_2_virat, and doc_3_empty fixtures as arguments. 
#          This test function tests the get_field method of PrescriptionParser for extracting patient names.
#line 53 - The next few lines contain assertions testing the behavior of the get_field method for extracting patient names from different prescription documents.
#Similar test functions are defined for testing other methods (get_address, get_medicines, get_directions, and parse) of the PrescriptionParser class.
#The tests assert various properties of the parsed data, ensuring that the PrescriptionParser class behaves as expected for different input scenarios.
    
#This script sets up fixtures representing different prescription documents, and then defines test functions to verify the correctness of the PrescriptionParser class methods for parsing and extracting information from these documents.