# Caden Burbridge                       02/09/2026
# Lab week 3 - This calculates distance

def distanceSpeedTime(velo, time):
    return velo * time


def main():
    v = float(input("What is the speed in meters per second: "))

    t = float(input("What is the time in seconds: "))

    # Citation - https://studymind.co.uk/notes/calculating-distance-travelled/ (2/2/2026)

    distance = distanceSpeedTime(v, t)

    print(f"The total distance traveled is: {distance}")

if __name__ == "__main__":
    main()