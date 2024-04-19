### ========== Library ========== ###
from pymongo.mongo_client import MongoClient
from config import secret

### ========== Create new client and connect to the server ========== ###
client = MongoClient(secret.MONGO_URL)

db = client[secret.DB_NAME]
studentsCollection = db[secret.COLLECTION_NAME]

### ========== Check ping to confirm server work correctly ========== ###
try:
    client.admin.command('ping')
    print(secret.PING_TEST)
except Exception as e:
    print(e)



