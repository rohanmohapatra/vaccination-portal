from flask import Blueprint, request, jsonify, Response

from dataaccess.get_functions import get_patient_metadata, get_patient_vaccination_data

patient_view = Blueprint('patient_view', __name__)

