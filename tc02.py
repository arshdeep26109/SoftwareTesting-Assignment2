from bowling_game_fix_arshdeep import BowlingGame

g = BowlingGame()
for _ in range(12):
    g.roll(10)

print("TC02 Perfect -> Expect 300, Got:", g.score())
