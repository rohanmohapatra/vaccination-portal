from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/admin')
db = client.admin

vaccination_details = db.vaccinations

data1 = {
	"vaccination_id" : "V1",
	"vaccination_name" : "Flu Vaccine"
	""
}

data2 = {
	"vaccination_id" : "V2",
	"vaccination_name" : "Pneumococcal Vaccine"
}

data3 = {
	"vaccination_id" : "V3",
	"vaccination_name" : "Tetanus, Diphtheria, Pertussis Vaccine (Td, Tdap)"
}

data4 = {
	"vaccination_id" : "V4",
	"vaccination_name" : "Hepatitis A Vaccine"
}

data5 = {
	"vaccination_id" : "V5",
	"vaccination_name" : "Hepatitis B Vaccine"
}

data6 = {
	"vaccination_id" : "V6",
	"vaccination_name" : "Human Papillomavirus (HPV) Vaccine"
}
vaccination_details.insert_many([data1,data2,data3,data4,data5,data6])
