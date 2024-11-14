# src/disease_extraction.py
import openai
from src.config import config

openai.api_key = config.OPENAI_API_KEY

def extract_diseases_from_text(criteria_text):
    """Uses OpenAI's LLM to extract diseases from eligibility criteria."""
    prompt = (
        "Extract and list the diseases or medical conditions mentioned in the following eligibility criteria:\n\n"
        f"{criteria_text}\n\n"
        "Only list the diseases or conditions as comma-separated values."
    )
    try:
        response = openai.Completion.create(
            model= "gpt-4",  # Use 'gpt-4' if available
            prompt=prompt, 
            max_tokens=100, #limits the length of the generated response
            temperature=0.3 #controls the randomness or creativity of the model's response
        )
        diseases = response.choices[0].text.strip()
        return [disease.strip() for disease in diseases.split(",") if disease]
    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
        return []
