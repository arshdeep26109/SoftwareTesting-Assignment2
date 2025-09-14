from bowling_game_fix_arshdeep import BowlingGame

g = BowlingGame()
for _ in range(9):
    g.roll(0)
    g.roll(0)
g.roll(10)
g.roll(10)
g.roll(10)

print("TC06 Strike Final -> Expect 30, Got:", g.score())
