from bowling_game_fix_arshdeep import BowlingGame

g = BowlingGame()
for _ in range(9):
    g.roll(0)
    g.roll(0)
g.roll(7)
g.roll(3)
g.roll(5)

print("TC05 Spare Final -> Expect 15, Got:", g.score())
