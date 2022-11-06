from django.conf import settings
from .constants import client,createUUID

class FHIRLocation:
    def __init__(self):
        self.location = None

    async def getLocation(self,location_id):
        location = await client.reference('Location',location_id).to_resource()
        self.location = location
        return self.location.serialize()
    
    async def createLocation(self,name):
        location = client.resource(
            'Location',
            id = createUUID(),
            name=name,
        )
        location.meta = {
					"profile": [
						settings.FHIR_URL.meta.url+"location|1.0.0",
                ]
        }
        location.identifier = [
                {
                    "system": "http://nphies.sa/license/location-license",
                    "value": "GACH"
                }
            ]
        location.status= "active"
        location.type = [
                {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
                            "code": "GACH"
                        }
                    ]
                }
				]
        location.managingOrganization = {
                "reference": f"Organization/{settings.NPHIES_ORGANIZATION_ID}"
            }
        
        await location.save()
        self.location = location
        return self.location.serialize()