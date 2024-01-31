weight = input("Weight: ")

what_weight = input("(L)bs or (K)g: ")

if what_weight.lower() == "l":
    weight = float(weight) * 0.4536
elif what_weight.lower() == "k":
    weight = float(weight) / 0.4536
else:
    print("Wrong Charater!")

print(f"Your weight is {weight}")
