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

def create_specific_data():
    v_dict = auxillary.get_types_vaccinations()
    print(v_dict)
    d = random.randint(1, int(time.time()))
    date_str = "16/05/2002"
    date_of_birth = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    print(date_of_birth)
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
    p_id = "P" + str(4)
    data = {
        "_id" : p_id,
        p_id : [],
    }
    for j in range(len(immunization_schedule)):
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

create_specific_data()