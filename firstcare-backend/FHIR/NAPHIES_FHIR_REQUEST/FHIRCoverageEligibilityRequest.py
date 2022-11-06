import datetime
from django.conf import settings
from .constants import client,createUUID
import asyncio


class FHIRCoverageEligibilityRequest:
    def _init__(self):
        self.coverage_eligibility_request = None
        
    async def createCoverageEligibilityRequest(self,patient_id,provider_id,payor_id,location_id,coverage_id,purpose,start_insurance_date,end_insurance_date):
        coverage_request = client.resource(
            'CoverageEligibilityRequest',
            id = createUUID(),
            status="active",
        )
        
        coverage_request.meta= {
            "profile": [
                "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/eligibility-request|1.0.0"
            ]
        }
        coverage_request.identifier = [
					{
						"system": f"{settings.NPHIES_FULL_URL}identifier/coverageeligibilityrequest",
						"value": f"req_{coverage_request.id}"
					}
				]
        coverage_request.priority= {
					"coding": [
						{
							"system": "http://terminology.hl7.org/CodeSystem/processpriority",
							"code": "normal"
						}
					]
				}
        coverage_request.purpose= purpose
        
        coverage_request.patient = {
            # nphies implementation
            # "reference": f"{settings.NPHIES_FULL_URL}Patient/{patient_id}"
            # HAPI implementation  
            "reference": f"Patient/{patient_id}"
        }
        coverage_request.servicedPeriod = {
            "start": start_insurance_date,
            "end": end_insurance_date,
        }
        
        coverage_request.created = datetime.datetime.now().date().strftime('%Y-%m-%d')
        
        coverage_request.provider = {
            "reference": f"{settings.NPHIES_FULL_URL}Organization/{provider_id}"
        }
        coverage_request.insurer= {
            "reference": f"{settings.NPHIES_FULL_URL}Organization/{payor_id}"
        }
        coverage_request.facility = {
					"reference": f"{settings.NPHIES_FULL_URL}Location/{location_id}"
        }
        if coverage_id is not None:
            coverage_request.insurance = [
                {
                    "coverage": {
                        "reference": f"{settings.NPHIES_FULL_URL}Coverage/{coverage_id}"
                    }
                }
            ]
        
        await coverage_request.save()
        self.coverage_eligibility_request = coverage_request
        
        return self.coverage_eligibility_request.serialize()
        