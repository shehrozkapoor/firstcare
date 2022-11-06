import datetime
from django.conf import settings
from .constants import client,createUUID
import asyncio


class FHIRCoverageEligibilityResponse:
    def __init__(self):
        self.coverage_response = None
        
    async def getEligibilityResponse(self,request_id):
        response = await client.reference('CoverageEligibilityResponse',request_id).to_resource()
        self.coverage_response = response
        return self.coverage_response.serialize()
        
    async def createEligibilityResponse(self,patient_id,eligibility_request_id,payor_id,coverage_id):
        coverage_reponse = client.resource(
            'CoverageEligibilityResponse',
            id = createUUID(),
            status="active",
            outcome = "complete",
            created = datetime.datetime.now().date().strftime('%Y-%m-%d'),
            disposition = "Patient’s coverage is subject to the contracted terms and condition",
        )
        
        coverage_reponse.meta = {
            "profile": [
                "http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/eligibility-response|1.0.0"
            ]
        }
        coverage_reponse.identifier= [
					{
						"system": "http://sni.com.sa/fhir/coverageeligibilityresponse",
						"value": f"resp_{coverage_reponse.id}"
					}
        ]
        
        coverage_reponse.purpose = [
					"benefits",
					"validation"
        ]
        
        coverage_reponse.patient = {
					"reference": f"Patient/{patient_id}"
        }
        coverage_reponse.servicedPeriod= {
                "start": datetime.datetime.now().date().strftime('%Y-%m-%d'),
        }
        
        coverage_reponse.request = {
            "identifier": {
                "system": "http://sgh.com.sa/identifier/coverageeligibilityrequest",
                "value": f"req_{eligibility_request_id}"
            }
        }
        
        coverage_reponse.insurer = {
                "reference": f"{settings.NPHIES_FULL_URL}fhir/Organization/{payor_id}"
        }
        
        coverage_reponse.insurance = [
					{
						"coverage": {
							"reference": f"Coverage/{coverage_id}"
						},
						"inforce": True,
						"item": [
							{
								"category": {
									"coding": [
										{
											"system": "http://nphies.sa/terminology/CodeSystem/benefit-category",
											"code": "1"
										}
									]
								},
								"excluded": False,
								"name": "Medical Care",
								"description": "Medical Care.",
								"network": {
									"coding": [
										{
											"system": "http://terminology.hl7.org/CodeSystem/benefit-network",
											"code": "in"
										}
									]
								},
								"unit": {
									"coding": [
										{
											"system": "http://terminology.hl7.org/CodeSystem/benefit-unit",
											"code": "individual"
										}
									]
								},
								"term": {
									"coding": [
										{
											"system": "http://terminology.hl7.org/CodeSystem/benefit-term",
											"code": "annual"
										}
									]
								},
								"benefit": [
									{
										"type": {
											"coding": [
												{
													"system": "http://nphies.sa/terminology/CodeSystem/benefit-type",
													"code": "benefit"
												}
											]
										},
										"allowedMoney": {
											"value": 1000,
											"currency": "SAR"
										}
									}
								]
							},
							{
								"category": {
									"coding": [
										{
											"system": "http://nphies.sa/terminology/CodeSystem/benefit-category",
											"code": "2"
										}
									]
								},
								"excluded": False,
								"name": "Surgical",
								"description": "Surgical.",
								"network": {
									"coding": [
										{
											"system": "http://terminology.hl7.org/CodeSystem/benefit-network",
											"code": "in"
										}
									]
								},
								"unit": {
									"coding": [
										{
											"system": "http://terminology.hl7.org/CodeSystem/benefit-unit",
											"code": "individual"
										}
									]
								},
								"term": {
									"coding": [
										{
											"system": "http://terminology.hl7.org/CodeSystem/benefit-term",
											"code": "annual"
										}
									]
								},
								"benefit": [
									{
										"type": {
											"coding": [
												{
													"system": "http://nphies.sa/terminology/CodeSystem/benefit-type",
													"code": "benefit"
												}
											]
										},
										"allowedMoney": {
											"value": 1050,
											"currency": "SAR"
										}
									}
								]
							}
						]
					}
        ]
        
        await coverage_reponse.save()
        self.coverage_response = coverage_reponse
        
        return self.coverage_response.serialize()