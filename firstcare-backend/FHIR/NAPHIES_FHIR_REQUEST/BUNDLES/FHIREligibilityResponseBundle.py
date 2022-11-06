from django.conf import settings
from ..constants import client,createUUID
import datetime

from ..FHIRMessageHeader import FHIRMessageHeader
from ..FHIRCoverageEligibilityResponse import FHIRCoverageEligibilityResponse
from .FHIRRequestBundle import FHIRRequestBundle


class FHIREligibilityReponseBundle(FHIRRequestBundle,FHIRMessageHeader,FHIRCoverageEligibilityResponse):
    def __init__(self):
        pass
    
    async def CreateEligibilityResponseBundle(self,patient_id,eligibility_request_id):
        
        
        bundle = await self.createBundle(patient_id)
        
        
        await self.createEligibilityResponse(self.patient.id,eligibility_request_id,self.payor_organization.id,self.coverage.id)
        
        await self.createMessageHeader(self.coverage_response.id,self.payor_organization,"eligibility-response")
        
        bundle.entry = [
            {
                "fullUrl": f"urn:uuid:{self.MessageHeader.id}",
                "resource":self.MessageHeader.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Coverageeligibilityresponse/{self.coverage_response.id}",
                "resource":self.coverage_response.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Coverage/{self.coverage.id}",
                "resource":self.coverage.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Patient/{self.patient.id}",
                "resource":self.patient.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Organization/{self.payor_organization.id}",
                "resource":self.payor_organization.serialize()
            }
        ]
        
        await bundle.save()
        self.bundle = bundle
        return self.bundle.serialize()
