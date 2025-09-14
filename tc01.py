from bowling_game_fix_arshdeep import BowlingGame

g = BowlingGame()
for _ in range(20):
    g.roll(0)

print("TC01 Gutter -> Expect 0, Got:", g.score())
