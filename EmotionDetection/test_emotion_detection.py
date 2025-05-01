import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_happy(self):
        text = "I am glad this happened"
        result = emotion_detector(text)
        self.assertIsNotNone(result, f"emotion_detector returned None for text: '{text}'")
        self.assertEqual(result['dominant_emotion'], 'joy', 
        f"Expected 'joy' but got '{result.get('dominant_emotion')}' for text: '{text}'")

    def test_angry(self):
        text = "I am really mad about this"
        result = emotion_detector(text)
        self.assertIsNotNone(result, f"emotion_detector returned None for text: '{text}'")
        self.assertEqual(result['dominant_emotion'], 'anger', 
        f"Expected 'anger' but got '{result.get('dominant_emotion')}' for text: '{text}'")

    def test_disgusted(self):
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        self.assertIsNotNone(result, f"emotion_detector returned None for text: '{text}'")
        self.assertEqual(result['dominant_emotion'], 'disgust', 
        f"Expected 'disgust' but got '{result.get('dominant_emotion')}' for text: '{text}'")

    def test_sad(self):
        text = "I am so sad about this"
        result = emotion_detector(text)
        self.assertIsNotNone(result, f"emotion_detector returned None for text: '{text}'")
        self.assertEqual(result['dominant_emotion'], 'sadness', 
        f"Expected 'sadness' but got '{result.get('dominant_emotion')}' for text: '{text}'")

    def test_afraid(self):
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        self.assertIsNotNone(result, f"emotion_detector returned None for text: '{text}'")
        self.assertEqual(result['dominant_emotion'], 'fear', 
        f"Expected 'fear' but got '{result.get('dominant_emotion')}' for text: '{text}'")

if __name__ == '__main__':
    unittest.main()