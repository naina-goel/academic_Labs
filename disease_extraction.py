def extract_diseases_from_text(criteria_text):
    """Extracts diseases from the inclusion criteria using keyword matching."""
    keywords = ["tuberculosis", "diabetes", "cancer"]  # Extend this list as needed
    diseases = [keyword for keyword in keywords if keyword.lower() in criteria_text.lower()]
    return diseases