import json
from django.conf import settings
from FHIR.NAPHIES_FHIR_REQUEST.FHIRClaim import FHIRClaim
from .FHIRRequestBundle import FHIRRequestBundle
from ..FHIRMessageHeader import FHIRMessageHeader
from ..constants import FHIR


class FHIRBatchRequestBundle(FHIRRequestBundle,FHIRMessageHeader):
    def __init__(self):
        pass
    
    async def createFHIRBatchRequestBundle(self,claim_objs):
        fhir = FHIR()
        claim = FHIRClaim()
        bundles_list = []
        for obj in claim_objs:
            careteams = fhir.createCareTeamManual(obj.care_team.all())
            supporting_info = fhir.createSupportingInfoManual(obj.supporting_info.all())
            diagnosis = fhir.createDiagnosisManual(obj.diagnosis_information.all())
            items = fhir.createItemsManual(obj.items.all())
            await claim.sendClaimManual(claim_obj=obj,use="claim",claim_type=obj.claim_type,sub_type=obj.claim_sub_type,processPriority='normal',careTeams=careteams,supportingInfos=supporting_info,diagnosis=diagnosis,items=items)
            bundle = await self.createBundle(patient_id=obj.patient.document_id,practitioner_id=obj.care_team.all().first().practitioner.fhir_practitioner_id)
        
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
            bundles_list.append(bundle.serialize())
            
        main_bundle = await self.createBundle()
        
        await self.createMessageHeader(bundles_list,self.payor_organization,"batch-request")
        main_bundle.entry = [
            {
                "fullUrl": f"urn:uuid:{self.MessageHeader.id}",
                "resource":self.MessageHeader.serialize()
            },
        ]
        print(main_bundle.entry)
        for obj in bundles_list:
            main_bundle.entry.append(obj)
        
        await main_bundle.save()
        
        self.bundle = main_bundle
        return self.bundle.serialize()