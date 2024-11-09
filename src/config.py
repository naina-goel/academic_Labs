# src/config.py
import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    DATABASE_NAME = "clinical_trials_db"
    COLLECTION_NAME = "clinical_trials"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")
    API_URL = "https://clinicaltrials.gov/api/query/study_fields"
    API_PARAMS = {
        "expr": "LASTUPDATE_DATE:[2024-10-20+TO+2024-10-21]",
        "fields": "NCTId,Title,Phase,StartDate,CompletionDate,LeadSponsorName,LocationFacility,EligibilityCriteria",
        "min_rnk": 1,
        "fmt": "json"
    }

config = Config()