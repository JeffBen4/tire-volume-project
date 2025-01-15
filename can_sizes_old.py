import math

def main():

    name = "#1 Picnic"
    radius = 6.83
    height = 10.16


    name = "#1 Tall"
    radius = 7.78
    height = 11.91
    volume = can_vol(radius, height)
    area = can_are(radius, height)
    eff = volume / area
    print(f"{name} volume = {volume:.2f} area = {area:.2f} efficiency= {eff:.2f}\n")

    name = "#2"
    radius = 8.73
    height = 11.59
    volume = can_vol(radius, height)
    area = can_are(radius, height)
    eff = volume / area
    print(f"{name} volume = {volume:.2f} area = {area:.2f} efficiency= {eff:.2f}\n")

    name = "#2.5"
    radius = 10.32
    height = 11.91
    volume = can_vol(radius, height)
    area = can_are(radius, height)
    eff = volume / area
    print(f"{name} volume = {volume:.2f} area = {area:.2f} efficiency= {eff:.2f}\n")

    name = "#3 Cylinder"
    radius = 10.79
    height = 17.78
    volume = can_vol(radius, height)
    area = can_are(radius, height)
    eff = volume / area
    print(f"{name} volume = {volume:.2f} area = {area:.2f} efficiency= {eff:.2f}\n")

    name = "#5"
    radius = 13.02
    height = 14.29
    volume = can_vol(radius, height)
    area = can_are(radius, height)
    eff = volume / area
    print(f"{name} volume = {volume:.2f} area = {area:.2f} efficiency= {eff:.2f}\n")

    name = "#6Z"
    radius = 5.40
    height = 8.89
    volume = can_vol(radius, height)
    area = can_are(radius, height)
    eff = volume / area
    print(f"{name} volume = {volume:.2f} area = {area:.2f} efficiency= {eff:.2f}\n")

    name = "#8Z short"
    radius = 6.83
    height = 7.62
    volume = can_vol(radius, height)
    area = can_are(radius, height)
    eff = volume / area
    print(f"{name} volume = {volume:.2f} area = {area:.2f} efficiency= {eff:.2f}\n")

    name = "#10"
    radius = 15.72
    height = 17.78
    volume = can_vol(radius, height)
    area = can_are(radius, height)
    eff = volume / area
    print(f"{name} volume = {volume:.2f} area = {area:.2f} efficiency= {eff:.2f}\n")

    name = "#211"
    radius = 6.83
    height = 12.38
    volume = can_vol(radius, height)
    area = can_are(radius, height)
    eff = volume / area
    print(f"{name} volume = {volume:.2f} area = {area:.2f} efficiency= {eff:.2f}\n")

    name = "#300"
    radius = 7.62
    height = 11.27
    volume = can_vol(radius, height)
    area = can_are(radius, height)
    eff = volume / area
    print(f"{name} volume = {volume:.2f} area = {area:.2f} efficiency= {eff:.2f}\n")

    name = "303"
    radius = 8.10
    height = 11.11
    volume = can_vol(radius, height)
    area = can_are(radius, height)
    eff = volume / area
    print(f"{name} volume = {volume:.2f} area = {area:.2f} efficiency= {eff:.2f}\n")


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
    print(f"{name} volume={volume:.2f} area={area:.2f} efficiency={eff:.2f}\n")
main()