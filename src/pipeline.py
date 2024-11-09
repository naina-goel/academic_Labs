from src.data_retrieval import fetch_clinical_trials
from src.data_transformation import map_trial_data
from src.database import db
from src.disease_extraction import extract_diseases_from_text

def run_pipeline():
    # Step 1: Retrieve raw clinical trial data
    raw_trials = fetch_clinical_trials()
    
    # Step 2: Transform raw data into the desired JSON format
    mapped_trials = [map_trial_data(trial) for trial in raw_trials]
    db.insert_trials(mapped_trials)  # Insert transformed data into MongoDB

    # Step 3: Extract diseases using LLM and update records in MongoDB
    for trial in mapped_trials:
        if trial["eligibilityCriteria"]:
            diseases = extract_diseases_from_text(trial["eligibilityCriteria"])
            db.update_trial_with_diseases(trial["trialId"], diseases)

if __name__ == "__main__":
    run_pipeline()