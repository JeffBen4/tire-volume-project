import math

def main():
    can_sizes = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.4, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.1, 11.11, 0.42]
    ]
    for i in range(len(can_sizes)):
        name = can_sizes[i][0]
        radius = can_sizes[i][1]
        height = can_sizes[i][2]
        cost = can_sizes[i][3]

        compute_cost_efficiency(radius, height, cost)
        can_eff(name,radius,height)

def can_vol(radius,height):
    volume = math.pi * radius ** 2 * height
    return volume

def can_are(radius, height):
    area = 2 * math.pi * radius * (radius + height)
    return area

def can_eff(name, radius, height):
    volume = can_vol(radius, height)
    area = can_are(radius, height)
    eff = volume / area
    print(f"{name} volume = {volume:.2f} area = {area:.2f} efficiency = {eff:.2f}\n")

def compute_cost_efficiency(radius, height, cost):
    volume = can_vol(radius, height)
    efficiency = volume / cost
    print(f"This is the cost efficienty: {efficiency:.2f}")



main()