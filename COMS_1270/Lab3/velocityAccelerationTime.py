# Caden Burbridge                       02/09/2026
# Lab week 3 - This calculates final velocity

def velocityAccelerationTime(time, iVelo, accel):
    return iVelo + (time * accel)

def main():
    t = float(input("What is the time in seconds: "))

    v = float(input("What is the initial velocity in meters per second: "))

    a = float(input("What is the acceleration in meter per second squared: "))

    # Citation - https://www.calculatorsoup.com/calculators/physics/velocity_a_t.php (2/2/2026)

    vf = velocityAccelerationTime(t, v, a)

    print(f"The final velocity is: {vf}")

if __name__ == "__main__":
    main()