import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=my_obj, headers=headers)
    # --- INCORPORACIÓN DEL MANEJO DE ERRORES POR STATUS CODE ---
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    try:
        formatted_response = response.json()
        
        # Extraemos el diccionario de emociones navegando por la lista 'emotionPredictions'
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        # Encontramos la emoción con el puntaje más alto (ej: 'joy')
        dominant_emotion = max(emotions, key=emotions.get)
        dominant_score = emotions[dominant_emotion]
        
        # El proyecto de IBM suele pedir este formato específico de salida:
        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
        
    except (ValueError, KeyError, IndexError, TypeError):
        return {
            'anger': None, 'disgust': None, 'fear': None, 
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }