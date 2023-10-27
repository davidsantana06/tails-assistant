import json
import random

from .constants import DATABASE_DIR


class Actuator:
    def __init__(self):
        self.item_names = []


class ArchiveGames(Actuator):
    def __init__(self):
        self.item_names = ['jogo', 'populares']
        
        with open(f'{DATABASE_DIR}/games_archive.json', 'r', encoding='utf-8') as games_archive_file:
            games_archives: dict[str, object] = json.load(games_archive_file)
            self.best_games: list[dict[str, object]] = games_archives.get('best_games')
            self.popular_games: list[dict[str, object]] = games_archives.get('popular_games')      

    def recommend_game(self):
        game = random.choice(self.popular_games).get('name')
        msg = random.choice([
            'Recomendo o jogo {}.',
            'O jogo {} é muito bom.',
            'Você deveria jogar {}.',
            'Jogue {}.',
            'O jogo {} é muito divertido.'
        ])
        return (msg.format(game), 'primary')
    
    def show_popular(self, total: int = 10):
        games = ''

        for i, game in enumerate(self.popular_games[0:total], start=1):
            quantity_sold = '{:,}'.format(game.get('quantity_sold'))
            games += f'{i}. {game.get("name")} com {quantity_sold} unidades comercializadas.'

            if i < total:
                games += '\n'

        msg = random.choice([
            'Os jogos mais populares são:\n{}',
            'Os jogos mais jogados são:\n{}'
        ]).format(games)
        return (msg, 'primary')


class UserGames(Actuator):
    def __init__(self):
        self.item_names = ['jogo', 'jogos']
        self.user_games = 0

    def add(self):
        self.user_games += 1
        return ('Jogo adicionado com sucesso!', 'success')

    def remove(self):
        msg, cat = '', ''

        if self.user_games > 0:
            self.user_games -= 1
            msg, cat = 'Jogo removido com sucesso!', 'success'
        else:
            msg, cat = 'Você não possui jogos cadastrados!', 'warning'

        return (msg, cat)

    def show(self):
        msg, cat = '', ''

        if self.user_games > 0:
            msg = random.choice([
                'Que maravilha! Você já tem {} jogos cadastrados.',
                'Incrível! São {} jogos na sua sessão.',
                'Uau! Você possui {} jogos registrados.',
                'Parabéns! Sua sessão contém {} jogos.',
                'Fantástico! {} jogos já estão na sua sessão.'
            ]).format(self.user_games)
            cat = 'primary'
        else:
            msg, cat = 'Você não possui jogos cadastrados.', 'warning'
            
        return (msg, cat)
