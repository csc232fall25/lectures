import math


def time_of_flight(height):
    return 0


def range_of_shot(velocity, time):
    """
    Compute a cannonball's ideal range.

    :param velocity: A floating point velocity
    :param time: A floating point time of flight
    :return: The floating point range
    """
    return velocity * time


def is_hit(shot, distance, width):
    """
    Determine whether or not a cannonball hits.

    :param shot: A cannonball's floating point range
    :param distance: A floating point target distance
    :param width: A floating point target width
    :return: Whether or not the cannonball hits
    """
    return distance <= shot


def main():
    height = float(input("How high is the cannon (m)? "))
    velocity = float(input("How fast is the ball (m/s)? "))
    distance = float(input("How far is the target (m)? "))
    width = float(input("How wide is the target (m)? "))

    time = time_of_flight(height)
    shot = range_of_shot(velocity, time)
    print("The cannonball will travel " + str(round(shot, 2)) + " m.")

    if is_hit(shot, distance, width):
        print("Hit!")
    else:
        print("Miss!")


if __name__ == "__main__":
    main()
