import os
import time


def filter_log_by_level(log_file_path, level):
    """
    Filters log messages by a specific level (e.g. "INFO", "WARNING", "ERROR") and returns them in a list.
    Uses file.readlines(sizehint) to read the file.
    """
    messages = []
    with open(log_file_path, 'r') as f:
        for line in f.readlines():
            if line.startswith(level):
                messages.append(line.strip())
    return messages


def count_events_by_module(log_file_path):
    """
    Counts how many events occurred for each module in the application and returns a dictionary with the results.
    Uses file.readline() to read the file and file.seek(offset[, whence]) and file.tell() to search for a module name.
    """
    events = {}
    with open(log_file_path, 'r') as f:
        while True:
            pos = f.tell()
            line = f.readline()
            if not line:
                break
            if " - " not in line:
                continue
            module = line.split(" - ")[1].split()[0]
            events[module] = events.get(module, 0) + 1
            pos_end = f.tell()
            f.seek(pos)
            if pos == pos_end:
                break
    return events


def generate_log_report(log_file_path, report_file_path):
    """
    Generates a statistical report based on the information extracted from the log file, including the number of events
    per module and the frequency of events per level. Writes the statistical report in a new file using file.write(str)
    and file.writelines(sequence).
    """
    report = []
    levels = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    events_by_module = count_events_by_module(log_file_path)
    report.append("Events per module:\n")
    for module, count in events_by_module.items():
        report.append(f"{module}: {count}\n")
    report.append("\nFrequency of events per level:\n")
    with open(log_file_path, 'r') as f:
        for line in f.readlines():
            if " - " not in line:
                continue
            level = line.split(" - ")[0]
            levels[level] += 1
    for level, count in levels.items():
        report.append(f"{level}: {count}\n")
    with open(report_file_path, 'w') as f:
        f.writelines(report)


def real_time_log_monitoring(log_file_path):
    """
    Allows real-time monitoring of the log file. It checks if new lines have been added to the file and processes them
    accordingly. Uses file.next() and file.truncate([size]).
    """
    with open(log_file_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            print(line.strip())
            if not os.isatty(f.fileno()):
                break
            f.next()
            f.truncate()
            f.flush()


# Example usage:
log_file_path = "log.txt"
report_file_path = "log_report.txt"
messages = filter_log_by_level(log_file_path, "ERROR")
print(messages)
generate_log_report(log_file_path, report_file_path)
real_time_log_monitoring(log_file_path)
