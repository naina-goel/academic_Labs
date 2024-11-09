def map_trial_data(raw_trial):
    """Maps raw clinical trial data to the specified JSON schema format."""
    return {
        "trialId": raw_trial.get("NCTId", [None])[0],
        "title": raw_trial.get("Title", [None])[0],
        "startDate": raw_trial.get("StartDate", [None])[0],
        "endDate": raw_trial.get("CompletionDate", [None])[0],
        "phase": raw_trial.get("Phase", [None])[0],
        "principalInvestigator": {
            "name": raw_trial.get("LeadSponsorName", [None])[0],
            "affiliation": None  # No affiliation data in API response
        },
        "locations": [
            {"facility": loc, "city": None, "country": None}
            for loc in raw_trial.get("LocationFacility", [])
        ],
        "eligibilityCriteria": raw_trial.get("EligibilityCriteria", [None])[0]
    }