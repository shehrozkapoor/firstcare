from .constants import client,createUUID
from .FHIRCoverage import FHIRCoverage
from django.conf import settings
import datetime
from ..models import Claim

class FHIRClaim:
    def __init__(self):
        self.claim = None

    async def getClaim(self,claim_id):
        claim_resources = await client.reference('Claim',claim_id).to_resource()
        self.claim=claim_resources
        return self.claim.serialize()
    
    async def sendClaim(self,patient_id=None,claim_type=None,sub_type=None,processPriority="normal",extensions=None,product_services=None,service_date=None,quantity_val=1,unit_price=0,net_price=0,supportingInfos=None,diagnosis=None,careTeams=None):
        coverage = FHIRCoverage()
        coverage = await coverage.getCoverageByPatientId(patient_id)
        
        
        claim = client.resource(
            'Claim',
            id=createUUID(),
            status="active",
            use = "preauthorization",
            created=str(datetime.datetime.now().isoformat()),
        )
        
        claim.meta = {
            "profile": [
                f"http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/{claim_type}-priorauth|1.0.0"
            ]
        }
        
        if extensions is not None:
            claim.extension = [extension for extension in extensions]
        
        claim.type = {
                "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/claim-type",
                    "code": claim_type
                }
            ]
        }
        
        claim.subType = {
            "coding": [
                {
                    "system": "http://nphies.sa/terminology/CodeSystem/claim-subtype",
                    "code": sub_type
                }
            ]
        }
        
        claim.patient = {
            "reference": f"{settings.NPHIES_FULL_URL}Patient/{patient_id}"
        }
        claim.insurer = {
            "reference": f"{settings.NPHIES_FULL_URL}Organization/{coverage['payor'][0]['reference'].split('Organization/')[1]}"
        }
        
        claim.provider = {
            "reference": f"{settings.NPHIES_FULL_URL}Organization/{settings.NPHIES_ORGANIZATION_ID}"
        }
        
        claim.priority = {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/processpriority",
                    "code": processPriority
                }
            ]
        }
        claim.payee =  {
            "type": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/payeetype",
                        "code": "provider"
                    }
                ]
            }
        }
        
        claim.careTeam = [careTeam for careTeam in careTeams]
        claim.supportingInfo = supportingInfos
        claim.diagnosis =  [diagnose for diagnose in diagnosis]
        
        claim.insurance = [
            {
                "sequence": 1,
                "focal": True,
                "coverage": {
                    "reference": f"{settings.NPHIES_FULL_URL}Coverage/{coverage['id']}"
                }
            }
        ]

        
        claim.item = [
            {
            "sequence": 1,
            "careTeamSequence": [sequence for sequence in range(1,len(claim.careTeam)+1)],
            "diagnosisSequence": [sequence for sequence in range(1,len(claim.diagnosis)+1)],
            "productOrService" : {
                "coding": [product for product in product_services]
                },
            "servicedDate": service_date,
            "quantity": {
                "value": quantity_val
            },
            "unitPrice": {
                "value": unit_price,
                "currency": "SAR"
            },
            "net": {
                "value": net_price,
                "currency": "SAR"
            },
            "total": {
                "value": net_price,
                "currency": "SAR"
            }
        }]
        if extensions is not None:
            claim.item[0]['extensions'] = [extension for extension in extensions]
            
        await claim.save()
        self.claim = claim
        return claim.serialize()
    
    async def sendClaimManual(self,claim_obj,use,claim_type,sub_type,processPriority,careTeams,supportingInfos,diagnosis,items):
        coverage = FHIRCoverage()
        coverage = await coverage.getCoverageByPatientId(claim_obj.patient.document_id)
        
        
        claim = client.resource(
            'Claim',
            id=createUUID(),
            status="active",
            use = use,
            created=str(datetime.datetime.now().isoformat()),
        )
        
        claim.meta = {
            "profile": [
                f"http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/{claim_type}-priorauth|1.0.0"
            ]
        }
        
        claim.extension = [
					{
						"url": "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/extension-eligibility-offline-reference",
						"valueString": f"EligResp-{claim_obj.coverage_eligibility_request.response_bundle['entry'][1]['resource']['id']}"
					},
					{
						"url": "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/extension-eligibility-offline-date",
						"valueDateTime": f"{claim_obj.coverage_eligibility_request.response_bundle['entry'][1]['resource']['created']}"
					}
        ]
        
        claim.type = {
                "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/claim-type",
                    "code": claim_type
                }
            ]
        }
        
        claim.subType = {
            "coding": [
                {
                    "system": "http://nphies.sa/terminology/CodeSystem/claim-subtype",
                    "code": sub_type
                }
            ]
        }
        
        claim.patient = {
            "reference": f"{settings.NPHIES_FULL_URL}Patient/{claim_obj.patient.document_id}"
        }
        claim.insurer = {
            "reference": f"{settings.NPHIES_FULL_URL}Organization/{coverage['payor'][0]['reference'].split('Organization/')[1]}"
        }
        
        claim.provider = {
            "reference": f"{settings.NPHIES_FULL_URL}Organization/{settings.NPHIES_ORGANIZATION_ID}"
        }
        
        claim.priority = {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/processpriority",
                    "code": processPriority
                }
            ]
        }
        claim.payee =  {
            "type": {
                "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/payeetype",
                        "code": "provider"
                    }
                ]
            }
        }
        
        claim.careTeam = careTeams
        claim.supportingInfo = supportingInfos
        claim.diagnosis =  diagnosis
        
        claim.insurance = [
            {
                "sequence": 1,
                "focal": True,
                "coverage": {
                    "reference": f"{settings.NPHIES_FULL_URL}Coverage/{coverage['id']}"
                }
            }
        ]

        
        claim.item = items
            
        await claim.save()
        self.claim = claim
        return claim.serialize()
        

    async def updateClaimStatus(self,claim_id,status):
        get_claim = await self.getClaim(claim_id=claim_id)
        self.claim.status='active'
        await self.claim.save(fields=['status'])
        return self.claim.serialize()
    
    async def updateClaimIdentifier(self,claim_id,status,auth_req_id):
        get_claim = await self.getClaim(claim_id=claim_id)
        self.claim.identifier = [
            {
                "system": f"{settings.NPHIES_FULL_URL}authorization",
                "value": f"req_{auth_req_id}"
            }
        ]
        await self.claim.save(fields=['identifier'])
        return self.claim.serialize()