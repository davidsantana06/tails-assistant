from os import path


DATABASE_DIR = path.abspath(
    path.join(
        path.dirname(__file__),
        '..', '..', 'database'
    )
)