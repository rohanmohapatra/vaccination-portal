from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/admin')
db = client.admin

patient_details = db.patients

data1 = {
	"patient_id" : "P1",
	"patient_name" : "Rahul",
	"dob" : "24/11/1997",
	"city_of_birth" : "Bangalore",
	"father_name" : "Ajay",
	"mother_name" : "Sangeeta",
	"phone_number" : "9823862874",
	"organization" : ["COL","BGS","APO"],
	"email_address" : "rahulv@gmail.com"
}

data2 = {
	"patient_id" : "P2",
	"patient_name" : "Anand",
	"dob" : "24/11/1997",
	"city_of_birth" : "Hyderabad",
	"father_name" : "Deepak",
	"mother_name" : "Anjali",
	"phone_number" : "9483123874",
	"organization" : ["MAN","BGS"],
	"email_address" : "silverbellanand@gmail.com"
}

data3 = {
	"patient_id" : "P3",
	"patient_name" : "Alan",
	"dob" : "24/11/1997",
	"city_of_birth" : "Chennai",
	"father_name" : "Jordan",
	"mother_name" : "Anita",
	"phone_number" : "9153862874",
	"organization" : ["COL"],
	"email_address" : "alanlobo@gmail.com"
}


patient_details.insert_many([data1,data2,data3])
