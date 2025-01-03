import apache_beam as beam
from apache_beam.io.gcp.pubsub import ReadFromPubSub
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from apache_beam.options.pipeline_options import  PipelineOptions
import json
from config import GOOGLE_API_KEY ,PROJECT_ID,BUCKET_ID,DATASET_ID,REGION

import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_API_KEY

options =PipelineOptions(runner = 'DirectRunner',
                         project = PROJECT_ID,
                         region =REGION,
                         temp_location ='gs://'+ BUCKET_ID + '/Temp',
                         staging_location ='gs://'+ BUCKET_ID + '/Staging',
                         streaming =True,
                         #service_account_email='first-project@data-load-417316.iam.gserviceaccount.com'
                         )

with beam.Pipeline(options = options) as pipeline:
    weather_data = pipeline | ReadFromPubSub(
        subscription='projects/'+ PROJECT_ID +'/subscriptions/weather')
    
    weather_data_parsed = weather_data | beam.Map(lambda msg : json.loads(msg.decode('utf-8'))) # |beam.Map(print)
                        
    bq_data = weather_data_parsed | beam.Map(lambda data : {
        'city': data.get('city',None),
        'mx_temp' : data.get('mx_temp',None),
        'mn_temp': data.get('mn_temp',None)
    })
    bq_data|beam.Map(print)

    tempschema_1 = {
                   'fields':[
                       {'name':'city', 'type':'STRING'},
                        {'name':'mx_temp','type':'INTEGER'},
                        {'name':'mn_temp','type':'INTEGER'} 
                        ]
                   }
        
    tablename =f"{PROJECT_ID}:{DATASET_ID}.temperature"
    print((tablename))   
         
    """with beam.Pipeline(options = options) as pipeline:
        bq_data =(
        pipeline
        | "Read data" >>     beam.Create([
            {'city': 'New York', 'mx_temp': 85,'mn_temp':65},
            {'city': 'Los Angeles', 'mx_temp': 90}
        ]) """
    bq_data |"writing to Bigquery">> WriteToBigQuery ( table=tablename,
                                                    schema=tempschema_1,                                           
                                                    create_disposition = beam.io.BigQueryDisposition.CREATE_IF_NEEDED, 
                                                    write_disposition = beam.io.BigQueryDisposition.WRITE_APPEND
                                                    )