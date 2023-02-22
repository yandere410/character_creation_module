from graphic_arts.start_game_banner import run_screensaver

def attack(char_name: str, char_class: str) -> str:
    """Choosing your attack."""
    ...


def defence(char_name: str, char_class: str) -> str:
    """Choosing characters nickname."""
    ...


def special(char_name: str, char_class: str) -> str:
    """Choosing class your characters."""
    ...


def start_training(char_name: str, char_class: str) -> str:
    """Start fighting with mobs."""
    ...


def choice_char_class() -> str:
    """Choosing class char."""


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
