import os
import sys
import json
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import get_functions
import post_functions

def populate_vaccination_details():
    vaccination_details = 0
    with open('vaccination.json') as f:
        vaccination_details = json.loads(f.read())

    for eachPatient in vaccination_details:
        for eachVaccine in eachPatient:
            for i in range(len(eachPatient[eachVaccine])):
                print(eachPatient[eachVaccine][i])
                print(eachVaccine, 
                eachPatient[eachVaccine][i]["vaccination_name"], 
                eachPatient[eachVaccine][i]["vacc_id"], 
                eachPatient[eachVaccine][i]["date_given"], 
                eachPatient[eachVaccine][i]["validity"])

                post_functions.add_vaccination_record(eachVaccine, 
                eachPatient[eachVaccine][i]["vaccination_name"], 
                eachPatient[eachVaccine][i]["vacc_id"], 
                eachPatient[eachVaccine][i]["date_given"], 
                eachPatient[eachVaccine][i]["validity"]
                )


populate_vaccination_details()