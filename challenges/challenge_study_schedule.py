def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    counter = 0

    for time in permanence_period:
        if (type(time[0]) is not int or type(time[1]) is not int):
            return None

        elif target_time in range(time[0], time[1] + 1):
            counter += 1

    return counter
