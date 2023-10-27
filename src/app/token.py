from nltk import word_tokenize
from nltk.corpus import stopwords
from speech_recognition import AudioData


CORPUS_LANGUAGE = 'portuguese'


def retrieve_stop_words():
    return stopwords.words(CORPUS_LANGUAGE)


def transcription_tokenize(transcription: AudioData, stop_words: list[str]):
    return [
        token
        for token in word_tokenize(transcription)
        if token not in stop_words
    ]
