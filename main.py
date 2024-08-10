
import google.generativeai as genai
import os

# Fetch API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")  # Use the environment variable name
if not api_key:
    raise ValueError("API key not found in environment variables.")

# Configure the Generative AI client
genai.configure(api_key=api_key)

# Initialize the AI model
model_name = "gemini-1.5-flash"  # Replace with the correct model name if necessary
model = genai.GenerativeModel(model_name=model_name)

# Define a prompt for story generation
prompt = "Once upon a time in a land far, far away, there was a magical forest where... "

# Generate content based on the prompt
response = model.generate_content([prompt])

# Print the response
print("Response from Google Generative AI:")
print(response[0].text)  # Assuming the response is a list of texts
