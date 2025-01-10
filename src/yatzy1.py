class Yatzy:

    # Moved constructor method to the top of the class
    # Changed arguments d1, d2... to die1, die2
    # Re-defined self.dice from a list holding 5 zeroes to a list holding the values of the arguments from the start (which, if not give, shall remain 0)
    def __init__(self, die1=0, die2=0, die3=0, die4=0, die5=0):
        self.dice = [die1, die2, die3, die4, die5]

    # Eliminated @staticmethod as it will now depend of the class instance
    # Simplified into returning the sum of all Yatzy instance dice.
    def chance(self):
        return sum(self.dice)

    # Eliminated @staticmethod as it will now depend of the class instance
    # Simplified into returning 50 if all items in a list are the same (data obtained from the length of a set); if the set length is other than 1, return 0
    def yatzy(self):
        return 50 if len(set(self.dice)) == 1 else 0


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
        return sum(candidate_values) if len(candidate_values) == 2 else 0

    # Simplified arguments: recieved all dices separatedly, only self is needed.
    # Morphed into the sum of a list comprehension that uses a sorted list made out of the set of self.dice to parse through the values of the dice in a max to min order, returning only the first possition of the list to take only the highest value
    def four_of_a_kind(self):
        X_OF_A_KIND = 4
        return sum([value*X_OF_A_KIND for value in sorted(set(self.dice), reverse=True) if self.dice.count(value) >= X_OF_A_KIND][:1])

    # Simplified arguments: recieved all dices separatedly, only self is needed.
    # Morphed into the sum of a list comprehension that uses a sorted list made out of the set of self.dice to parse through the values of the dice in a max to min order, returning only the first possition of the list to take only the highest value
    def three_of_a_kind(self):
        X_OF_A_KIND = 3
        return sum([value*X_OF_A_KIND for value in sorted(set(self.dice), reverse=True) if self.dice.count(value) >= X_OF_A_KIND][:1])

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
