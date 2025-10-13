import math


def time_of_flight(height):
    """
    Compute a cannonball's ideal time of flight.

    :param height: A floating point initial height
    :return: A floating point time of flight
    """
    return math.sqrt(2 * height / 9.81)


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
    # NOTE: Our first attempt at finding bugs is to add print statements
    #       throughout our program -- we want to know exactly what our program
    #       was doing at each step along the way, rather than trying to infer
    #       from what we can see at the end.
    # print(shot, distance, width)
    return distance <= shot and shot <= distance + width


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
