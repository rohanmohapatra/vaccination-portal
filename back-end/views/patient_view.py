from flask import Blueprint,Response, jsonify, request
from dataaccess.get_functions import *
from flask_cors import CORS, cross_origin
import json

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
def get_patient_id():
    json_data = request.get_json(force=True)
    data = get_patient_metadata_with_username(json_data["username"])
    return jsonify({"patient_id":data["patient_id"]})

@patient_view.route("/get_patient_vaccination_details/<patient_id>", methods=["GET"])
def get_patient_vaccination_details_controller(patient_id):
    data = get_patient_vaccination_data(patient_id)
    return jsonify(data[patient_id])
