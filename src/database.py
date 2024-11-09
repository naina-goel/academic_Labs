# src/database.py
from pymongo import MongoClient
from src.config import config

class Database:
    _instance = None

    @staticmethod
    def get_instance():
        if Database._instance is None:
            Database()
        return Database._instance

    def __init__(self):
        if Database._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.client = MongoClient(config.MONGO_URI)
            self.db = self.client[config.DATABASE_NAME]
            Database._instance = self

    def insert_trials(self, data):
        collection = self.db[config.COLLECTION_NAME]
        if data:
            collection.insert_many(data)

    def update_trial_with_diseases(self, trial_id, diseases):
        collection = self.db[config.COLLECTION_NAME]
        collection.update_one(
            {"trialId": trial_id},
            {"$set": {"extractedDiseases": diseases}}
        )

db = Database.get_instance()