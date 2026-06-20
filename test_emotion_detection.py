import EmotionDetection.emotion_detection
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Caso de prueba para sentimiento positivo 
        result_1 = EmotionDetection.emotion_detection.emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy') 

        result_2 = EmotionDetection.emotion_detection.emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger') 

        result_3 = EmotionDetection.emotion_detection.emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust') 

        result_4 = EmotionDetection.emotion_detection.emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness') 

        result_5 = EmotionDetection.emotion_detection.emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()