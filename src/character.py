class GenericCharacter:
    """
    Represents a generic unit in the tactical hex-based skirmish game.
    This class provides the basic interface for movement, attacking, and scoring.
    No stats or specific logic are implemented at this stage.
    """

    def move(self, destination):
        """
        Move the character to a new hex location.
        :param destination: The target hex coordinates (to be defined by the game engine).
        """
        pass

    def attack(self, target):
        """
        Attack another character.
        :param target: The target GenericCharacter instance.
        """
        pass

    def score(self):
        """
        Calculate or update the character's score based on game rules.
        """
        pass 