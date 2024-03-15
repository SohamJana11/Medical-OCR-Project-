from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from extractor import extract
import uuid
import os

app = FastAPI()


@app.post("/extract_from_doc")
def extract_from_doc(
        file_format: str = Form(...),
        file: UploadFile = File(...),
):
    contents = file.file.read()

    file_path = "../uploads/" + str(uuid.uuid4()) + ".pdf"

    with open(file_path,"wb") as f:
        f.write(contents)

    try:
        data = extract(file_path, file_format)
    except Exception as e:
        data = {
            'error': str(e)
        }

    if os.path.exists(file_path):
        os.remove(file_path)

    return data

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


#line 1 - This line imports necessary classes and functions from the FastAPI framework. 
#         FastAPI is the main class for creating FastAPI applications. 
#         Form, UploadFile, and File are classes used for handling form data and file uploads.
#line 2 - This line imports the uvicorn module, which is a lightning-fast ASGI server implementation used to run FastAPI applications.
#  ASGI ((Asynchronous Server Gateway Interface)) server enables asynchronous communication between web servers and applications, 
#  allowing for concurrent handling of multiple requests in Python web applications.
#line 3 - This line imports the extract function from a module named extractor. 
#         This function is responsible for extracting data from documents.
#line 4 - This line imports the uuid module, which provides functions for generating universally unique identifiers (UUIDs).
#line 5 - This line imports the os module, which provides functions for interacting with the operating system.
#line 7 - This line creates an instance of the FastAPI class, which represents the FastAPI application.
#line 10 - This line defines a route for handling HTTP POST requests to the /extract_from_doc endpoint.
#line 11 - his line defines a function named extract_from_doc, which is the handler for requests to the /extract_from_doc endpoint.
#line 12 - This line defines a parameter named file_format of type str. It's annotated with Form(...), 
#          indicating that this parameter is expected to be passed as form data.
#line 13 - This line defines a parameter named file of type UploadFile. It's annotated with File(...), 
#          indicating that it's expected to receive file upload data.
#line 15 - This line reads the contents of the uploaded file using the read() method of the file object.
#line 17 - This line generates a unique filename for the uploaded file by concatenating the path to the uploads directory, 
#          a UUID generated using uuid.uuid4(), and the .pdf extension.
#line 19 - This line opens the file specified by file_path in binary write mode ("wb").
#line 20 - This line writes the contents of the uploaded file to the file opened in the previous step.
#line 22 - This line starts a try block to handle potential exceptions.
#line 23 - This line calls the extract function imported earlier to extract data from the uploaded file. 
#          The extracted data is stored in the data variable.
#line 24 - This line catches any exceptions that occur within the try block and assigns the exception object to the variable e.
#line 25 - This line creates a dictionary with an error message extracted from the exception, converting it to a string.
#line 29 - This line checks if the file specified by file_path exists.
#line 30 - This line removes the file specified by file_path from the filesystem.
#line 32 - This line returns the extracted data or an error message as a JSON response.
#line 34 - This line checks if the script is being run directly as the main program.
#line 35 - This line runs the FastAPI application using the Uvicorn server, specifying the host (127.0.0.1) and port (8000) to listen on.