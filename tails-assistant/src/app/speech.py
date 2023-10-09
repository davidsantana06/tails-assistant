from speech_recognition import AudioData, Microphone, Recognizer


CORPUS_LANGUAGE = 'portuguese'
SPEECH_LANGUAGE = 'pt-BR'
SPEECH_INPUT_TIMEOUT = 5


def speech_input(recognizer: Recognizer):
    speech = None

    with Microphone() as audio_source:
        recognizer.adjust_for_ambient_noise(audio_source)
        print('Fale alguma coisa...')

        try:
            speech = recognizer.listen(
                audio_source, timeout=SPEECH_INPUT_TIMEOUT
            )
        except:
            pass

    return speech


def speech_transcription(speech: AudioData, recognizer: Recognizer):
    transcription = None

    try:
        transcription = recognizer.recognize_google(
            speech, language=SPEECH_LANGUAGE
        )
    except:
        pass

    return transcription


def filter_tokens(tokens: list[str], stopwords: set[str]):
    return [
        token
        for token in tokens
        if token not in stopwords
    ]
