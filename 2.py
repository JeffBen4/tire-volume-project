import math

# Solicitar los valores al usuario
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calcular el volumen usando la fórmula proporcionada
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Mostrar el resultado
print(f"The approximate volume is {volume:.2f} liters")