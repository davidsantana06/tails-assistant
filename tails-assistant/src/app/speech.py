from speech_recognition import AudioData, Microphone, Recognizer


SPEECH_LANGUAGE = 'pt-BR'
SPEECH_INPUT_TIMEOUT = 5


def speech_input(recognizer: Recognizer):
    with Microphone() as audio_source:
        recognizer.adjust_for_ambient_noise(audio_source)
        speech = recognizer.listen(audio_source, timeout=SPEECH_INPUT_TIMEOUT)

    return speech


def speech_transcription(speech: AudioData, recognizer: Recognizer):
    return recognizer.recognize_google(speech, language=SPEECH_LANGUAGE)
