from app import app
from views.patient_view import patient_view
from views.organization_view import organization_view

base_url = '/api'

app.register_blueprint(patient_view, url_prefix=base_url+'/patient')
app.register_blueprint(organization_view, url_prefix=base_url+'/organization')


@app.errorhandler(500)
def server_error(e):
    return 'An internal error occurred.',500

if __name__=="__main__":
	app.run(host='0.0.0.0', port=80)
