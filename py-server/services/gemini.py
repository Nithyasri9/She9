from google import genai

client = genai.Client(api_key="AIzaSyC8_JymLm9dTsbDh0Fx2VwVyL-CT2etQhM")

def generate_nutrition_plan(mother_data):
    prompt = f"""
You are a professional dietitian. Create a 30-day diet plan for a 4-month pregnant woman (second trimester).

Mother's Info:
- Name: {mother_data.get("name")}
- Age: {mother_data.get("age")}
- Height: {mother_data.get("height")} cm
- Weight: {mother_data.get("weight")} kg
- Living Conditions: {mother_data.get("living_conditions")}
- Working Conditions: {mother_data.get("working_conditions")}
- Medical History: {mother_data.get("medical_history")}

Each day should include:
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
    return response.text.strip()


def generate_activity_plan(mother_data):
    prompt = f"""
You are a prenatal wellness expert. Create a 30-day activity plan for a healthy 4-month pregnant woman (second trimester).

Mother's Info:
- Name: {mother_data.get("name")}
- Age: {mother_data.get("age")}
- Height: {mother_data.get("height")} cm
- Weight: {mother_data.get("weight")} kg
- Living Conditions: {mother_data.get("living_conditions")}
- Working Conditions: {mother_data.get("working_conditions")}
- Medical History: {mother_data.get("medical_history")}

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
- Avoid repeating the same activity too often.
- Keep the structure clean and consistent, like this:

Day 1:
  Light Physical Activity: ...
  Mental Wellness Activity: ...
  Self-Care Suggestion: ...
  Tip for the Day: ...

Continue this format for all 30 days.
"""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text.strip()


def generate_medication_plan(mother_data):
    prompt = f"""
You are a licensed obstetrician. Create a 30-day medication and supplement plan for a healthy 4-month pregnant woman (second trimester).

Mother's Info:
- Name: {mother_data.get("name")}
- Age: {mother_data.get("age")}
- Height: {mother_data.get("height")} cm
- Weight: {mother_data.get("weight")} kg
- Living Conditions: {mother_data.get("living_conditions")}
- Working Conditions: {mother_data.get("working_conditions")}
- Medical History: {mother_data.get("medical_history")}

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
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text.strip()


def generate_mood_tracker(mother_data):
    prompt = f"""
You are a maternal mental health expert. Create a 30-day mood swings tracker for a 4-month pregnant woman (second trimester).

Mother's Info:
- Name: {mother_data.get("name")}
- Age: {mother_data.get("age")}
- Height: {mother_data.get("height")} cm
- Weight: {mother_data.get("weight")} kg
- Living Conditions: {mother_data.get("living_conditions")}
- Working Conditions: {mother_data.get("working_conditions")}
- Medical History: {mother_data.get("medical_history")}

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
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text.strip()
