from nltk import word_tokenize
from speech_recognition import AudioData


def transcription_tokenize(transcription: AudioData, stopwords: set[str]):
    return [
        token
        for token in word_tokenize(transcription)
        if token not in stopwords
    ]
