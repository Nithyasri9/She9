from google import genai

# Initialize Gemini Client
client = genai.Client(api_key="AIzaSyC8_JymLm9dTsbDh0Fx2VwVyL-CT2etQhM")

# Define prompt for 30-day medication/supplement plan
prompt = """
You are a licensed obstetrician. Create a 30-day medication and supplement plan for a healthy 4-month pregnant woman (second trimester).

Each day should include:
- Morning Medication
- Afternoon Medication
- Evening Medication
- Supplement Notes
- Caution Note (if any)

Guidelines:
- Include essential supplements like iron, folic acid, calcium, vitamin D, and DHA.
- Avoid medications unsafe in pregnancy (e.g., NSAIDs, retinoids, high-dose vitamin A, etc.).
- Focus on general health, fetal development, and preventing common issues like anemia or bone loss.
- Format cleanly and clearly like this:

Day 1:
  Morning Medication: ...
  Afternoon Medication: ...
  Evening Medication: ...
  Supplement Notes: ...
  Caution Note: ...

Continue this structure for all 30 days.
"""

# Generate content using Gemini
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
)

# Output the response
print(response.text)