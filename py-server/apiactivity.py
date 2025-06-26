from google import genai

# Initialize Gemini Client
client = genai.Client(api_key="AIzaSyC8_JymLm9dTsbDh0Fx2VwVyL-CT2etQhM")

# Prompt for 30-day activity plan
prompt = """
You are a prenatal wellness expert. Create a 30-day activity plan for a healthy 4-month pregnant woman (second trimester).

Each day should include:
- Light Physical Activity
- Mental Wellness Activity
- Self-Care Suggestion
- Tip for the Day

Guidelines:
- Activities must be safe for pregnancy (e.g., walking, prenatal yoga, light stretching).
- Mental wellness ideas can include journaling, affirmations, reading, or meditation.
- Self-care suggestions should help reduce stress and improve well-being.
- Tips must be helpful, supportive, and aligned with second trimester needs.
- Do not repeat the same activity too often.
- Keep the structure clean and consistent, like this:

Day 1:
  Light Physical Activity: ...
  Mental Wellness Activity: ...
  Self-Care Suggestion: ...
  Tip for the Day: ...

Continue this format for all 30 days.
"""

# Generate the content from Gemini
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
)

# Print the generated 30-day activity plan
print(response.text)