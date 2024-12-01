# Refer to https://exercism.org/tracks/python/exercises/robot-simulator

# Create your solution below

robot = {
    "x": 7,
    "y": 3,
    "dir": "north"
}

def advance(_rob):
    if _rob["dir"] == "north":
        _rob["y"] += 1
    elif _rob["dir"] == "west":
        _rob["x"] -= 1
    elif _rob["dir"] == "south":
        _rob["y"] -= 1
    elif _rob["dir"] == "east":
        _rob["x"] += 1
    return _rob


def left(_rob):
    if _rob["dir"] == "north":
        _rob["dir"] = "west"
    elif _rob["dir"] == "west":
        _rob["dir"] = "south"
    elif _rob["dir"] == "south":
        _rob["dir"] = "east"
    elif _rob["dir"] == "east":
        _rob["dir"] = "north"
    return _rob


def right(_rob):
    if _rob["dir"] == "north":
        _rob["dir"] = "east"
    elif _rob["dir"] == "west":
        _rob["dir"] = "north"
    elif _rob["dir"] == "south":
        _rob["dir"] = "west"
    elif _rob["dir"] == "east":
        _rob["dir"] = "south"
    return _rob


def robot_position(_rob):
    print(f"({_rob['x']}, {_rob['y']}) facing {_rob['dir']}")


def instructions(letters, _rob):
    for letter in letters:
        if letter == "R":
            _rob = right(_rob)
        elif letter == "L":
            _rob = left(_rob)
        elif letter == "A":
            _rob = advance(_rob)
    return _rob

robot_position(robot)

message = input("provide R for right, L for left, and A for advance\n")

robot = instructions(message, robot)

robot_position(robot)
