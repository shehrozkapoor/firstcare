from django.conf import settings
from FHIR.NAPHIES_FHIR_REQUEST.FHIRClaim import FHIRClaim
from .FHIRRequestBundle import FHIRRequestBundle
from ..FHIRMessageHeader import FHIRMessageHeader
from ..constants import FHIR


class FHIRClaimRequestBundle(FHIRRequestBundle,FHIRMessageHeader):
    def __init__(self):
        pass
    
    async def createFHIRClaimRequestBundle(self,claim_type=None,sub_type=None,claim_obj=None):
        
        
        fhir = FHIR()
        careteams = fhir.createCareTeamManual(claim_obj.care_team.all())
        supporting_info = fhir.createSupportingInfoManual(claim_obj.supporting_info.all())
        diagnosis = fhir.createDiagnosisManual(claim_obj.diagnosis_information.all())
        items = fhir.createItemsManual(claim_obj.items.all())
        
        claim = FHIRClaim()
        
        await claim.sendClaimManual(claim_obj=claim_obj,use="claim",claim_type=claim_type,sub_type=sub_type,processPriority='normal',careTeams=careteams,supportingInfos=supporting_info,diagnosis=diagnosis,items=items)
    
        bundle = await self.createBundle(patient_id=claim_obj.patient.document_id,practitioner_id=claim_obj.care_team.all().first().practitioner.fhir_practitioner_id)
        
        await self.createMessageHeader(claim.claim.id,self.payor_organization,"claim-request")
        
        
        bundle.entry = [
            {
                "fullUrl": f"urn:uuid:{self.MessageHeader.id}",
                "resource":self.MessageHeader.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Claim/{claim.claim.id}",
                "resource":claim.claim.serialize()
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
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Organization/{self.payor_organization.id}",
                "resource":self.payor_organization.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Coverage/{self.coverage.id}",
                "resource":self.coverage.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Practitioner/{self.practitioner.id}",
                "resource":self.practitioner.serialize()
            }
        ]
        
        await bundle.save()
        self.bundle = bundle
        return self.bundle.serialize()