from bowling_game_fix_arshdeep import BowlingGame

g = BowlingGame()
rolls = [3,4, 2,5, 1,6, 4,2, 8,1, 7,1, 5,3, 2,3, 4,3, 2,6]
for r in rolls:
    g.roll(r)

print("TC04 Regular Open -> Expect 72, Got:", g.score())
