# Streaming_data_pubsub_bq
Streaming data from API/Own data using PUBSUB to load  Bigquery for further analyis.


# Prerquisties 
1>Google cloud
 a>Storage
 b>PUBSUB
 c>Bigquery
2>python
3>apache beam


# Data Generator.py
This code generates set of sample stream data which is our use case data to load the Bigquery tables.
The code will generate a set of streaming data in json format and load it into GCS bucket.

# Data to PUB_SUB.py
This code will take the above data from GCS and initalizes the PUBSUB topics . There after the data is  published on to PUBSUB topic,  for the underlying subscriptions to consume. 

# PUBSUB to BQ.py
The code will use the Apache beam pipleine to read the PUBSUB subscription , transform the data and load to BQ schema. 

# config.py
Code for storing the GOOGLE connection details,bucket name,project details..


