class Board:
    """
    Represents the hex grid board for the tactical skirmish game.
    Uses axial coordinates for hexes.
    """
    def __init__(self, width, height):
        """
        Initialize the board with given width and height (in hexes).
        :param width: Number of columns (q axis)
        :param height: Number of rows (r axis)
        """
        self.width = width
        self.height = height
        self.grid = {}  # {(q, r): character}

    def place_character(self, character, position):
        """
        Place a character at a given hex position.
        :param character: GenericCharacter instance
        :param position: (q, r) tuple
        """
        self.grid[position] = character

    def move_character(self, from_pos, to_pos):
        """
        Move a character from one hex to another.
        :param from_pos: (q, r) tuple
        :param to_pos: (q, r) tuple
        """
        character = self.grid.pop(from_pos, None)
        if character:
            self.grid[to_pos] = character

    def remove_character(self, position):
        """
        Remove a character from a hex.
        :param position: (q, r) tuple
        """
        if position in self.grid:
            del self.grid[position]

    def is_occupied(self, position):
        """
        Check if a hex is occupied by a character.
        :param position: (q, r) tuple
        :return: True if occupied, False otherwise
        """
        return position in self.grid

    def get_character(self, position):
        """
        Get the character at a given hex, or None if empty.
        :param position: (q, r) tuple
        :return: GenericCharacter or None
        """
        return self.grid.get(position) 