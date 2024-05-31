import requests
import json

def emotion_detector(text_to_analyse):
   url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   myobj = { "raw_document": { "text": text_to_analyse } }
   header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   response = requests.post(url, json = myobj, headers=header)

   if response.status_code == 200:
        formatted_response = json.loads(response.text)['emotionPredictions'][0]['emotion']
        formatted_response['dominant_emotion'] = max(formatted_response, key=formatted_response.get)
   elif response.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}
   
   return formatted_response

print(emotion_detector(""))

# from emotion_detection import emotion_detector