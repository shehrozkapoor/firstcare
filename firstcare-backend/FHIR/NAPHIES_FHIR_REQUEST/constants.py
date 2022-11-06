from fhirpy import AsyncFHIRClient
from django.conf import settings
import uuid



client = AsyncFHIRClient(settings.FHIR_ENDPOINT,authorization=settings.FHIR_AUTHORIZATION,extra_headers={
    'content-type': 'application/fhir+json;charset=utf-8'
})

def createUUID():
    return str(uuid.uuid4())

class FHIR:
    def __init__(self):
        self.resource = None
    
    async def createResourceBundleResponseJson(self,json_body):
        bundle = client.resource(
            'Bundle',
            id = json_body['id'],
            meta = json_body['meta'],
            type = json_body['type'],
            timestamp = json_body['timestamp'],
            entry = json_body['entry']
        )
        await bundle.save()
        self.bundle = bundle
        return self.bundle.serialize()
    
    def createCareTeam(self,doctor):
        return [{
        "sequence": 1,
        "provider": {
            "reference": f"{settings.NPHIES_FULL_URL}Practitioner/{doctor.fhir_practitioner_id}"
        },
        "role": {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/claimcareteamrole",
                    "code": "primary"
                }
            ]
        },
        "qualification": {
            "coding": [
                {
                    "system": "http://nphies.sa/terminology/CodeSystem/practice-codes",
                    "code": doctor.practice_code
                }
            ]
        }
    }]
    def createDiagnosis(self,icd_10_codes):
        return [{
        "sequence": 1,
        "onAdmission": {
            "coding": [
                {
                    "system": "http://nphies.sa/terminology/CodeSystem/diagnosis-on-admission",
                    "code": "y"
                }
            ]
        },
        "diagnosisCodeableConcept": {
            "coding": [{
                    "system": "http://hl7.org/fhir/sid/icd-10-am",
                    "code": code.code
                    } for code in icd_10_codes]
        },
        "type": [
            {
                "coding": [
                    {
                        "system": "http://nphies.sa/terminology/CodeSystem/diagnosis-type",
                        "code": "principal"
                    }
                ]
            }
        ]
    }]
        
    def createSupportingInfo(self,vital_signs):
        return [{"sequence":i+1,"category": {
            "coding": [
                {
                    "system": "http://nphies.sa/terminology/CodeSystem/claim-information-category",
                    "code": vital_signs[i].code
                }
            ]
        },"valueQuantity": {
            "value": vital_signs[i].value,
            "system": "http://unitsofmeasure.org",
            "code": vital_signs[i].unit_of_measure.name
        }} for i in range(0,len(vital_signs))]
        
    def createProductServices(self,hcpcs):
        return [{
        "system": "http://nphies.sa/terminology/CodeSystem/services",
        "code": item.hcpcs_item.code,
        "display": item.hcpcs_item.name
    } for item in hcpcs]
    
    def createCareTeamManual(self,careteam):
        return [{
        "sequence": i+1,
        "provider": {
            "reference": f"{settings.NPHIES_FULL_URL}Practitioner/{careteam[i].practitioner.fhir_practitioner_id}"
        },
        "role": {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/claimcareteamrole",
                    "code": careteam[i].practitioner_role 
                }
            ]
        },
        "qualification": {
            "coding": [
                {
                    "system": "http://nphies.sa/terminology/CodeSystem/practice-codes",
                    "code": careteam[i].practitioner.practice_code
                }
            ]
        }
    }for i in range(0,len(careteam))]
        
        
        
    def createDiagnosisManual(self,diagnosis):
        return [{
        "sequence": 1,
        "onAdmission": {
            "coding": [
                {
                    "system": "http://nphies.sa/terminology/CodeSystem/diagnosis-on-admission",
                    "code": diagnose.on_admission
                }
            ]
        },
        "diagnosisCodeableConcept": {
            "coding": [{
                    "system": "http://hl7.org/fhir/sid/icd-10-am",
                    "code": diagnose.icd_10.code
                    }]
        },
        "type": [
            {
                "coding": [
                    {
                        "system": "http://nphies.sa/terminology/CodeSystem/diagnosis-type",
                        "code": diagnose.type
                    }
                ]
            }
        ]
    }for diagnose in diagnosis]
        
        
    def createSupportingInfoManual(self,infos):
        
        return [{"sequence":i+1,"category": {
            "coding": [
                {
                    "system": "http://nphies.sa/terminology/CodeSystem/claim-information-category",
                    "code": infos[i].category
                }
            ]
        },"valueQuantity": {
            "value": infos[i].value,
            "system": "http://unitsofmeasure.org",
            "code": infos[i].code
        }} for i in range(0,len(infos))]
        
    def createProductServicesManual(self,hcpcs):
        return [{
        "system": "http://nphies.sa/terminology/CodeSystem/services",
        "code": item.hcpcs_item.code,
        "display": item.hcpcs_item.name
    } for item in hcpcs]
    

    def createItemsManual(self,items):
        return [
            {
                "extension": [
                    {
                        "url": "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/extension-tax",
                        "valueMoney": {
                            "value": items[i].tax,
                            "currency": "SAR"
                        }
                    },
                    {
                        "url": "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/extension-patient-share",
                        "valueMoney": {
                            "value": items[i].patient_share,
                            "currency": "SAR"
                        }
                    },
                    {
                        "url": "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/extension-patientInvoice",
                        "valueIdentifier": {
                            "system": "http://sgh.com/patientInvoice",
                            "value": "Invc-20220120/IP-1110987"
                        }
                    },
                    {
                        "url": "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/extension-package",
                        "valueBoolean": False
                    }
                ],
                "sequence": i+1,
                "careTeamSequence": [i+1 for i in range(0,len(items[i].care_teams.all()))],
                "diagnosisSequence": [i+1 for i in range(0,len(items[i].diagnoses.all()))],
                "informationSequence": [i+1 for i in range(0,len(items[i].support_info.all()))],
                "productOrService": {
                    "coding": [
                        {
                            "system": "http://nphies.sa/terminology/CodeSystem/services",
                            "code": "83600-00-00",
                            "display": "General Practitioner Consultation"
                        }
                    ]
                },
                "servicedDate": items[i].start_DateTime,
                "quantity": {
                    "value": items[i].quantity
                },
                "unitPrice": {
                    "value": items[i].unit_price,
                    "currency": "SAR"
                },
                "net": {
                    "value": items[i].net,
                    "currency": "SAR"
                }
            } for i in range(0,len(items))]