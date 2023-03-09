import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi

ca=certifi.where()

class MongoDBClient:
    client = None
    def __init__(self, datsbase_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = "mongodb+srv://test:971358@cluster0.cblzmsc.mongodb.net/?retryWrites=true&w=majority"
                MongoDBClient.client =pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[datsbase_name]
            self.database_name = datsbase_name

        except Exception as e:
            raise e