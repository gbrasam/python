from give_bmi import give_bmi, apply_limit
height = [2.71, 1.15]
weight = [165.3, 38.4]
# height = [2.71]
# weight = [165.3, 38.4]
# height = [2.71, 1.15]
# weight = ["Hello", 38.4]
# height = [2.71, 1.15]
# weight = []
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))