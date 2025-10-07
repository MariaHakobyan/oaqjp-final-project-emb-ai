import requests
import logging

logging.basicConfig(level=logging.DEBUG)  # Enable debug logging

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=input_json, headers=headers)
        response.raise_for_status()
        emotion_data = response.json()
        logging.debug(f"API response: {emotion_data}")

        predictions = emotion_data.get('emotionPredictions', [{}])[0]

        # Extract scores with default 0 if missing
        result = {
            'anger': predictions.get('anger', 0),
            'disgust': predictions.get('disgust', 0),
            'fear': predictions.get('fear', 0),
            'joy': predictions.get('joy', 0),
            'sadness': predictions.get('sadness', 0),
        }

        # Find dominant emotion with check for all-zero scores
        if all(score == 0 for score in result.values()):
            result['dominant_emotion'] = None  # or 'neutral'
        else:
            dominant_emotion = max(result, key=result.get)
            result['dominant_emotion'] = dominant_emotion

        logging.debug(f"Extracted emotions: {result}")
        return result

    except requests.exceptions.RequestException as e:
        logging.error(f"RequestException: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None