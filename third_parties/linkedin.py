import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    # api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    # header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    api_endpoint = "https://gist.githubusercontent.com/agaveazul/72ac1225ba9a65668cbdb7d5400656d9/raw/737ee54234b57fbec0d6055b729a7e6a3e818b29/richard-strauss.json"
    
    response = requests.get(
        api_endpoint, 
        params={"url": linkedin_profile_url}, 
        # headers=header_dic
    )

    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
            and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    
    return data

