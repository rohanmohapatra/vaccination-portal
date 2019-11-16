import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from app import mongo

def get_patient_metadata(patient_id):
	patients_collection = mongo.db.patients
	result = patients_collection.find_one({"patient_id" : patient_id})
	return result

def get_patient_vaccination_data(patient_id):
	vaccinations_collection = mongo.db.vaccinations
	result = vaccinations_collection.find_one({patient_id})
	return result

def get_organization(organization_id):
	organizations_collection = mongo.db.organizations 
	result = organizations_collection.find_one({"organization_id":organization_id})
	return result