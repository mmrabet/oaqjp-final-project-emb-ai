"""
Flask server for the Emotion Detection application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def render_index_page():
    """
    Renders the index.html page when the root URL is accessed.
    """
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Endpoint to analyze text for emotions using the emotion_detector function.
    Expects a 'textToAnalyze' query parameter.
    Returns a formatted string with emotion scores and the dominant emotion,
    or an error message if input is missing or analysis fails.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(text_to_analyze)
    if emotion_result is None or emotion_result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"
    anger_score = emotion_result.get('anger', 0)
    disgust_score = emotion_result.get('disgust', 0)
    fear_score = emotion_result.get('fear', 0)
    joy_score = emotion_result.get('joy', 0)
    sadness_score = emotion_result.get('sadness', 0)
    dominant_emotion = emotion_result.get('dominant_emotion', 'unknown')
    formatted_output = (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, "
        f"'disgust': {disgust_score}, "
        f"'fear': {fear_score}, "
        f"'joy': {joy_score} and "
        f"'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return formatted_output

if __name__ == '__main__':
    pass
