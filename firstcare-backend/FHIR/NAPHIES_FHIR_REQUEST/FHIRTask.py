from .constants import client,createUUID
from .FHIRCoverage import FHIRCoverage
from django.conf import settings
import datetime


class FHIRTask:
    def __init__(self):
        self.task = None
        
        
    async def getTask(self,id):
        task = await client.reference('Task',id).to_resource()
        
        self.task=task
        return self.task.serialize()
    
    async def createTask(self,status=None,intent=None,priority=None,focus_resource_type=None,focus_resource_type_id=None,last_modified=None,payor_org=None,task_reason_code=None,task_code=None):
        task = client.resource(
            'Task',
            id=createUUID(),
            status = status,
            intent = intent,
            priority = priority,
            authoredOn = str(datetime.datetime.now().strftime('%Y-%m-%d')),
            )
        
        task.meta = {
            "profile": [
                "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/task|1.0.0"
            ]
        }
        
        task.code = {
            "coding": [
                {
                    "system": "http://nphies.sa/terminology/CodeSystem/task-code",
                    "code": task_code
                }
            ]
        }
        
        if last_modified is not None:
            task.lastModified = last_modified
            
        task.requester = {
                "reference": f"Organization/{settings.NPHIES_ORGANIZATION_ID}"
        }
        
        if task_code == 'status-check':
            task.identifier = [
            {
                "system": "http://saudidentalclinic.com.sa/task",
                "value": f"Status_{task.id}"
            }
            ]
        if task_code == 'cancel-request':
            task.identifier = [
            {
                "system": "http://saudidentalclinic.com.sa/task",
                "value": f"Cancel_{task.id}"
            }
            ]
        
        if task_code == "poll":
            task.owner = {
            "identifier": {
                    "system": "http://nphies.sa/license/nphies",
                    "value": "NPHIES"
                }
                }
            task.input = [
					{
						"type": {
							"coding": [
								{
									"system": "http://nphies.sa/terminology/CodeSystem/task-input-type",
									"code": "include-message-type"
								}
							]
						},
						"valueCode": "claim-response"
					}
				]
            task.identifier = [
            {
                "system": "http://saudidentalclinic.com.sa/task",
                "value": f"PlReq_{task.id}"
            }
            ]
        else:
            task.owner = {
                    "reference": f"Organization/{payor_org}"
            }
            
            if focus_resource_type is not None and focus_resource_type_id is not None:
                task.focus = {
                        "type": focus_resource_type,
                        "identifier":                     {
                            "system": f"{settings.NPHIES_FULL_URL}{focus_resource_type.lower()}",
                            "value": f"req_{focus_resource_type_id}"
                        }
                }
            if task_reason_code is not None:
                task.reasonCode = {
                        "coding": [
                            {
                                "system": "http://nphies.sa/terminology/CodeSystem/task-reason-code",
                                "code": task_reason_code
                            }
                        ]
                }
        
        await task.save()
        self.task = task
        return self.task.serialize()