import requests
import json

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    try:
        response = requests.post(url, headers=headers, json=input_json)

        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }


        response.raise_for_status() 
        response_json = response.json()

        if 'emotionPredictions' in response_json and \
           isinstance(response_json['emotionPredictions'], list) and \
           len(response_json['emotionPredictions']) > 0 and \
           'emotion' in response_json['emotionPredictions'][0]:

            emotion_scores = response_json['emotionPredictions'][0]['emotion']

            anger_score = emotion_scores.get('anger', 0) 
            disgust_score = emotion_scores.get('disgust', 0)
            fear_score = emotion_scores.get('fear', 0)
            joy_score = emotion_scores.get('joy', 0)
            sadness_score = emotion_scores.get('sadness', 0)
            
            emotions = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            dominant_emotion_name = max(emotions, key=emotions.get)
            output_format = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion_name
            }

            return output_format
        else:
            print("Warning: Unexpected response format from API.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON response from API.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
