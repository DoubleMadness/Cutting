#Imports (Libraries)
import datetime
from PIL import Image
from moviepy.editor import VideoFileClip

def cutting():
    clear()
    try:
        file = VideoFileClip(input("Write the path to the file - "))
        clear()
        action = input("Select action:\n1 - Cut Frame\n2 - Cut Clip\nYour select - ")
        if action not in ["1", "2"]:
            error()
            cutting()
        match action:
            case "1":
                cut_frame(file)
                file.close()
            case "2":
                cut_clip(file)
                file.close()
    except:
        error()
        cutting()
    clear()
    main()

def calculator():
    try:
        full_time = input("Write your time (Example - X:XX:XX) - ")
        timea, timeb, timec = full_time.split(":")
        complete_time = int(timec) + (int(timeb)*60) + (int(timea)*360)
        print("Your time in seconds is " + str(complete_time))
        wait_any_key()
    except:
        error()
        calculator()
    clear()
    main()

def about():
    clear()
    print("Cutting is a program that allows you to cut videos into mini-clips / cut frames from it.")
    print("A time calculator is also available to convert to seconds, because the program works in them!\n")
    print("The program may create temporary files, which will not interfere with your work, but you can delete them!")
    print("Version - 1.0.0")
    # Split it (^^^) on 4 lines for goodlooking!
    wait_any_key()
    main()

def main():
    import os
    if not os.path.exists("Pictures"):
        os.makedirs("Pictures")
    if not os.path.exists("Videos"):
        os.makedirs("Videos")
    #options
    option = input(
        "Please select option:\n1 - Start cutting\n2 - Time Calculator\n3 - About the programm\nYour select - ")
    try:
        if option not in ["1", "2", "3"]:
            error()
            main()
        match option:
            case "1":
                clear()
                cutting()
            case "2":
                clear()
                calculator()
            case "3":
                clear()
                about()
    except:
        error()
        main()



def cut_frame(file):
    time = input("Write the time (In seconds) - ")
    clear()
    name = "Pictures/Frame" + get_time() + ".png"

    output_frame = file.get_frame(int(time))
    output = Image.fromarray(output_frame)
    output.save(name)

def cut_clip(file):
    start_time = input("Write the start time (In seconds) - ")
    end_time = input("Write the end time (In seconds) - ")
    clear()
    name = "Videos/Clip" + get_time() + ".mp4"

    output = file.subclip(int(start_time), int(end_time))
    output.write_videofile(name)


def wait_any_key():
    wait = input("\nPress Enter for continue...")
    clear()

def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def error():
    clear()
    print("ERROR\nTry again\n\n")

def get_time():
    __time = str(datetime.datetime.now())
    __time = __time.replace(":", "")
    __time = __time.replace("-", "")
    __time = __time.replace(" ", "")
    _time, tempi = __time.split(".")
    return str(_time)

if __name__ == "__main__":
    main()