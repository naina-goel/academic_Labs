import requests
from src.config import config

def fetch_clinical_trials():
    """Fetches clinical trials data from the configured API endpoint."""
    response = requests.get(config.API_URL, params=config.API_PARAMS)
    response.raise_for_status()  # Raises HTTPError if response code is 4xx/5xx
    return response.json().get("StudyFieldsResponse", {}).get("StudyFields", [])