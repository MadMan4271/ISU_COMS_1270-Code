t = float(input("What is the time in seconds: "))

v = float(input("What is the velocity in meters per second: "))

a = float(input("What is the acceleration in meter per second squared: "))

# Citation - https://www.calculatorsoup.com/calculators/physics/velocity_a_t.php (2/2/2026)

vf = v+ (t*a)

print("The final velocity is: " + str(vf))
