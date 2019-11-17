import json
def get_types_vaccinations():
    types_vaccinations = dict()
    with open("/home/rohan/Desktop/Semester7/WebTechnologies2/Project/vaccination-portal/back-end/dataaccess/utils/types_vaccinations.json") as f:
        types_vaccinations = json.loads(f.read())
    return types_vaccinations



def add_new_vaccination_type(vaccination_id, vaccination_name,validity):
    types_vaccinations = dict()
    with open("utils/types_vaccinations.json") as f:
    	types_vaccinations = json.loads(f.read())
    new_vaccination = {
    	vaccination_id:
    		{
    			"vaccination_id": vaccination_id,
    			"vaccination_name": vaccination_name,
    			"validity": validity
    		}
    }
    types_vaccinations.update(new_vaccination)
    with open('utils/types_vaccinations','w') as f:
    	json.dump(types_vaccinations,f)



