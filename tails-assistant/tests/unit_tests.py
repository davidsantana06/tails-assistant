from os import path
from unittest import TestCase as UnitTestCase, TestLoader, TestSuite, TextTestRunner
import sys


ROOT_FOLDER = path.abspath(path.join(path.dirname(__file__), '..'))
TESTS_FOLDER = path.join(ROOT_FOLDER, 'tests')
AUDIO_FOLDER = path.join(TESTS_FOLDER, 'audio')
TEST_AI_NAME = path.join(AUDIO_FOLDER, 'test-ai-name.wav')
TEST_ADD_GAME = path.join(AUDIO_FOLDER, 'test-add-game.wav')
TEST_REMOVE_GAME = path.join(AUDIO_FOLDER, 'test-remove-game.wav')
TEST_SHOW_GAMES = path.join(AUDIO_FOLDER, 'test-show-games.wav')
TEST_RECOMMEND_GAME = path.join(AUDIO_FOLDER, 'test-recommend-game.wav')
TEST_SHOW_POPULAR = path.join(AUDIO_FOLDER, 'test-show-popular.wav')

sys.path.append(ROOT_FOLDER)


from src.app import init_app
from src.app.speech import speech_from_audio_file, speech_transcription
from src.app.command import translate_command
from src.app.token import transcription_tokenize


class TestCase(UnitTestCase):
    def setUp(self):
        self.ai_name, self.ai_actions, self.actuators, self.recognizer, self.stop_words = \
            init_app()
        
    def assert_true_from_command_audio(self, audio_path: str):
        command = self.tokenike_audio(audio_path)
        valid_command = False
        print(f'Comando: {command}')

        try:
            translate_command(command, self.ai_name, self.ai_actions)
            valid_command = True
        except:
            ...

        self.assertTrue(valid_command)
        
    def tokenike_audio(self, audio_path: str):
        speech = speech_from_audio_file(audio_path, self.recognizer)
        transcription = speech_transcription(speech, self.recognizer)
        return transcription_tokenize(transcription, self.stop_words)
        

class TestAiName(TestCase):
    def assert_in_from_name_audio(self, audio_path: str, assert_in: bool = True):
        command = self.tokenike_audio(audio_path)
        ai_name = ''

        if len(command):
            ai_name = command[0]
            print(f'Nome da IA: {ai_name}')

        if assert_in:
            self.assertIn(self.ai_name, ai_name)
        else:
            self.assertNotIn(self.ai_name, ai_name)

    def test_recognize_ai_name(self):
        self.assert_in_from_name_audio(TEST_ADD_GAME)

    def test_not_recognize_ai_name(self):
        self.assert_in_from_name_audio(TEST_AI_NAME, assert_in=False)


class TestArchiveGames(TestCase):
    def test_recommend_game(self):
        self.assert_true_from_command_audio(TEST_RECOMMEND_GAME)

    def test_show_popular(self):
        self.assert_true_from_command_audio(TEST_SHOW_POPULAR)

class TestUserGames(TestCase):
    def test_add_game(self):
        self.assert_true_from_command_audio(TEST_ADD_GAME)

    def test_remove_game(self):
        self.assert_true_from_command_audio(TEST_REMOVE_GAME)

    def test_show_games(self):
        self.assert_true_from_command_audio(TEST_SHOW_GAMES)


if __name__ == '__main__':
    test_loader = TestLoader()
    tests = TestSuite()
    test_cases = [
        TestAiName, TestArchiveGames, TestUserGames
    ]
    test_runner = TextTestRunner()

    for test_case in test_cases:
        tests.addTests(test_loader.loadTestsFromTestCase(test_case))

    test_runner.run(tests)
