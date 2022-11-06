import asyncio
from .constants import client



class FHIRPractitioner:
    def __init__(self):
        self.practitioner = None
        
    async def getPractitionerById(self,id):
        practitioner = await client.reference('Practitioner',id).to_resource()
        self.practitioner = practitioner
        return self.practitioner.serialize()

    async def createPractitioner(self,first_name,last_name,license_id):
        practitioner = client.resource(
            'Practitioner',
            active = True,
        )
        
        
        practitioner.meta = {
					"profile": [
						"http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/practitioner|1.0.0"
					]
        }
        
        practitioner.name = [
            {
                "use": "official",
                "text": f"Dr. {first_name} {last_name}",
                "family": last_name,
                "given": [
                    first_name
                ]
            }
        ]
        
        practitioner.identifier = [
					{
						"type": {
							"coding": [
								{
									"system": "http://terminology.hl7.org/CodeSystem/v2-0203",
									"code": "MD"
								}
							]
						},
						"system": "http://nphies.sa/license/practitioner-license",
						"value": f"N-P-{license_id}"
					}
        ]
        
        await practitioner.save()
        self.practitioner = practitioner
        return self.practitioner.serialize()