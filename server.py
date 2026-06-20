'''Módulo de servidor Flask para el detector de emociones'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    ''' This function receives text from the frontend, analyzes it
        using the emotion_detector and returns the formatted response.
    '''
    # 1. El frontend de IBM envía los datos por GET usando 'textToAnalyze'
    text_to_analyze = request.args.get('textToAnalyze', '')
    # 2. Ejecutamos tu detector de emociones
    result = emotion_detector(text_to_analyze)
    # 3. Formateamos la respuesta en el texto exacto que la interfaz de IBM espera mostrar
    # Si la respuesta es válida y no es None
    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again."
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)