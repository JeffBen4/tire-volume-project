def main():
  start_miles = float(input("Enter the first odometer reading (miles): "))
  end_miles = float(input("Enter the second odometer reading (miles): "))
  amount_gallons = float(input("Enter the amount of fuel used (gallons): "))

  mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
  lp_100k = lp100k_from_mpg(mpg)
  
  print(f"{mpg:.2f} miles per gallon.")
  print(f"{lp_100k:.2f} liters per 100 kilometers.")

def miles_per_gallon(start_miles, end_miles, amount_gallons):
  formula = (end_miles - start_miles) / amount_gallons
  return formula

def lp100k_from_mpg(mpg):
  return 235.215 / mpg

main()