#!/usr/bin/python3
import sys 
import os
from pathlib import Path 
from method import Method
 
global API_KEY
global method

API_KEY = Path(sys.argv[1]).read_text().strip()
method = Method(env='dev', api_key=API_KEY)  


