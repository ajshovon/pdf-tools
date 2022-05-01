# Python Script To Manipulate Pdf (WIP)

## Requirements
- Python3 installed

## Setup
- `pip3 install -r requirements.txt`


## Available options for now

```
$ python pdf-tools.py
usage: pdf-tools.py [-h] [-d {even,odd}] [-i FILENAME] [-o FILENAME] [-e FOLDERNAME]

PDF tools written in python with PyPDF2...

options:
  -h, --help            show this help message and exit
  -d {even,odd}, --delete {even,odd}
                        Delete every even or odd number pages
  -i FILENAME, --input FILENAME
                        Enter target pdf name
  -o FILENAME, --output FILENAME
                        Enter new pdf name
  -e FOLDERNAME, --export FOLDERNAME
                        Export each page separately to given folder
```