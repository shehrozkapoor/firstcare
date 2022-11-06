# from firstcare.celery import app
# @app.task
def checkStatus(json_obj,eligibility_bundle):
    if json_obj['outcome'] == 'complete':
        # if the outcome is complete and inforce is true for every insurance object then it will be eligible for more details see the nphies documentation(SiteEligibility.pdf).
        for obj in json_obj['insurance']:
            if obj['inforce'] == True:
                eligibility_bundle.response_eligibility_status = "eligible"    
            else:
                for extension in obj['extension']:
                    for code in extension['valueCodeableConcept']['coding']:
                        code_system = code['system'].split('CodeSystem/')[1]
                        site_code = code['code']
                        if code_system == 'siteEligibility':
                            print(site_code)
                            eligibility_bundle.response_site_eligibility_status += f"{site_code},"
                        if code_system == 'not-in-force-reason':
                            eligibility_bundle.response_site_eligibility_not_inforce+=f'{site_code},'
                eligibility_bundle.response_eligibility_status = "not-eligible"    
                    
                    
    elif json_obj['outcome'] == 'error':
        eligibility_bundle.response_eligibility_error = True
        for obj in json_obj['error']:
            for sub_obj in obj['valueCodeableConcept']['coding']:
                if sub_obj['code'] == '1658':
                    eligibility_bundle.response_eligibility_error_description+='No member found with the supplied patient credentials,'
                if sub_obj['code'] == '1659':
                    eligibility_bundle.response_eligibility_error_description+='Provider license is not a contracted provider as of the date of service,'
                if sub_obj['code'] == '1660':
                    eligibility_bundle.response_eligibility_error_description+='TPA doesn’t provide adjudication services for this insurer,'
                if sub_obj['code'] == '1665':
                    eligibility_bundle.response_eligibility_error_description+='Newborn exceeds 30 days of age,'
                if sub_obj['code'] == '1666':
                    eligibility_bundle.response_eligibility_error_description+='Provider not licensed during the date of service,'
                if sub_obj['code'] == '1680':
                    eligibility_bundle.response_eligibility_error_description+='Document ID number does not follow the correct structure,'
                if sub_obj['code'] == '1681':
                    eligibility_bundle.response_eligibility_error_description+='Membership number does not follow the correct structure,'
                if sub_obj['code'] == '1682':
                    eligibility_bundle.response_eligibility_error_description+='The patient information does not match the insurance member details,'
    try:
        eligibility_bundle.response_eligibility_description = json_obj['disposition']
    except:
        pass
    eligibility_bundle.save()
    return "done"