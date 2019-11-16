import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from app import mongo



def add_vaccination_record(patient_id,vacination_name,vacc_id,date_given,validity):
    vaccination_collection = mongo.db.vaccinations
    query_result = vaccination_collection.find_one({"_id":patient_id})
    print(query_result)
    data = dict()
    data["vacination_name"] = vacination_name
    data["vacc_id"] = vacc_id
    data["date_given"] = date_given
    data["validity_in_days"] = validity
    if(query_result == None):
        vaccination_collection.insert_one({"_id":patient_id, patient_id:[data]})
    else:
        update_result = vaccination_collection.update_one(
            {"_id" : patient_id},
            {'$push': {patient_id:data}}
        )
    


	