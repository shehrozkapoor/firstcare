## Getting started

Steps:
```
1. git clone https://github.com/aloalqma/firstcare.git
2. pip install virtualenv
3. virtualenv venv
4. source venv/bin/activate
5. pip install -r requirements.txt
6. python3 manage.py runserver
```

## deployment serve access
ssh firstcare1@20.115.112.82
ASDFasdf123456

```
1. push your updated code to the production branch
2. login to ssh
3. pull your changes
4. sudo systemctl restart nginx
5. sudo systemctl restart gunicorn
```

### Production Server Configurations
frontend is running using **nginx**
backend is running using **gunicorn**

**nginx config**
if you go on the server to this
sudo nano /etc/nginx/sites-available/firstcare
on port 8000 the django admin,drchrono insurance,
and the vue3 application is running on the port 80



## Project Structure
- main folder
    - sub folder
        -another sub folder
#### description
__project structure is tree like structure__
###### example
- management
    - bed_management
        - api
    - doctor_management
        - api
    - inpatient_management
    - outpatient_management
        - clinic_management
            - api
    - schedule_management
        - api
    - ward_management
        - api

## API TESTING AND POSTMAN COLLECTION
FIRST CARE.postman_collection.json
__description__
all the api that are present are tested with the server you can just import the collection into the postman and use that
**Note**i have created the same tree structure in the postman as well so you can also get the idea of the project structure and the API's url according to the structure in the project as well

## Folder with their descriptions
1. accounts
__description__
__all the models and function and API"s that are handling the account is available in the account folder__
**Note:**__this is the main userModel and Api's this account has no relation or not dependent on other modules__
2. firstcare
__description__
__all the project setting and configurations are in the firstcare__

3. billing
__description__
__all the billing models and API's are in the billing__

**Note:**__there are two insurance modules one is [drchrono](https://www.drchrono.com) and other is EMS Insurance
4. drchrono_insurance
__description__
we were working before on the EMS insurance then we quit and then start working on the drchrono insuracne for the reference you can signup on the drchrono and see their system to get the idea how our system is working.

### How to run HAPI in Local
##### prerequisite
make sure you have the docker downloaded in your desktop
```
1. open cmd or terminal
2. git clone https://github.com/hapifhir/hapi-fhir-jpaserver-starter.git
3. cd hapi-fhir-jpaserver-starter
4. ./build-docker-image.sh && docker run -p 8080:8080 hapi-fhir/hapi-fhir-jpaserver-starter:latest
```

5. FHIR
### what is FHIR
FHIR are the internation standards for the healthcare system [FHIR](https://www.hl7.org/fhir/)
__description__
all the implementation of FHIR is in the FHIR module but this is not the complete FHIR implementation because we found a better solution we have the opensource already build FHIR implementation [HAPI](https://github.com/hapifhir/hapi-fhir-jpaserver-starter.git)
**visit this [link](https://github.com/hapifhir/hapi-fhir-jpaserver-starter.git)this is the complete FHIR implementation it provides you the API so we can perform CRUD operations**
you can setup the HAPI project in your local and test it.
to perform the queries we can not do it directly so that's why we are using the [FHIRCLIENT](https://pypi.org/project/fhirclient/) pypi page and this is the main website [FHIR-CLIENT](https://smart-on-fhir.github.io/client-py)

The implementation of the FHIRPY is in FHIR/fhir.py

## **Note:How to use FHIR in any module**
##### __description__
__first you need to understand the fhir resources then HAPI server what is [HAPI](https://github.com/hapifhir/hapi-fhir-jpaserver-starter.git) then you need to understand the workflow of [FHIRPY](https://pypi.org/project/fhirpy/) and the FHIRPY is most important thing you will be mostly dealing with.Using FHIRPY you can perform CRUD operations on HAPI if you go to the FHIR/fhir.py i have created some of the classes and using fhir client e.g. FHIRPatient__

### How to use FHIRPatient in any other module.
__description__
__example 1__
```
import FHIRPatient from FHIR.fhir
fhir_patient = FHIRPatient()
response = fhir_patient.createPatient(data=patient)
print(response)
```
__data=patient data will be the information that will be saved into the FHIR implementation e.g. HAPI.__

__example 2__
```
import FHIRCoverageEligibility from FHIR.fhir
fhir_coverage = FHIRCoverageEligibility()
response = fhir_coverage.updateEligibilityStatus(coverage_id=coverage_id)
print(response)
```
__if you need to see the classes you can go to the billing.fhir__

__example 3__
```
import FHIRCoverageEligibility from FHIR.fhir
fhir_coverage = FHIRCoverageEligibility()
response = fhir_coverage.getEligibility(patient_id=patient_id)
```

6. Insurance
this is the implementation for the old OPENIMS insurance implementation.

7. Laboratory
all the implementation for laboratory will be in the laboratory folder i have created some of the models in the Laboratory but this module is still under development.

8. management
all the management for the patient healthcare record system held in management.

9. media
all the images or the media will be saved in the media folder

10. Medical_report
all the medical reports will be in the medical report and some of the models are created but no API's for medical report has been built

11. Patient
all the patient models and API's are in the Patient also implemented the Patient with FHIR.
when you will create any patient in the our system it will also be created in the FHIR

12. Patient_health_record

all the patient health record are present here

13. Radiology
all the Radiology will be here

14. rest_auth
__description__
this is the authentication library for the python [rest-auth-pypi](https://django-rest-auth.readthedocs.io/en/latest/installation.html)

## why put the rest_auth in the project folder instead of virtual env?
**ans** this was not compatible with the current python version so i made some changes in the default library that are not too complex changes a little bit import issues were there.

15. templates
all the templates are present in the templates.
we have implemented the Drchrono insurance through the AngularJS.so all the javascript and css are present in the static_files and all the templates are in the templates.
patient healthcare record and patient management is implemented by using the Vue3 only the Insurance is implemented by the AngularJs.
