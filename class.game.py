class Game(object):

    letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
    ships_rules = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    field_size = len(letters)

    def __init__(self):

        self.players = []
        self.current_player = None
        self.next_player = None
        self.status = 'prepare'

# просто названия функций входящих в Game
# сами функции с детальным описанием можно найти в полном коде
def start_game(self)
def status_check(self)
def add_player(self, player)
def ships_setup(self, player)
def draw(self)
def switch_players(self)
def clear_screen()