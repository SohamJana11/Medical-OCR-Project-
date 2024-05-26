# Medical Data Extraction OCR Project
Medical Data Extraction using Python, Panda, OpenCV, PyTesseract, RegEx, Unit-Tests &amp; FastAPI

## Problem Statement
Health insurance companies must adhere to numerous government regulations when issuing claims. This involves processing images of patient details and prescriptions provided by hospitals or individual doctors to extract relevant data. To handle this, many insurance companies outsource the task to firms like "Mr. X Data Analytics," which manually extract information from these images.

Mr. X Data Analytics employs software that displays scanned images of patient details or prescriptions. Workers manually input the information from these images into a column on the right side of the interface and select the type of information being entered. Given the manual nature of this process, errors are common. Additionally, during high-demand periods such as the pandemic, the current workforce struggles to manage the large volume of images. Furthermore, insurance companies require that data be processed and returned within 24 hours of submission for extraction. These challenges have compelled Mr. X Data Analytics to consider upgrading their outdated software.

## Solution approach
To address these issues, we are developing a program that can automatically extract data from images. While automation will handle the bulk of the extraction, humans will still play a role by rechecking the extracted data before submission. This approach significantly reduces the time and effort required for manual data entry.

We are utilizing the Python programming language along with the Pytesseract Google library for data extraction and the Regex module for data processing to achieve the desired output.

## Technologies used
* Python <br />
* OOPs <br />
* Pdf2image module <br />
* Opencv <br />
* pytesseract <br />
* Regular expression <br />
* pytest <br />
* Postman <br />
* FastApi <br />

## Workflow
Insert the Technical Architecture

## PDF to Image
For converting PDF to image, we have used pdf2image library.

## Without preprocessing extracting data
Attempted to extract data directly from the source files, but due to their improper format, the extracted data did not meet expectations.

Insert image over here.

## Extracted data from the above image
    

      Dr John Smith, M.D
      2 Non-Important Street,
      New York, Phone (000)-111-2222

      Name: Maria Sharapova Date: 5/11/2022

      Address: 9 tennis court, new Russia, DC

      —momennannenncmneneunnmnnnnninsissiyoinnitnahaadaanih issn earnttneenrenen:

      Prednisone 20 mg
      Lialda 2.4 gram

      3 days,

      or 1 month

## Image processing
We decided to preprocess the images using the OpenCV module before extracting data from them. Initially, we applied normal thresholding, which resulted in the following image.

Insert image

If there is any shadow or noise, normal thresholding can obscure parts of the image, leading to data loss.

To find a better solution, we decided to use adaptive thresholding. This technique divides the image into subregions, applying different thresholding values to each. The result of adaptive thresholding is significantly better than that of normal thresholding.

Insert image.

## After preprocessing the image data extraction

      Dr John Smith, M.D
      2 Non-Important Street,
      New York, Phone (000)-111-2222
      
      Name: Marta Sharapova Date: 5/11/2022
      
      Address: 9 tennis court, new Russia, DC
      
      K
      
      Prednisone 20 mg
      Lialda 2.4 gram
      
      Directions:
      
      Prednisone, Taper 5 mg every 3 days,
      Finish in 2.5 weeks a
      Lialda - take 2 pill everyday for 1 month
      
## Notebook
For all the trials mentioned above, we used Jupyter notebooks to develop small functional components, which can be integrated later during the class design phase.

)))))))))))))))))))))
      
## OOPS design
The code was developed using OOP principles to extract medical data from prescription and patient detail documents.

)))))))))))))))))))))

## Regular expression
Using the regular expressions module, we can match patterns and extract the desired data from the files. For this project, we analyzed the medical files and found that all medical documents follow a consistent pattern. We then wrote regex patterns to match only the required data. Before implementing these patterns in Python, it is advisable to practice and verify them on the regex101 website.

)))))))))))))))))

## Test driven Development
In this project, we used test-driven development to write the code. We used the pytest module for testing. Test cases were created and checked for all methods and the final result while we were developing the code.

))))))))))))))))))))))))))

## FastApi
Used FastAPI for hosting the server of the project. FastApi, as name suggest is help us to develop fast and some other advantages are,

* In build Data validation <br/>
* In build Documentation <br/>
* Fast running and performance <br/>

## Postman
Since this is a backend project, we didn't develop a frontend. To check how the server responds to HTTP requests, we used Postman to send requests and test the responses.

))))))))))))))))))))))))))


## Result
This backend functionality can be added to Mr. X Analytics' existing software to automatically extract data. The extracted data might have some errors, so the person handling the task will need to correct it before submitting the response.

## Benefits
* Mr. X Analytics can save at least 30 seconds for each document. While this may seem like a small amount of time for one document, it adds up significantly over multiple documents. This time-saving can help the company complete more documents within the given time frame, leading to increased profits. <br/>
* The company doesn't need to hire additional staff during peak seasons. <br/>
* Since it involves a combination of automation and manual work, the error rate will be significantly reduced. <br/>

