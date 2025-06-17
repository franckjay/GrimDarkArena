from character import GenericCharacter
from game import Game

# Set up the game
WIDTH, HEIGHT = 7, 7

game = Game(WIDTH, HEIGHT)

# Add two characters for each player at starting positions
p1_char1 = GenericCharacter()
p1_char2 = GenericCharacter()
p2_char1 = GenericCharacter()
p2_char2 = GenericCharacter()

game.add_character(1, p1_char1, (0, 0))
game.add_character(1, p1_char2, (0, 1))
game.add_character(2, p2_char1, (6, 6))
game.add_character(2, p2_char2, (6, 5))

# Simple text-based loop for demonstration
while not game.is_game_over():
    print(f"\nTurn {game.turn_number} - Player {game.current_player}'s turn")
    print("Characters on board:")
    for pos, char in game.board.grid.items():
        owner = 1 if char in game.players[1] else 2
        print(f"  Player {owner} character at {pos}")
    print("Commands: move <from_q> <from_r> <to_q> <to_r> | attack <att_q> <att_r> <tgt_q> <tgt_r> | end")
    cmd = input("> ").strip().split()
    if not cmd:
        continue
    if cmd[0] == "move" and len(cmd) == 5:
        from_pos = (int(cmd[1]), int(cmd[2]))
        to_pos = (int(cmd[3]), int(cmd[4]))
        char = game.board.get_character(from_pos)
        if char and char in game.players[game.current_player]:
            game.move_character(char, to_pos)
        else:
            print("Invalid move: No such character or not your character.")
    elif cmd[0] == "attack" and len(cmd) == 5:
        att_pos = (int(cmd[1]), int(cmd[2]))
        tgt_pos = (int(cmd[3]), int(cmd[4]))
        attacker = game.board.get_character(att_pos)
        target = game.board.get_character(tgt_pos)
        if attacker and target and attacker in game.players[game.current_player]:
            game.attack_character(attacker, target)
        else:
            print("Invalid attack: Check positions and ownership.")
    elif cmd[0] == "end":
        game.end_turn()
    else:
        print("Unknown command.")

print("Game over!") 