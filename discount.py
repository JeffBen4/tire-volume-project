from datetime import datetime

day = datetime.now()
day_week = day.weekday()


mount = 1
while mount != 0:
    mount = float(input("Please enter de subtotal: "))
    if mount != 0:
        if day_week == 2 or day_week == 3:
        
            discount = mount * 0.1
            mount -= discount
            tax = mount * 0.06
            mount += tax
            print(f"Discount amount: {discount:.2f}")
            print(f"Sales tax amount: {tax:.2f}")
            print (f"Total: {mount:.2f}")
        else:
            tax = mount * 0.06
            mount += tax
            print(f"Sales tax amount: {tax:.2f}")
            print (f"Total: {mount:.2f}")
    else: 
        print("Thank you.")