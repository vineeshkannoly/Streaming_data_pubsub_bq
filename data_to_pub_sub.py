
from google.cloud import storage
from google.cloud import pubsub_v1
import time
import os
from config import GOOGLE_API_KEY ,PROJECT_ID,BUCKET_ID

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_API_KEY
print(GOOGLE_API_KEY)
#Setting up the publisher
publisher = pubsub_v1.PublisherClient()
topic_path = f"projects/{PROJECT_ID}/topics/weather"
topic = publisher.get_topic (request={"topic" :topic_path })
print(topic.name)

#getting the data from bucket
storgae_client = storage.Client()
bucket = storgae_client.bucket(BUCKET_ID)
blob = bucket.blob('weather_data')


#passing the data from the GCS to to PUB_SUB
with blob.open("r") as input :
    for line in input :
        data =line.encode("utf-8")
        future=publisher.publish(topic=topic.name,data=data)
        print(future.result())
        time.sleep(10)





