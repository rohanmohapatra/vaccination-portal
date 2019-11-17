import json
def get_types_vaccinations():
    types_vaccinations = dict()
    with open("/home/rohan/Desktop/Semester7/WebTechnologies2/Project/vaccination-portal/back-end/dataaccess/utils/types_vaccinations.json") as f:
        types_vaccinations = json.loads(f.read())
    return types_vaccinations