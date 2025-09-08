class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        score_total = 0
        idx = 0
        for frame in range(10):
            if self.rolls[idx] == 10:
                score_total += 10 + self.rolls[idx+1] + self.rolls[idx+2]
                idx += 1
            elif self.rolls[idx] + self.rolls[idx+1] == 10:
                score_total += 10 + self.rolls[idx+2]
                idx += 2
            else:
                score_total += self.rolls[idx] + self.rolls[idx+1]
                idx += 2
        return score_total
