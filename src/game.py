from character import GenericCharacter
from board import Board

class Game:
    """
    Manages the overall game state, turns, and player actions for the tactical hex-based skirmish game.
    """
    def __init__(self, board_width=7, board_height=7):
        """
        Initialize the game with a board and two players.
        :param board_width: Width of the board (q axis)
        :param board_height: Height of the board (r axis)
        """
        self.board = Board(board_width, board_height)
        self.players = {1: [], 2: []}  # player_id: list of GenericCharacter
        self.current_player = 1
        self.turn_number = 1

    def add_character(self, player_id, character, position):
        """
        Add a character for a player at a given position.
        :param player_id: 1 or 2
        :param character: GenericCharacter instance
        :param position: (q, r) tuple
        """
        self.players[player_id].append(character)
        self.board.place_character(character, position)

    def move_character(self, character, destination):
        """
        Move a character to a new position on the board.
        :param character: GenericCharacter instance
        :param destination: (q, r) tuple
        """
        # Find current position
        for pos, c in self.board.grid.items():
            if c == character:
                self.board.move_character(pos, destination)
                break

    def attack_character(self, attacker, target):
        """
        Perform an attack from one character to another.
        :param attacker: GenericCharacter instance
        :param target: GenericCharacter instance
        """
        attacker.attack(target)

    def end_turn(self):
        """
        End the current player's turn and switch to the other player.
        """
        self.current_player = 2 if self.current_player == 1 else 1
        self.turn_number += 1

    def is_game_over(self):
        """
        Check if the game is over (stub for now).
        :return: True if game is over, False otherwise
        """
        return False 