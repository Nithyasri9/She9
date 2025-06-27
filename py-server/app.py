from flask import Flask, request, jsonify
from flask_cors import CORS
from services import gemini as gemini_services

app = Flask(__name__)
CORS(app)

@app.route('/api/nutrition', methods=['POST'])
def nutrition():
    data = request.json
    return jsonify({"response": gemini_services.generate_nutrition_plan(data)})

@app.route('/api/activity', methods=['POST'])
def activity():
    data = request.json
    return jsonify({"response": gemini_services.generate_activity_plan(data)})

@app.route('/api/medication', methods=['POST'])
def medication():
    data = request.json
    return jsonify({"response": gemini_services.generate_medication_plan(data)})

@app.route('/api/mood-tracker', methods=['POST'])
def mood_tracker():
    data = request.json
    return jsonify({"response": gemini_services.generate_mood_tracker(data)})

if __name__ == '__main__':
    app.run(debug=True)
