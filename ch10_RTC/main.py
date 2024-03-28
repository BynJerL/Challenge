from datetime import datetime
from time import sleep
from myfun import clear_line as cl

def showTime():
    now = datetime.now()

    currDate = now.strftime("%A, %m/%d/%Y")
    currTime = now.strftime("%H:%M:%S")
    
    print(f"CLI DATETIME (press ctrl+c to quit):\n{currDate}\n{currTime}")

if __name__ == "__main__":
    try: 
        while(1):
            showTime()
            sleep(.1)
            cl(3)
    except KeyboardInterrupt:
        print("\nQuitting the program")

        