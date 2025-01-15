import math

def main():
  
  radius = float(input("Enter the radius of a cylinder: "))
  height = float(input("Enter the height of a cylinder: "))

  volume = compute_cylinder_volume(radius, height)

  print(f"Volume: {volume:.2f}")

def compute_cylinder_volume(radius, height):

  volume = math.pi * radius**2 * height
  return volume

main()