import asyncio
from .constants import client,createUUID
from django.conf import settings
import datetime

class FHIRPaymentNotice:
    def __init__(self):
        self.payment_notice = None
    
    async def getPaymentNotice(self,id):
        notice = await client.reference('PaymentNotice',id).to_resource()
        self.payment_notice = notice
        return self.payment_notice.serialize()
    

    async def createPaymentNotice(self,payment_reconciliation_id,payment_date,amount,payment_status):
        notice = client.resource(
            'PaymentNotice',
            id=createUUID(),
            status = "active",
            created = str(datetime.datetime.now().strftime('%Y-%m-%d')),
            )
        
        notice.meta = {
            "profile": [
                "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/payment-notice|1.0.0"
            ]
        }
        
        notice.identifier = [
            {
                "system": f"{settings.IDENTIFIER_URL}",
                "value": settings.NPHIES_VALUE
            }
        ]
        
        notice.provider = {
                "reference": f"{settings.NPHIES_FULL_URL}Organization/{settings.NPHIES_ORGANIZATION_ID}"
        }
        
        
        notice.payment = {
            "identifier": {
                "system": "{settings.NPHIES_FULL_URL}paymentreconciliation",
                "value": payment_reconciliation_id
            }
        }
        
        notice.paymentDate = payment_date,
        
        notice.payee = {
            "reference": f"{settings.NPHIES_FULL_URL}Organization/{settings.NPHIES_ORGANIZATION_ID}"
        }
        
        
        notice.recipient = {
            "identifier": {
                "system": "http://nphies.sa/license/nphies",
                "value": "NPHIES"
            }
        }
        
        notice.amount = {
                "value": amount,
                "currency": "SAR"
        }
        
        notice.paymentStatus = {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/paymentstatus",
                    "code": payment_status
                }
            ]
        }
        
        await notice.save()
        self.payment_notice = notice
        return self.payment_notice.serialize()