import os
import sys
import json
import random
import time
import datetime
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import get_functions
import post_functions
import auxillary
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/cavach')
db = client.cavach

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





def generate_vaccination_details():
    v_dict = auxillary.get_types_vaccinations()
    print(v_dict)
    dob=[]
    for i in range(100):
        random.seed(random.randint(1,9000))
        d = random.randint(1, int(time.time()))
        date_of_birth = datetime.datetime.fromtimestamp(d).date()
        print(date_of_birth)
        dob.append(date_of_birth)
        immunization_schedule =[
            {
                "vaccination_names" : ["V1", "V2", "V3"],
                "vaccination_time" : date_of_birth.strftime("%d/%m/%Y")
            },
            {
                "vaccination_names" : ["V4", "V2", "V3"],
                "vaccination_time" : (date_of_birth + datetime.timedelta(weeks=6)).strftime("%d/%m/%Y")
            },
            {
                "vaccination_names" : ["V4", "V2", "V3"],
                "vaccination_time" : (date_of_birth + datetime.timedelta(weeks=10)).strftime("%d/%m/%Y")
            },
            {
                "vaccination_names" : ["V4", "V2", "V3"],
                "vaccination_time" : (date_of_birth + datetime.timedelta(weeks=14)).strftime("%d/%m/%Y")
            },
            {
                "vaccination_names" : ["V5", "V6"],
                "vaccination_time" : (date_of_birth + datetime.timedelta(days=270)).strftime("%d/%m/%Y")
            },
            {
                "vaccination_names" : ["V4", "V2", "V5", "V6"],
                "vaccination_time" : (date_of_birth + datetime.timedelta(days=500)).strftime("%d/%m/%Y")
            },
            {
                "vaccination_names" : ["V4"],
                "vaccination_time" : (date_of_birth + datetime.timedelta(days=1825)).strftime("%d/%m/%Y")
            },
            {
                "vaccination_names" : ["V7"],
                "vaccination_time" : (date_of_birth + datetime.timedelta(days=4015)).strftime("%%d/%m/%Y")
            }
        ]
        p_id = "P" + str(i)
        data = {
            "_id" : p_id,
            p_id : [],
        }
        for j in range(random.randint(1,len(immunization_schedule))):
            each = immunization_schedule[j]
            for vaccine in each["vaccination_names"]:
                in_data ={
                    "vaccination_id" : vaccine,
                    "vaccination_name" : v_dict[vaccine]["vaccination_name"],
                    "date_given" : each["vaccination_time"],
                    "validity" : v_dict[vaccine]["validity"]
                }
                data[p_id].append(in_data)
        
        print(data)
        db.vaccinations.insert_one(data)
    with open("file.txt","w") as f:
        f.write("{},".format([i.strftime("%d/%m/%Y") for i in dob]))
    '''
    data1 = {
	"P1" : [
	{
		"vaccination_id": "V1",
		"vaccination_name": "Flu Vaccine",
		"date_given": "12/2/2005"
	},
	{
		"vaccination_id": "V5",
		"vaccination_name" : "Hepatitis B Vaccine",
		"date_given": "13/7/2013"
	},
	{
		"vaccination_id": "V3",
		"vaccination_name" : "Tetanus, Diphtheria, Pertussis Vaccine (Td, Tdap)",
		"date_given: 17/9/2015"
	},
	{
		"vaccination_id": "V1",
		"vaccination_name" : "Flu Vaccine",
		"date_given": "12/2/2007"
	}]
    }
    '''
#populate_vaccination_details()
generate_vaccination_details()