import os
import sys
import json
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import get_functions
def populate_vaccination_details():
    vaccination_details = 0
    with open('vaccination.json') as f:
        vaccination_details = json.loads(f.read())
    print(vaccination_details)

populate_vaccination_details()