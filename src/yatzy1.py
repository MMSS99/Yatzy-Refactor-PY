class Yatzy:
    
    ZERO = 0
    # Moved constructor method to the top of the class
    # Changed arguments d1, d2... to die1, die2
    # Re-defined self.dice from a list holding 5 zeroes to a list holding the values of the arguments from the start (which, if not give, shall remain 0)
    def __init__(self, *dice):
        self.dice = list(dice)

    # Eliminated @staticmethod as it will now depend of the class instance
    # Simplified into returning the sum of all Yatzy instance dice.
    def chance(self):
        return sum(self.dice)

    # Eliminated @staticmethod as it will now depend of the class instance
    # Simplified into returning 50 if all items in a list are the same (data obtained from the length of a set); if the set length is other than 1, return 0
    def yatzy(self):
        YATZY = 50
        return YATZY if len(set(self.dice)) == 1 else self.ZERO


    # Eliminated @staticmethod as it will now depend of the class instance
    # Simplified into returning the sum of a list compresension of self.dice that only stores the value defined in the filter constant
    def ones(self):
        FILTER = 1
        return sum([die for die in self.dice if die == FILTER])

    # Eliminated @staticmethod as it will now depend of the class instance
    # Simplified into returning the sum of a list compresension of self.dice that only stores the value defined in the filter constant
    def twos(self):
        FILTER = 2
        return sum([die for die in self.dice if die == FILTER])

    # Eliminated @staticmethod as it will now depend of the class instance
    # Simplified into returning the sum of a list compresension of self.dice that only stores the value defined in the filter constant
    def threes(self):
        FILTER = 3
        return sum([die for die in self.dice if die == FILTER])

    # Simplified into returning the sum of a list compresension of self.dice that only stores the value defined in the filter constant
    def fours(self):
        FILTER = 4
        return sum([die for die in self.dice if die == FILTER])

    # Simplified into returning the sum of a list compresension of self.dice that only stores the value defined in the filter constant
    def fives(self):
        FILTER = 5
        return sum([die for die in self.dice if die == FILTER])

    # Simplified into returning the sum of a list compresension of self.dice that only stores the value defined in the filter constant
    def sixes(self):
        FILTER = 6
        return sum([die for die in self.dice if die == FILTER])

    # Barely legible, but takes the highest pair and sums it.
    # Simplified arguments: recieved all dices separatedly, only self is needed.
    # Morphed into the sum of a list comprehension that uses a sorted list made out of the set of self.dice to parse through the values of the dice in a max to min order, returning only the first possition of the list to take only the highest value
    def score_pair(self):
        X_OF_A_KIND = 2
        return sum([value*X_OF_A_KIND for value in sorted(set(self.dice), reverse=True) if self.dice.count(value) >= X_OF_A_KIND][:1])

    # Simplified arguments: recieved all dices separatedly, only self is needed.
    def two_pair(self):
        X_OF_A_KIND = 2
        candidate_values = [value*X_OF_A_KIND for value in sorted(set(self.dice), reverse=True) if self.dice.count(value) >= X_OF_A_KIND][:2]
        return sum(candidate_values) if len(candidate_values) == 2 else self.ZERO
    
    # Simplified arguments: recieved all dices separatedly, only self is needed.
    # Morphed into the sum of a list comprehension that uses a sorted list made out of the set of self.dice to parse through the values of the dice in a max to min order, returning only the first possition of the list to take only the highest value
    def three_of_a_kind(self):
        X_OF_A_KIND = 3
        return sum([value*X_OF_A_KIND for value in sorted(set(self.dice), reverse=True) if self.dice.count(value) >= X_OF_A_KIND][:1])

    # Simplified arguments: recieved all dices separatedly, only self is needed.
    # Morphed into the sum of a list comprehension that uses a sorted list made out of the set of self.dice to parse through the values of the dice in a max to min order, returning only the first possition of the list to take only the highest value
    def four_of_a_kind(self):
        X_OF_A_KIND = 4
        return sum([value*X_OF_A_KIND for value in sorted(set(self.dice), reverse=True) if self.dice.count(value) >= X_OF_A_KIND][:1])

    # Change arguments: only self.dice needed.
    # Values saves the ordered values of the die, which are then comparated to the small straight combination during the return statement
    def small_straight(self):
        SMALL_STRAIGHT = {1, 2, 3, 4, 5}
        values = set(self.dice)
        return sum(values) if values == SMALL_STRAIGHT else self.ZERO

    # Change arguments: only self.dice needed.
    # Values saves the ordered values of the die, which are then comparated to the large straight combination during the return statement
    def large_straight(self):
        LARGE_STRAIGHT = {2, 3, 4, 5, 6}
        values = set(self.dice)
        return sum(values) if values == LARGE_STRAIGHT else self.ZERO

    # Change arguments: only self.dice needed.
    # Function checks each possible value: if it finds three of a kind it saves it (can only happen once so it remains in code), with an elif that is designed to separate those dice from possible pairs

    def full_house(self):
        THREE_OF_A_KIND = 3
        PAIR = 2

        threeofakind_value = 0
        pair_value = 0

        for die in self.dice:
            if self.dice.count(die) == PAIR:
                pair_value = self.score_pair()
            elif self.dice.count(die) == THREE_OF_A_KIND:
                threeofakind_value = self.three_of_a_kind()

            if threeofakind_value and pair_value:
                return threeofakind_value + pair_value
        
        return self.ZERO
      
            

