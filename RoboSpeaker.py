import os

if __name__ == '__main__':
    print("RoboSpeaker 1.0")
    while(True):
        x = input("Enter What you want to Speak: ")
        if x == 'end':
            break
        command = f"echo {x}"
        os.system(command)
