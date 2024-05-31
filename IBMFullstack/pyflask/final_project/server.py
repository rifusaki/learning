''' Executing this function initiates the application of emotion
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion detector app thingy")

@app.route("/emotionDetector")
def sent_analyzer():
    '''Simple emotion detector using Watson NLP'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again."
    return (f"For the given statement, the system response is 'anger': {response['anger']},"
    f"'disgust': {response['disgust']}," 
    f"'fear': {response['fear']},"
    f"'joy': {response['joy']} and"
    f"'sadness': {response['sadness']}."
    f"The dominant emotion is {dominant_emotion}")

@app.route("/")
def render_index_page():
    '''Index page rendering'''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
