"""Google Civic Info API."""

import os
import requests 

BASE_URL = "https://www.googleapis.com/civicinfo/v2/"
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

def get_election_info():
    URL = BASE_URL + "elections"

    PARAMS = {'key':GOOGLE_API_KEY} 
    
    response = requests.get(url = URL, params = PARAMS) 
    data = response.json() 

    return data

def get_voter_info(address, electionId):
    URL = BASE_URL + "voterinfo"

    PARAMS = {
        'key': GOOGLE_API_KEY,
        'address': address,
        'electionId': electionId
    } 
    
    response = requests.get(url = URL, params = PARAMS) 
    data = response.json() 

    return data

def get_representative_info(address):
    URL = BASE_URL + "representatives"

    PARAMS = {
        'key': GOOGLE_API_KEY,
        'address': address
    } 
    
    response = requests.get(url = URL, params = PARAMS) 
    data = response.json() 

    return data
