"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
age = int(input("Please enter your age: "))
maximum_heart = 220 - age
rate = maximum_heart / 100
mim_rate = rate * 65
max_rate = rate * 85

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {mim_rate:.0f} and {max_rate:.0f} beats per minute.")
