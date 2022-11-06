import asyncio
from .constants import client





class FHIRPatient:
    def __init__(self):
        self.patient = None

    async def getPatient(self,National_id):
        patient = await client.reference('Patient',National_id).to_resource()

        self.patient = patient
        return self.patient.serialize()


    async def createPatient(self,data):
        try:
            decease_datetime = data.deceasedDateTime.strftime('%Y-%m-%d %H:%M:%S')
        except:
            decease_datetime=""
        patient = client.resource('Patient',
            id=data.document_id,
            gender=data.gender,
            active=True,
            deceasedBoolean= data.deceasedBoolean,
            deceasedDateTime=decease_datetime,
            birthDate=data.DOB.strftime('%Y-%m-%d')
        )

        patient.name = [{
            'use':'official',
            'text': f"{data.first_name} {data.second_name} {data.third_name}",
            'given':[data.first_name,data.second_name],
            'family': data.third_name,
            'prefix':[data.first_name],
            'suffix':[data.second_name]
        }]


        patient.telecom = [{
            'system':'phone',
            'value':data.contact_info.phone_number,
            'rank' : 1
        }]

        #address
        # patient.address = [
        #     {
        #         'use':'home',
        #         'text':data.contact_info.permanent_address,
        #         'city':data.contact_info.city,
        #         'country':data.contact_info.country,
        #         'district':data.contact_info.area,
        #         'postalCode':data.contact_info.zip_code
        #     }
        # ]

        # contact
        if data.contact_info.emergency_contact_number is not None:
            patient.contact=[
                {
                    # 'relationship':[{
                    #     'text':data.contact_info.emergency_contact_relationship
                    # }],
                    # 'name':{
                    #     'use':'official',
                    #     'text' : data.contact_info.emergency_contact_name
                    # },
                    'telecom':[{
                        'system':'phone',
                        'value':data.contact_info.emergency_contact_number,
                        'rank':2
                    }],
                    # 'gender':data.contact_info.emergency_contact_gender
                }
            ]
        await patient.save()
        self.patient=patient
        return self.patient.serialize()