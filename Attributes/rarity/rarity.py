def rarity(value):
    if value <= 0.35:
        if value <= 0.05:
            print("SSR")
        elif 0.15 >= value > 0.05:
            print("SR")
        elif 0.35 >= value > 0.15:
            print("R")
    else:
        print("N")
