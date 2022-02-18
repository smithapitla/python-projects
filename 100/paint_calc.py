import math

def paint_calc(height, width, cover):
    cans_needed = (height * width) / cover
    round_up_cans= math.ceil(cans_needed)
    print(f"You'll need {round_up_cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
