def flip(n):
    odds = 1.0         # start with 50% chance of the magic coin, which is the same as odds = 1:1
    r = 1.0 / 0.5
    for i in range(n):
        odds *= r
              # edit here to update the odds
    return odds
    print(odds)



