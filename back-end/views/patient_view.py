from flask import Blueprint,Response, jsonify, request
from dataaccess.get_functions import *
from flask_cors import CORS, cross_origin
import json
import time
import datetime

patient_view = Blueprint('patient_view',__name__)

@patient_view.route("/")
def test_patient():
    print("Working")
    return Response(status=200)

@patient_view.route("/get_personal_details/<patient_id>", methods=['GET'])
@cross_origin()
def get_personal_details_with_id(patient_id):
    print("View Reached with id{}".format(patient_id))
    data = get_patient_metadata(patient_id)
    print(type(data))
    data.pop("username",None)
    data.pop("password",None)
    return jsonify(data)

@patient_view.route("/get_personal_details/", methods=['GET'])
def get_personal_details():
    print("View Reached with ")
    return Response(status=200)

@patient_view.route("/get_patient_id/",methods=["POST"])
@cross_origin()
def get_patient_id():
    json_data = request.get_json(force=True)
    data = get_patient_metadata_with_username(json_data["username"])
    return jsonify({"patient_id":data["patient_id"]})

@patient_view.route("/get_patient_vaccination_details/<patient_id>", methods=["GET"])
@cross_origin()
def get_patient_vaccination_details_controller(patient_id):
    data = get_patient_vaccination_data(patient_id)
    return jsonify(data[patient_id])

@patient_view.route("/login/", methods=["POST"])
@cross_origin()
def patient_login():
    '''
    {
        "username" : "x",
        "password" : "y"
    }
    '''
    json_data = request.get_json(force=True)
    query = get_patient_metadata_with_username(json_data["username"])
    if query["password"] == json_data["password"]:
        return Response(status=200)
    else:
        return Response(status=401)

def get_message():
    '''this could be any function that blocks until data is ready'''
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s


@patient_view.route('/stream')
@cross_origin()
def stream():
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            yield 'data: {}\n\n'.format(get_message())
    return Response(eventStream(), mimetype="text/event-stream")


@patient_view.route('/get_remainders/<patient_id>')
@cross_origin()
def get_remainders(patient_id):
    def eventStream():
        data = get_patient_metadata(patient_id)
        date_str = data["dob"]
        date_of_birth = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()

        immunization_schedule =[
            {
                "vaccination_names" : "BCG, OPV-0, Hepatitis-B",
                "vaccination_time" : date_of_birth.strftime("%d %B, %Y")
            },
            {
                "vaccination_names" : "DPT-1, OPV-1, Hepatitis-B-1",
                "vaccination_time" : (date_of_birth + datetime.timedelta(weeks=6)).strftime("%d %B, %Y")
            },
            {
                "vaccination_names" : "DPT-2, OPV-2, Hepatitis-B-2",
                "vaccination_time" : (date_of_birth + datetime.timedelta(weeks=10)).strftime("%d %B, %Y")
            },
            {
                "vaccination_names" : "DPT-3, OPV-3, Hepatitis-B-3",
                "vaccination_time" : (date_of_birth + datetime.timedelta(weeks=14)).strftime("%d %B, %Y")
            },
            {
                "vaccination_names" : "Measeles, Vitamin A-1",
                "vaccination_time" : (date_of_birth + datetime.timedelta(days=270)).strftime("%d %B, %Y")
            },
            {
                "vaccination_names" : "DPT, OPV-Booster, Measeles, Vitamin-A-2",
                "vaccination_time" : (date_of_birth + datetime.timedelta(days=480)).strftime("%d %B, %Y") +" to " + (date_of_birth + datetime.timedelta(days=730)).strftime("%d %B, %Y")
            },
            {
                "vaccination_names" : "DPT Booster-2",
                "vaccination_time" : (date_of_birth + datetime.timedelta(days=1825)).strftime("%d %B, %Y")
            },
            {
                "vaccination_names" : "TT",
                "vaccination_time" : (date_of_birth + datetime.timedelta(days=4015)).strftime("%d %B, %Y")
            },
        ]

        for i in immunization_schedule:
            # wait for source data to be available, then push it
            yield 'data: {}\n\n'.format(get_reminder_stream(i["vaccination_names"],i["vaccination_time"]))
    return Response(eventStream(), mimetype="text/event-stream")

def get_reminder_stream(vaccination_name, vaccination_time):
    time.sleep(5.0)
    s = "Reminder for getting {} on {}".format(vaccination_name, vaccination_time)
    return s

