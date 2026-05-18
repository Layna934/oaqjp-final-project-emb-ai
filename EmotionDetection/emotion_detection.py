import json
import requests

def emotion_detector(text_to_analyze):
    url = ('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(
        url, headers=headers, json=input_json
    )

    formatted_response = json.loads(response.text)

    print(formatted_response)

    anger_score = formatted_response["emotionPredictions"][0]["emotion"].get("anger", 0)
    disgust_score = formatted_response["emotionPredictions"][0]["emotion"].get("disgust", 0)
    fear_score = formatted_response["emotionPredictions"][0]["emotion"].get("fear", 0)
    joy_score = formatted_response["emotionPredictions"][0]["emotion"].get("joy", 0)
    sadness_score = formatted_response["emotionPredictions"][0]["emotion"].get("sadness", 0)

    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }

