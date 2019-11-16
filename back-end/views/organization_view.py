from flask import Blueprint, request, jsonify, Response

from dataaccess.get_functions import get_patient_metadata, get_patient_vaccination_data, get_organization
from dataaccess.post_functions import push_to_document, set_something, remove_from_list, remove_document

organization_view = Blueprint('organization_view',__name__)
