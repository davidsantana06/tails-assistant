from speech_recognition import AudioData, AudioFile, Microphone, Recognizer


SPEECH_LANGUAGE = 'pt-BR'
SPEECH_INPUT_TIMEOUT = 5


def speech_from_audio_file(audio_path: str, recognizer: Recognizer):
    with AudioFile(audio_path) as audio_source:
        return recognizer.recognize_google(
            recognizer.listen(audio_source), language=SPEECH_LANGUAGE
        )


def speech_input(recognizer: Recognizer):
    with Microphone() as audio_source:
        recognizer.adjust_for_ambient_noise(audio_source)
        return recognizer.listen(audio_source, timeout=SPEECH_INPUT_TIMEOUT)


def speech_transcription(speech: AudioData, recognizer: Recognizer):
    return recognizer.recognize_google(speech, language=SPEECH_LANGUAGE)
