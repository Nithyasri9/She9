from google import genai

client = genai.Client(api_key="AIzaSyC8_JymLm9dTsbDh0Fx2VwVyL-CT2etQhM")

prompt = """
You are a professional dietitian. Create a 30-day diet plan for a 4-month pregnant woman (second trimester).

Each day should include the following:
- Breakfast
- Lunch
- Snack
- Dinner
- Hydration Tip

Guidelines:
- Focus on nutrients essential for second trimester: folate, iron, calcium, protein, omega-3s, and fiber.
- Include both vegetarian and non-vegetarian Indian options (a few international dishes are okay).
- Avoid caffeine, alcohol, and high-mercury fish.
- Avoid repeating meals.
- Keep the format clean and structured like this:

Day 1:
  Breakfast: ...
  Lunch: ...
  Snack: ...
  Dinner: ...
  Hydration Tip: ...

Continue this structure for all 30 days.
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
)

print(response.text)