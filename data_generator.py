
import os
#import requests
import random
#from time import strftime
from datetime import datetime, timedelta
from google.cloud import storage
import json
from config import  GOOGLE_API_KEY,API_URL,API_KEY,API_HOST,BUCKET_ID

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_API_KEY

print(GOOGLE_API_KEY)
""" Read from API 
querystring = {"q":"London","days":"1"}
HEADERS = {
	"x-rapidapi-key":API_KEY
	"x-rapidapi-host": API_HOST
}

def Weather_stream ():
    response = requests.get(API_URL, headers=headers, params=querystring)
    #print(response.json())
    weather_dir = response.json()
    return weather_dir
    
"""
def generate_time():
    #cur_time = (strftime('%Y-%m-%d %H:%M:%S',time.gmtime()))
    cur_time = datetime.now()
    cur_time = cur_time + timedelta(seconds = random.randint(1,120))
    return (cur_time)
    
def generate_weather () :
 city = ["toronto","london","bangalore","singapore"]
    
 __time = generate_time()
 weather_data ={
         "time" :__time.strftime('%Y-%m-%d %H:%M:%S') ,
        "city": random.choice(city),
         "mx_temp":random.randint(-5,45),
         "mn_temp": random.randint(-5,45)
         
    }
 return (weather_data)
     #time.sleep(10)
weather_list =[]  
for i in range(1,11) :
    weather=generate_weather()
    #print(weather)
    weather_list.append(weather)
    #print(weather_list)

output_json = "weather_data.json"
with open(output_json,"w") as file :
    for w in weather_list :
        json.dump(w,file,separators=(",",":"))
        file.write("\n")
        
"""while weather_flag is True :
    
    weather_dir=Weather_stream ()
    print(weather_dir['location']['name'])
    print(weather_dir['location']['localtime'])
    print(weather_dir['current']['temp_c'])
    time.sleep(60)
    count = count +1
    if count >5 :
        weather_flag =False
"""
client = storage.Client()
bucket = client.bucket(BUCKET_ID)
blob = bucket.blob('weather_data')
blob.upload_from_filename('c:/python/Scripts/Codes/streaming_project/weather_data.json')