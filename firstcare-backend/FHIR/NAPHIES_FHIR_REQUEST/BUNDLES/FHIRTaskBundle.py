from django.conf import settings
from .FHIRRequestBundle import FHIRRequestBundle
from ..FHIRMessageHeader import FHIRMessageHeader
from ..FHIRTask import FHIRTask

class FHIRTaskBundle(FHIRRequestBundle,FHIRMessageHeader):
    def __init__(self):
        pass

    async def createFHIRTaskBundle(self,request_type=None,patient_id=None,status=None,intent=None,priority=None,focus_resource_type=None,focus_resource_type_id=None,task_reason_code=None,task_code=None):
        bundle = await self.createBundle(patient_id=patient_id)
        
        task_obj = FHIRTask()
        await task_obj.createTask(status=status,intent=intent,priority=priority,focus_resource_type=focus_resource_type,focus_resource_type_id=focus_resource_type_id,payor_org=self.payor_organization.id,task_reason_code=task_reason_code,task_code=task_code)
        
        await self.createMessageHeader(id=task_obj.task.id,payor_organization=self.payor_organization,request_code=request_type)
        
        bundle.entry = [
            {
                "fullUrl": f"urn:uuid:{self.MessageHeader.id}",
                "resource":self.MessageHeader.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Task/{task_obj.task.id}",
                "resource":task_obj.task.serialize()
            },
            {
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Organization/{self.sender_organization.id}",
                "resource":self.sender_organization.serialize()
            },
            
        ]
        if self.MessageHeader.eventCoding.code != 'poll-request':
            bundle.entry.append({
                "fullUrl": f"{settings.NPHIES_FULL_URL}/Organization/{self.payor_organization.id}",
                "resource":self.payor_organization.serialize()
            })
        await bundle.save()
        self.bundle = bundle
        return self.bundle.serialize()

        
        