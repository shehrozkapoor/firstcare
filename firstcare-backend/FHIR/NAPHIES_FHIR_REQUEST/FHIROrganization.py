from .constants import client,createUUID
from django.conf import settings




class FHIROrganization:
    def __init__(self):
        self.organization = None

    async def getOrganization(self,organization_id):
        organization = await client.reference('Organization', organization_id).to_resource()
        self.organization = organization
        return self.organization.serialize()
    
    async def createOrganization(self,id=createUUID(),name=None,type=None):
        organization = client.resource(
            'Organization',
            id = id,
            active=True,
            name = name
        )
        
        organization.meta = {
					"profile": [
						"http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/provider-organization|1.0.0"
					]
        }
        organization.identifier = [
            {
                "system": settings.NPHIES_SYSTEM,
                "value": settings.NPHIES_PROVIDER_LICENSE_VALUE
            }
        ]
        
        organization.type = [
            {
                "coding": [
                    {
                        "system": "http://nphies.sa/terminology/CodeSystem/organization-type",
                        "code": type
                    }
                ]
            }
        ]
        
        await organization.save()
        
        self.organization = organization
        
        
        return self.organization.serialize()