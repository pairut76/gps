#Pairut Dumkuengthanant
#ID: 64856070


#module for building url and retrieving url json
import json
import urllib.parse
import urllib.request

GOOGLE_API_KEY = 'Fmjtd%7Cluu82168l9%2Cag%3Do5-942l0z'
BASE_URL = 'http://open.mapquestapi.com/directions/v2/route?key='
URL_API_KEY =BASE_URL+GOOGLE_API_KEY

url=None
#create url and returns url
def build_url(locations: [str]) -> str:
    search_parameters=[]
    
    for i in range(len(locations)):
        if search_parameters==[]:
            search_parameters.append(('from', locations[i]))
        else:
            search_parameters.append(('to', locations[i]))

    return URL_API_KEY+'&'+urllib.parse.urlencode(search_parameters)

#accepts url and sends the information retrieve from url out
def get_result(url: str) -> 'json':
    response=None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding='utf-8')
        return json.loads(json_text)
    finally:
        if response != None:
            response.close()

#build url for eleation
def get_elevations(latlong: [int])->int:
    url1='http://open.mapquestapi.com/elevation/v1/profile?key='
    url2='&latLngCollection='
    latlong_str=''
    for i in range((len(latlong))):
        latlong_str+=str(latlong[i])+','
   
    url=url1+GOOGLE_API_KEY+url2+(latlong_str[:-1])
    return url
    





