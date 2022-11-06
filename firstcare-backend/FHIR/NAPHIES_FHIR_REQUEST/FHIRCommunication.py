import json
from .constants import client,createUUID
from django.conf import settings
import base64
import datetime
import pathlib


class FHIRCommunication:
    def __init__(self):
        self.communication = None

    async def getCommunicationById(self,id):
        communication =  await client.reference('Communication',id).to_resource()
        self.communication = communication
        return self.communication.serialize()
    
    def createPayload(self,pdf_file,payload_message,title):
        file_extension = pathlib.Path(pdf_file).suffix.replace('.','')
        with open(pdf_file, "rb") as pdf_file:
            encoded_string = str(base64.b64encode(pdf_file.read()))
        payload = [
            {
                "contentString":payload_message
            },
            {
                "contentAttachment":{
                    "contentType": f"application/{file_extension}",
                    "data": encoded_string,
                    "title":title,
                    "creation": str(datetime.datetime.now().strftime('%Y-%m-%d'))
                }
            }
        ]
        return payload
    
    async def createCommunication(self,request_id,patient_id,claim_id,payor_org_id,payload):
        communication =  client.resource(
            'Communication',
            id=createUUID(),
            status = "completed",
            priority ="routine",
        )
        
        communication.meta = {
            "profile": [
                "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/communication|1.0.0"
            ]
        }
        
        communication.identifier = [
            {
                "system": "http://saudicentralpharmacy.sa.com/communication",
                "value": "Communication_20211202982284"
            }
        ]
        
        communication.basedOn = [
            {
                "type": "CommunicationRequest",
                "identifier": {
                    "system": f"{settings.NPHIES_FULL_URL}communicationrequest",
                    "value": f"CommReq_{request_id}"
                }
            }
        ]
        
        communication.category = [
            {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/communication-category",
                        "code": "instruction"
                    }
                ]
            }
        ]
        
        communication.subject =  {
            "reference": f"{settings.NPHIES_FULL_URL}Patient/{patient_id}"
        }
        
        communication.about = [
            {
                "type": "Claim",
                "identifier": {
                    "system": f"{settings.NPHIES_FULL_URL}claim",
                    "value": f"req_{claim_id}"
                }
            }
        ]
        
        communication.recipient = [
            {
                "reference": f"{settings.NPHIES_FULL_URL}Organization/{payor_org_id}"
            }
        ]
        communication.sender = {
            "reference": f"{settings.NPHIES_FULL_URL}Organization/{settings.NPHIES_ORGANIZATION_ID}"
        }
        
        communication.payload = payload
        
        await communication.save()
        self.communication = communication
        return self.communication.serialize()