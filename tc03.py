from bowling_game_fix_arshdeep import BowlingGame

g = BowlingGame()
for _ in range(21):
    g.roll(5)

print("TC03 All Spares -> Expect 150, Got:", g.score())
