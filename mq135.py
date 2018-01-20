import time
import botbook_mcp3008 as mcp 


def readSmokeLevel():
    global smokeLevel
    smokeLevel= mcp.readAnalog()
    #print (smokeLevel)
def main():
        while True:
            readSmokeLevel() 
            print (smokeLevel)
            if smokeLevel > 0.1:
               print ("Smoke detected")
            time.sleep(1) # s


main()