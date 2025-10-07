from flask import Flask, request, jsonify
import logging
from emotion_detection import emotion_detector

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)  # Enable debug logging

@app.route('/', methods=['GET'])
def home():
    return "Emotion Detection API is running."

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    try:
        data = request.get_json()
        logging.debug(f"Received data: {data}")

        text = data.get('text', '')
        if not text:
            logging.warning("No text provided in request")
            return jsonify({'error': 'No text provided'}), 400

        result = emotion_detector(text)
        if result is None:
            logging.error("Emotion detection failed")
            return jsonify({'error': 'Emotion detection failed'}), 500

        logging.debug(f"Returning result: {result}")
        return jsonify(result)

    except Exception as e:
        logging.error(f"Exception in detect_emotion: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)