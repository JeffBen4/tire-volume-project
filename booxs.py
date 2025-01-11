import math

number_items = int(input("Enter the number of items: "))
number_boxes = int(input("Enter the number of items per boxes: "))
needed = math.ceil(number_items / number_boxes)

print(f"For {number_items} items, packing {number_boxes}"
      f" items in each box, you well need {needed} boxes.")
print(“book”)