def trafficlight():
    signal = input("enter colour of traffic light:")
    if signal not in ("RED", "YELLOW", "GREEN"):
        print("please enter valid light in CAPITALS")
    else:
        value = lightcolour(signal)
        if value == 0:
            print("STOP, your life is precious")
        elif value == 1:
            print("Please go slow")
        else:
            print("GO!")

def lightcolour(colour):
    if colour == "RED":
        return 0
    elif colour == "YELLOW":
        return 1
    else:
        return 2

trafficlight()
print("SPEED THRILLS, BUT KILLS!")
