from django.conf import settings
from .FHIRRequestBundle import FHIRRequestBundle
from ..FHIRMessageHeader import FHIRMessageHeader
from ..FHIRPaymentNotice import FHIRPaymentNotice


class FHIRPaymentNoticeBundle(FHIRRequestBundle,FHIRMessageHeader):
    def __init__(self):
        pass
    
    async def createFhirPaymentNotice(self,patient_id,payment_reconciliation_id,payment_date,amount,payment_status):
        bundle = await self.createBundle(patient_id=patient_id)
        
        notice_obj = FHIRPaymentNotice()
        await notice_obj.createPaymentNotice(payment_reconciliation_id=payment_reconciliation_id,payment_date=payment_date,amount=amount,payment_status=payment_status)
        
        await self.createMessageHeader(id=notice_obj.payment_notice.id,payor_organization=self.payor_organization,request_code="payment-notice")

        bundle.entry = [
            {
                "fullUrl": f"urn:uuid:{self.MessageHeader.id}",
                "resource":self.MessageHeader.serialize()
            },            
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/PaymentNotice/{notice_obj.payment_notice.id}",
                "resource":notice_obj.payment_notice.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Organization/{self.sender_organization.id}",
                "resource":self.sender_organization.serialize()
            }
        ]
        
        await bundle.save()
        self.bundle = bundle
        return self.bundle.serialize()