# Classification-And-Analysis-of-Unstructured-Data-For-Windows


## Project statement:


Classification and analysis of unstructured data: Need to develop a tool/system which reads the data (There are Terabytes of unstructured data available in various storage systems like servers, local drives, online portals etc. These unstructured data are informed of below categories but not limited to it. Unstructured data available in forms like MS office formats(.xlsx,.docx, .pptx, .txt, .msg, etc), PDF form(scanned and text recognizable), Image form(.jpg. png,etc.), engineering drawing(.dwg, .dgn, etc.), Databases (.accdb, .dgf, .xml, etc.) Non-Engineering Documents: Emails, Presentations, Photos, Videos, Circulars, etc.) from files available in multiple SoRs (System of Records) and suggest what type of record it is, How old it is, when it was accessed by user last. Extract file metadata, etc. (Ref. https://patents.google.com/patent/US8266148B2) Hints: Metadata-based classification using mongoDB



# META-DATA EXTRACTOR
 
  META-DATA EXTRACTOR is a tool for classification and analysis of unstructured data,which extracts metadata of files in the unstructure data 
  using mongoDB.
 
  Thus, it allows Metadata-based classification using mongoDB. 
 
## USAGE
   
   Python3, PyQt5, monngoDB Cluster.
   
## REQUIREMENT
 
   Environment:
  
   Source code to this tool is coded in Python3, with its GUI running in PyQt5 env.
 
 
   Packages:

   subprocess, os, pymongo.


   Command Line Interface(CLI):
  
   exiftool.
 
 
## INSTALLATION 
 
   Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages subprocess, os, pymongo and set env for Python2.
 
   Packages :  

   $ pip install subprocess
   $ pip install os
   $ pip install pymongo

 
### Python3 env :

   $ pip install python3.7 python-pip


### Setting up PyQt5 env for Python3 :

   $ pip install python-pyqt5


   Installing exiftool from https://sno.phy.queensu.ca/~phil/exiftool/install.html#Windows link :
   
   exiftool.exe
 

## USER INSTRUCTIONS
 
   1. Open CMD, and change/move to the directory of the file interface.py ,i.e, mini.

   $ cd /'PATH'/mini

 
   2. Open the tool to start, by executing mdata.py file.
 
   $ python interface.py
 
   
   3. Enter the pathname in the tool for metadata extraction and click on the button for its corresponding type of sorted output.



