from flask import Blueprint, request, jsonify, Response
from flask_cors import CORS, cross_origin
from dataaccess.get_functions import get_patient_metadata, get_patient_vaccination_data, get_organization
from dataaccess.post_functions import push_to_document, set_something, remove_from_list, remove_document, add_vaccination_record
from dataaccess.auxillary import get_types_vaccinations, add_new_vaccination_type

organization_view = Blueprint('organization_view',__name__)

@organization_view.route("/organization_login/",methods=["POST"])
@cross_origin()
def organization_login():
	'''
	{
		"username" : "x",
		"password" : "y"
	}
	'''
	json_data = request.get_json(force=True)
	query = get_organization(json_data["username"])
	print(query)
	data = {"organization_id" : query["organization_id"]}
	if query["password"] == json_data["password"]:
		return jsonify(data)
	else:
		return Response(status=401)

@organization_view.route('/add_patient_vaccination_data',methods=["POST"])
@cross_origin()
def add_patient_vaccination_details():
	json_data = request.get_json(force=True)
	patient_id = json_data["patient_id"]
	vaccination_id = json_data["vaccination_id"]
	date_given = json_data["date_given"]
	vaccination_types = get_types_vaccinations()
	if vaccination_id in vaccination_types:
		vaccination_name = vaccination_types[vaccination_id]["vaccination_name"]
		validity = vaccination_types[vaccination_id]["validity"]
		add_vaccination_record(patient_id,vaccination_name,vaccination_id,date_given,validity)
		return Response(status=200)
	else:
		return Response(status=401)

@organization_view.route('/add_vaccination_type',methods=["POST"])
@cross_origin()
def add_vaccination_type():
	json_data = request.get_json(force=True)
	vaccination_name = json_data["vaccination_name"]
	validity=json_data["validity"]
	vaccination_types = get_types_vaccinations()
	vaccination_id = str(len(vaccination_types)+1)
	add_new_vaccination_type(vaccination_id,vaccination_name,validity)
	return Response(status=200)

@organization_view.route('/view_patients/<organization_id>',methods=["GET"])
@cross_origin()
def view_patients(organization_id):
	organization_data = get_organization(organization_id)
	organization_name = organization_data["organization_name"]
	patients_data = organization_data[patients_data]
	patient_names = []
	for patient_id in patients_data:
		patient_metadata = get_patient_metadata(patient_id)
		patient_name.append(patient_metadata[patient_name])
		response = { organization_name : patient_names}
	return jsonify(response), 200
