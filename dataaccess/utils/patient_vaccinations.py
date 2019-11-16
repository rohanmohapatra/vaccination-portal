from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/admin')
db = client.admin

patient_vaccination_details = db.patient_vaccinations

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

data2 = {
	"P2" : [
	{
		"vaccination_id": "V2",
		"vaccination_name" : "Pneumococcal Vaccine",
		"date_given": "12/2/2005"
	},
	{
		"vaccination_id": "V2",
		"vaccination_name" : "Pneumococcal Vaccine",
		"date_given": "13/7/2013"
	},
	{
		"vaccination_id": "V3",
		"vaccination_name" : "Tetanus, Diphtheria, Pertussis Vaccine (Td, Tdap)",
		"date_given: 17/9/2015"
	},
	{
		"vaccination_id": "V3",
		"vaccination_name" : "Tetanus, Diphtheria, Pertussis Vaccine (Td, Tdap)",
		"date_given": "12/2/2007"
	}]
}


patient_vaccination_details.insert_many([data1,data2])
