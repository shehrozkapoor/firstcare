import asyncio
from django.conf import settings
from ..constants import client,createUUID
import datetime


from ..FHIRCoverage import FHIRCoverage
from ..FHIRPatient import FHIRPatient
from ..FHIRMessageHeader import FHIRMessageHeader
from ..FHIROrganization import FHIROrganization
from ..FHIRLocation import FHIRLocation
from ..FHIRPractitioner import FHIRPractitioner
from ..FHIRClaim import FHIRClaim

import asyncio


class FHIRRequestBundle(FHIRPatient,FHIRCoverage,FHIRMessageHeader,FHIROrganization,FHIRLocation,FHIRPractitioner,FHIRClaim):
    def __init__(self):
        self.bundle = None
        self.payor_organization= None
        self.sender_organization = None
        
    async def createBundle(self,patient_id=None,location_id=None,practitioner_id=None,claim_id=None):
        bundle_id= createUUID()
        
        if patient_id is not None:
            await self.getPatient(patient_id)
            try:
                await self.getCoverageByPatientId(patient_id)
            except:
                pass
        
        if claim_id is not None:
            await self.getClaim(claim_id)
        
        if location_id is not None:
            await self.getLocation(location_id)
            
        if practitioner_id is not None:
            await self.getPractitionerById(practitioner_id)
        try:
            await self.getOrganization(self.coverage['payor'][0]['reference'].split('Organization/')[1])
            self.payor_organization = self.organization
        except:
            pass
        
        await self.getOrganization(settings.NPHIES_ORGANIZATION_ID)
        self.sender_organization = self.organization
        
        

        bundle = client.resource(
            'Bundle',
            id = bundle_id,
            type="message",
            timestamp = str(datetime.datetime.now().isoformat()),
        )

        bundle.meta= {
		"profile": [
			"http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/bundle|1.0.0"
		    ]
	    }
        
        return bundle