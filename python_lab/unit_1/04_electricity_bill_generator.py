# Electricity Bill Generator
# This program calculates an electricity bill using slab rates.

print("Electricity Bill Generator")

try:
    units = float(input("Enter electricity units consumed: "))
except ValueError:
    print("Please enter a valid number of units.")
else:
    if units < 0:
        print("Units consumed cannot be negative.")
    else:
        if units <= 100:
            energy_charge = units * 1.50
        elif units <= 200:
            energy_charge = (100 * 1.50) + ((units - 100) * 2.50)
        elif units <= 500:
            energy_charge = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
        else:
            energy_charge = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + ((units - 500) * 6.00)

        fixed_charge = 50.00
        total_bill = energy_charge + fixed_charge

        print("\nElectricity Bill")
        print("Units consumed:", units)
        print("Energy charge: Rs.", format(energy_charge, ".2f"))
        print("Fixed charge: Rs.", format(fixed_charge, ".2f"))
        print("Total bill: Rs.", format(total_bill, ".2f"))
