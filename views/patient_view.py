from flask import Blueprint

patient_view = Blueprint('patient_view',__name__)

@patient_view.route("/get_personal_details", methods=('GET'))
def get_personal_details():
    
