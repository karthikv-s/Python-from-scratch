weight=int(input("Enter your weight:"))
unit=input("Enter your unit L(lbs) or K(kg): ")
unit2=unit.upper()
if unit2=="L":
    weight_in_kg=float(weight)*0.45
    print(f"Weight in Kg is{weight_in_kg} kg")
elif unit2=="K":
    weight_in_lbs=float(weight)/0.45
    print(f"Weight in lbs is {weight_in_lbs} lbs")
else:
    print("Invalid unit")