import random

from app import init_app
from app.speech import speech_input, speech_transcription
from app.command import execute_command, translate_command
from app.token import transcription_tokenize
from app.utils import (
    print_error, print_primary, print_success, print_warning
)


if __name__ == '__main__':
    app_running = False

    try:
        ai_name, ai_actions, actuators, recognizer, stop_words = init_app()

        print(f'..| {ai_name} AI |..')

        print_primary('Antes de começarmos, gostaria de saber seu nome.', ai_name)
        user_name = input('\n> ')

        print_primary(
            'Pronto, sua sessão acaba de ser iniciada!\n' + \
            'Os dados da sua sessão NÃO serão armazenados em lugar algum.',
            ai_name
        )

        app_running = True
    except:
        print_error('Houve algum erro durante a inicialização da aplicação.', 'Sistema')

    while app_running:
        print_primary(random.choice([
            'Em que posso ajudar?',
            'O que deseja?',
            'Como posso ajudar?',
            'Estou ouvindo...',
            'Estou ouvindo, o que deseja?'
        ]), ai_name, char_by_char=False)

        try:
            speech = speech_input(recognizer)
            transcription = speech_transcription(speech, recognizer)
            print_primary(transcription, user_name)

            tokens = transcription_tokenize(transcription, stop_words)
            item, method = translate_command(tokens, ai_name, ai_actions)
            msg, cat = execute_command(item, method, actuators)
            print_func = globals().get(f'print_{cat}')
            print_func(msg, ai_name)
        except:
            print_warning(random.choice([
                'Não consegui entender o que você disse.',
                'Não entendi o que você disse.',
                'Não consegui entender.',
                'Não entendi.',
                'Não consegui entender o que você disse, pode repetir?'
            ]), ai_name)
