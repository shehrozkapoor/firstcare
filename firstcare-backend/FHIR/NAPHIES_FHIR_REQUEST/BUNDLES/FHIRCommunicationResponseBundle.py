from django.conf import settings
from .FHIRRequestBundle import FHIRRequestBundle
from ..FHIRMessageHeader import FHIRMessageHeader
from ..FHIRCommunication import FHIRCommunication

import asyncio


class FHIRCommunicationResponseBundle(FHIRRequestBundle,FHIRMessageHeader,FHIRCommunication):
    def __init__(self):
        pass
    
    async def createCommunicationResponseBundle(self,patient_id,communication_request_id,claim_id,payload):
        bundle = await self.createBundle(patient_id=patient_id)
        await self.createCommunication(request_id=communication_request_id,patient_id=patient_id,claim_id=claim_id,payor_org_id=self.payor_organization.id,payload=payload)
        await self.createMessageHeader(id=self.communication.id,payor_organization=self.payor_organization,request_code="communication")
        
        bundle.entry=[
            {
                "fullUrl": f"urn:uuid:{self.MessageHeader.id}",
                "resource":self.MessageHeader.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}Communication/{self.communication.id}",
                "resource":self.communication.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Patient/{self.patient.id}",
                "resource":self.patient.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Organization/{self.sender_organization.id}",
                "resource":self.sender_organization.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Organization/{self.payor_organization.id}",
                "resource":self.payor_organization.serialize()
            },
        ]
        
        
        await bundle.save()
        self.bundle = bundle
        return self.bundle.serialize()