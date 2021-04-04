import math

coverage = 53.8196

def paint(length, width, cover):

    area = length * width
    cans = math.ceil(area / cover)

    print(f"You will need {cans} cans of paint for your wall.")


paint(15, 8, coverage)