from pymongo import MongoClient
#client = MongoClient('mongodb://localhost:27017/cavach')
client = MongoClient("mongodb+srv://cavach:cavach@cavach-drssm.mongodb.net/test?retryWrites=true&w=majority")
db = client.cavach

patient_details = db.patients
#'17/06/1970', '08/04/1987', '08/05/1970'
data1 = {
	"_id" : "P1",
	"patient_id" : "P1",
	"patient_name" : "Rahul",
	"dob" : "17/06/1970",
	"city_of_birth" : "Bangalore",
	"father_name" : "Ajay",
	"mother_name" : "Sangeeta",
	"phone_number" : "9823862874",
	"organization" : ["COL","BGS","APO"],
	"email_address" : "rahulv@gmail.com",
	"username" : "rahulv",
	"password" : "a9993e364706816aba3e25717850c26c9cd0d89d"
}

data2 = {
	"_id" : "P2",
	"patient_id" : "P2",
	"patient_name" : "Anand",
	"dob" : "08/04/1987",
	"city_of_birth" : "Hyderabad",
	"father_name" : "Deepak",
	"mother_name" : "Anjali",
	"phone_number" : "9483123874",
	"organization" : ["MAN","BGS"],
	"email_address" : "silverbellanand@gmail.com",
	"username" : "anand",
	"password" : "a9993e364706816aba3e25717850c26c9cd0d89d"
}

data3 = {
	"_id" : "P3",
	"patient_id" : "P3",
	"patient_name" : "Alan",
	"dob" : "08/05/1970",
	"city_of_birth" : "Chennai",
	"father_name" : "Jordan",
	"mother_name" : "Anita",
	"phone_number" : "9153862874",
	"organization" : ["COL"],
	"email_address" : "alanlobo@gmail.com",
	"username" : "alanlobo",
	"password" : "a9993e364706816aba3e25717850c26c9cd0d89d"
}


patient_details.insert_many([data1,data2,data3])
