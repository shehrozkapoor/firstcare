from .constants import client,createUUID
from django.conf import settings

class FHIRCoverage:
    def __init__(self):
        self.coverage = None

    async def getCoverageByPatientId(self,document_id):
        coverage =  await client.resources('Coverage').search(beneficiary=document_id).first()
        self.coverage = coverage
        return self.coverage.serialize()

    async def getCoverageById(self,coverage_id):
        coverage = await client.reference('Coverage',coverage_id).to_resource()
        self.coverage = coverage
        return self.coverage.serialize()

    async def updateCoverage(self,coverage_id,status=None):
        coverage = self.getCoverageById(coverage_id)
        coverage = self.coverage
        coverage.status = status
        await coverage.update(status=status)
        return self.coverage.serialize()
    
    async def createCoverage(self,patient_id,org_id):
        coverage = client.resource(
            'Coverage',
            id = createUUID(),
            status="active",
        )
        
        coverage.meta= {
            "profile": [
                "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/coverage|1.0.0"
            ]
        }
        coverage.identifier = [
            {
                "system": "http://sni.com.sa/memberid",
                "value": "0000000001"
            }
        ]
        coverage.type = {
            "coding": [
                {
                    "system": "http://nphies.sa/terminology/CodeSystem/coverage-type",
                    "code": "EHCPOL",
                    "display": "extended healthcare"
                }
            ]
        }
        coverage.subscriber = {
            "reference": f"{settings.NPHIES_FULL_URL}/Patient/{patient_id}"
        }
        coverage.beneficiary = {
            "reference": f"{settings.NPHIES_FULL_URL}/Patient/{patient_id}"
        }
        coverage.relationship = {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/subscriber-relationship",
                    "code": "self",
                    "display": "Self"
                }
            ]
        }
        coverage.payor = [
            {
                "reference": f"{settings.NPHIES_FULL_URL}/Organization/{org_id}"
            }
        ]
        coverage['class'] = [
					{
						"type": {
							"coding": [
								{
									"system": "http://terminology.hl7.org/CodeSystem/coverage-class",
									"code": "group"
								}
							]
						},
						"value": "CB135",
						"name": "Insurance Group A"
					}
            ]
        coverage.network = "Golden C"
        
        await coverage.save()
        self.coverage = coverage
        return self.coverage.serialize()
        