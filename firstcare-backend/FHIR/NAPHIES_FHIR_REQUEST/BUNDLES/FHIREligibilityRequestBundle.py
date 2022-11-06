from django.conf import settings

from FHIR.models import CoverageEligibilityBundle
from Patient.models import Patient
from ..FHIRMessageHeader import FHIRMessageHeader
from ..FHIRCoverageEligibilityRequest import FHIRCoverageEligibilityRequest
from .FHIRRequestBundle import FHIRRequestBundle



class FHIREligibilityRequestBundle(FHIRRequestBundle,FHIRMessageHeader,FHIRCoverageEligibilityRequest):
    def __init__(self):
        pass

    async def CreateEligibilityRequestBundle(self,patient_id,location_id,purpose,start_insurance_date,end_insurance_date):
        bundle = await self.createBundle(patient_id,location_id)        
        await self.createCoverageEligibilityRequest(self.patient.id,self.sender_organization.id,self.payor_organization.id,self.location.id,self.coverage.id,purpose,start_insurance_date,end_insurance_date)
        await self.createMessageHeader(id=self.coverage_eligibility_request.id,payor_organization=self.payor_organization,request_code="eligibility-request")

        bundle.entry = [
            {
                "fullUrl": f"urn:uuid:{self.MessageHeader.id}",
                "resource":self.MessageHeader.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Coverageeligibilityrequest/{self.coverage_eligibility_request.id}",
                "resource":self.coverage_eligibility_request.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Organization/{self.sender_organization.id}",
                "resource":self.sender_organization.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Patient/{self.patient.id}",
                "resource":self.patient.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Location/{self.location.id}",
                "resource":self.location.serialize()
            }
        ]
        
        if 'Discovery' in purpose:
            pass
        else:
            bundle.entry.append({
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Coverage/{self.coverage.id}",
                "resource":self.coverage.serialize()
            })
            
        try:
            bundle.entry.append({
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Organization/{self.payor_organization.id}",
                "resource":self.payor_organization.serialize()
            })
        except:
            pass 
        patient = Patient.objects.get(document_id=patient_id)
        eligibility_bundle = CoverageEligibilityBundle(patient=patient,request_bundle_id=bundle.id,request_bundle=bundle,eligibility_request_id=self.coverage_eligibility_request.id)
        eligibility_bundle.save()
        await bundle.save()
        
        self.bundle = bundle
        return self.bundle.serialize(),eligibility_bundle