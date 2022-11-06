from django.conf import settings
from .constants import client,createUUID


class FHIRMessageHeader:
    def _init__(self):
        self.MessageHeader = None

    async def createMessageHeader(self,id=createUUID(),payor_organization=None,request_code=None):
        messageHeader = client.resource(
            'MessageHeader',
        )
        messageHeader.id = id
        messageHeader.meta = {
            "profile": [
                settings.FHIR_URL.meta.url+"message-header|1.0.0"
            ]
        }

        messageHeader.eventCoding = {
            "system": "http://nphies.sa/terminology/CodeSystem/ksa-message-events",
            "code": request_code
        }

        messageHeader.destination= [
            {
                "endpoint": f"{payor_organization.identifier[0]['system']}/{payor_organization.identifier[0]['value']}",
                "receiver": {
                    "type": "Organization",
                    "identifier": payor_organization.identifier
                }
            }
        ]

        messageHeader.sender= {
                "type": "Organization",
                "identifier": {
                    "system": settings.NPHIES_SYSTEM,
                    "value": settings.NPHIES_VALUE
                }
        }
        messageHeader.source = {"endpoint": settings.NPHIES_ENDPOINT}
        if request_code == 'priorauth-request':
            messageHeader.focus=[
            {   
                # NPHIES IMPLMENTATION
                # "reference": f"{settings.NPHIES_FULL_URL}Claim/{id}"
                #HAPI IMPLEMENTATION
                "reference": f"Claim/{id}"
            }
            ]
        elif request_code == 'eligibility-request':
            messageHeader.focus=[
                {   
                    # NPHIES IMPLMENTATION
                    # "reference": f"{settings.NPHIES_FULL_URL}Coverageeligibilityrequest/{coverageEligibilitId}"
                    #HAPI IMPLEMENTATION
                    "reference": f"CoverageEligibilityRequest/{id}"
                }
                ]
        elif request_code == 'communication':
            messageHeader.focus=[
                {   
                    # NPHIES IMPLMENTATION
                    # "reference": f"{settings.NPHIES_FULL_URL}Coverageeligibilityrequest/{coverageEligibilitId}"
                    #HAPI IMPLEMENTATION
                    "reference": f"Communication/{id}"
                }
                ]
        elif request_code == 'batch-request':
            messageHeader.focus=[{   
                    # NPHIES IMPLMENTATION
                    # "reference": f"{settings.NPHIES_FULL_URL}Coverageeligibilityrequest/{coverageEligibilitId}"
                    #HAPI IMPLEMENTATION
                    "reference": f"Bundle/{i['id']}"
                }for i in id]
        await messageHeader.save()
        self.MessageHeader = messageHeader
        return self.MessageHeader.serialize()