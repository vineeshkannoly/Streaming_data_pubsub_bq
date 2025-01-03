from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
PROJECT_ID = (os.getenv('PROJECT_ID'))
BUCKET_ID = (os.getenv('BUCKET_NAME'))
DATASET_ID =(os.getenv('DATASET_ID'))
REGION =(os.getenv('region'))
API_URL =(os.getenv('API_URL'))
API_KEY =(os.getenv('x-rapidapi-key'))
API_HOST =(os.getenv('x-rapidapi-host'))
