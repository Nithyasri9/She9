from google import genai

# Initialize Gemini Client with API key
client = genai.Client(api_key="AIzaSyC8_JymLm9dTsbDh0Fx2VwVyL-CT2etQhM")

# Prompt to generate 30-day mood swings tracker
prompt = """
You are a maternal mental health expert. Create a 30-day mood swings tracker for a 4-month pregnant woman (second trimester).

Each day should include:
- Likely Mood
- Possible Cause
- Coping Strategy
- Daily Affirmation

Guidelines:
- Use a variety of moods like: calm, anxious, happy, irritable, tired, emotional, energetic, etc.
- Causes should relate to hormonal changes, sleep issues, nutrition, body discomfort, or stress.
- Coping strategies should include safe and helpful options (e.g., rest, talking, meditation, breathing, light activity).
- Affirmations should be short, positive, and emotionally supportive.
- Avoid repetition across days.
- Keep the format clean and structured like this:

Day 1:
  Likely Mood: ...
  Possible Cause: ...
  Coping Strategy: ...
  Daily Affirmation: ...

Continue this structure for all 30 days.
"""

# Generate content from Gemini model
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
)

# Print the generated mood tracker
print(response.text)