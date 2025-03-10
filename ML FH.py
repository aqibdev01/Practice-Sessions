import csv
import datetime

def reading():
    with open("sample.txt", "r") as reading_file:
        content = reading_file.read()

        print(content)

def writing():
    with open("output.txt", "w") as writing:
        strings = ["Hello\n","There\n","Beautiful\n","File\n","We\n","are having"]
        lines = writing.writelines(strings)

def copy_pasting():
    with open("source.txt", "r") as copying:
        content = copying.read()

    with open("destination.txt", "w") as pasting:
        pasting.write(content)

def appending():
    with open("log.txt", "a") as appending_file:
        string = "\nThis is appended line"

        appending_file.write(string)


def reading_lines():
    with open("sample.txt", "r") as reading_lines:
        text = reading_lines.read()
        words = text.split()
    return len(words)
    
def Replacing_value():
    old_val = "Hello"
    new_val = "Hi"
    with open("sample.txt", "r") as replacing_file:
        content = replacing_file.read()
        new_text = content.replace(old_val, new_val)
    with open("sample.txt", "w") as placing:
        placing.write(new_text)

def read_reverse():
    with open("sample.txt", "r") as reversing:
        lines = reversing.readlines()
    for line in reversed(lines):
        print(line.strip())

# read_reverse()
def counting():
    with open("sample.txt", "r") as counting:
        lines = counting.readlines()
        words = sum(len((line.split())) for line in lines)
        characters = sum(len(line) for line in lines)

    return len(lines), words, characters

# print(counting())

def merging():
    file_list = ["destination.txt", "log.txt", "sample.txt"]
    with open("output.txt", "a") as merge_into:
        for fname in file_list:
            with open(fname, "r") as file:
                content = file.read()
                merge_into.write(content + "\n")

# merging()

def divide_file():
    with open("output.txt", "r") as large:
        lines = large.readlines()
        for i in range(0, len(lines), 10):
            with open(f"output.txt_part{i//10+1}", "w") as writer:
                writer.writelines(lines[i:i + 10])

# divide_file()

def log_file():
    time_stamp = datetime.datetime.now()
    with open("log_file.txt", "a") as file:
        file.write(f"{time_stamp}\tThis is log message.\n")

# log_file()

def csv_reading():
    with open("sample.txt", "r") as file:
        reader = csv.DictReader(file)
        print(list(reader))

# csv_reading()

def read_protected_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except PermissionError as e:
        print(f"Permission error: {e}")

read_protected_file('log.txt')