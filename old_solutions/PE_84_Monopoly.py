from random import randint

# ================================================================================== #
# At the beginning of the game, the CC and CH cards are shuffled. !!!!!!!!!!!!!!!!!! #
# ================================================================================== #


class Monopoly:

    def __init__(self, dice_n_faces:int) -> object:

        # Number of faces on each die
        self.dice_n_faces = dice_n_faces
    
        # Board
        self.squares = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
                        'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
                        'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
                        'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']

        # Options for Community Chest. 16 cards in total.
        self.community_chest = {1:"GO",
                                2:"JAIL"}
        
        # Options for Chance. 16 cards in total.
        self.chance = {1:"GO",
                       2:"JAIL",
                       3:"C1",
                       4:"E3",
                       5:"H2",
                       6:"R1",
                       7:"R",
                       8:"R",
                       9:"U",
                       10:"-3"}
        
        # Index of special squares on the board
        self.special = {"GO":0,
                        "JAIL":10}
        
        # Save how many times the player has visited a square
        self.visited_by_player = {}
        for square in self.squares:
            self.visited_by_player[square] = 0

        # Position of the player in the board
        self.player_pos = 0

        # Queue to know if the last three throws for the player
        # have been a pair.
        self.pair_queue = [False, False, False]
        
    # Throw 2 dice and save the sum of them and
    # if they form a pair.
    def throw_2_dice(self):
        throw = (randint(1, self.dice_n_faces), randint(1, self.dice_n_faces))
        moves = sum(throw)
        pair = (throw[0] == throw[1])
        return moves, pair
    
    # Returns the string representation of the square
    # the player is currently at.
    def get_square(self):
        return self.squares[self.player_pos]
    
    # Returns the index of a square in string representation
    def get_index(self, square):
        return self.squares.index(square)


    # Check for any special action and update
    # the players position based on it.
    def special_actions(self):

        # If player gets three consecutive pairs,
        # sent it to JAIL.
        if self.pair_queue == [True, True, True]:
            self.player_pos = self.special["JAIL"]

        square = self.get_square()

        # Check for GO TO JAIL
        if square == "G2J":
            self.player_pos = self.special["JAIL"]

        # Check for Community Chest
        if "CC" in square:
            action = randint(1, 16)

            if action <= 2:
                new_square = self.community_chest[action]
                new_index = self.get_index(new_square)

                self.player_pos = new_index

        # Check for Chance
        if "CH" in square:
            action = randint(1, 16)

            if action <= 10:
                
                # Go to [square]
                if action <= 6:
                    new_square = self.chance[action]
                    new_index = self.get_index(new_square)

                    self.player_pos = new_index

                else:
                    special = self.chance[action]
                    
                    # Go to next railway company
                    if special == "R":

                        if self.player_pos < 5 or self.player_pos > 35:
                            new_index = self.get_index("R1")
                            self.player_pos = new_index

                        elif self.player_pos < 15 and self.player_pos > 5:
                            new_index = self.get_index("R2")
                            self.player_pos = new_index

                        if self.player_pos < 25 and self.player_pos > 15:
                            new_index = self.get_index("R3")
                            self.player_pos = new_index

                        else:
                            new_index = self.get_index("R4")
                            self.player_pos = new_index

                    # Go to next railway company
                    if special == "U":

                        if self.player_pos < 12 or self.player_pos > 28:
                            new_index = self.get_index("U1")
                            self.player_pos = new_index

                        else:
                            new_index = self.get_index("U2")
                            self.player_pos = new_index

                    # Go back 3 squares
                    if special == "-3":
                        self.player_pos -= 3
    

    def simulate(self, n_turns):

        for turn in range(n_turns):

            # Remove the pair check from 3 turns ago.
            self.pair_queue.pop(0)

            # Throw the dice.
            moves, pair = self.throw_2_dice()

            # Add the pair check for this turn to the list.
            self.pair_queue.append(pair)

            # Update the player's position
            self.player_pos = (self.player_pos + moves) % 40

            # Apply special actions
            self.special_actions()

            # Update the "visited dictionary"
            square = self.get_square()
            self.visited_by_player[square] += 1

    # Print the state of the current simulation.
    def print_state(self):
        for key, value in self.visited_by_player.items():
            print(f"{key}: {value}")

    # Get three most visited squares on the board.
    def print_most_visited(self):
        squares = []
        total = 0

        for key, value in self.visited_by_player.items():
            squares.append((key, value))
            total += value

        squares.sort(key=lambda x:x[1], reverse=True)

        best = squares[:3]

        modal_string = ""
        for b0, b1 in best:
            print(f"{b0}: {b1/total * 100}%")
            modal_string += str(self.get_index(b0))

        print("Modal_string: ", modal_string)
