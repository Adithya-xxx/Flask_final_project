import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    format_response = json.loads(response.text)
    if response.status_code == 200:
        anger = format_response['emotionPredictions'][0]['emotion']['anger']
        disgust = format_response['emotionPredictions'][0]['emotion']['disgust']
        fear = format_response['emotionPredictions'][0]['emotion']['fear']
        joy = format_response['emotionPredictions'][0]['emotion']['joy']
        sadness = format_response['emotionPredictions'][0]['emotion']['sadness']
        check = max(anger,disgust,fear,joy,sadness)
        if check == anger:
            dominant_emotion = 'anger'
        elif check == disgust:
            dominant_emotion = 'disgust'
        elif check == fear:
            dominant_emotion = 'fear'
        elif check == joy:
            dominant_emotion = 'joy'
        elif check == sadness:
            dominant_emotion = 'sadness'
    elif response.status_code == 500:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
    
    return {'anger': anger, 'disgust': disgust, 'fear': fear,'joy':joy, 'sadness':sadness, 'dominant_emotion':dominant_emotion}
    
