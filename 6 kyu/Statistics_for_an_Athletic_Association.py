def seconds2hms(seconds: int) -> str:
    hours = seconds // 3600
    hours = str(hours) if hours > 9 else "0" + str(hours)
    seconds %= 3600
    minutes = seconds // 60
    minutes = str(minutes) if minutes > 9 else "0" + str(minutes)
    seconds %= 60
    seconds = str(seconds) if seconds > 9 else "0" + str(seconds)
    return "|".join((hours, minutes, seconds))


def stat(data):
    if data == "":
        return ""
    data = [tuple(map(int, i.split("|"))) for i in data.split(", ")]
    data_in_seconds = [i[0] * 3600 + i[1] * 60 + i[2] for i in data]
    range_in_seconds = max(data_in_seconds) - min(data_in_seconds)
    avg_in_seconds = sum(data_in_seconds) // len(data_in_seconds)
    mid = len(data) // 2
    sorted_data_in_seconds = list(sorted(data_in_seconds))
    median_in_seconds = (sorted_data_in_seconds[mid] + sorted_data_in_seconds[~mid]) // 2
    range_value = "Range: " + seconds2hms(range_in_seconds)
    avg_value = "Average: " + seconds2hms(avg_in_seconds)
    median_value = "Median: " + seconds2hms(median_in_seconds)
    return " ".join((range_value, avg_value, median_value))


print(stat("01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"))
