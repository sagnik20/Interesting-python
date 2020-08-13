import time
print("Press 's' to start the StopWatch")

while True:
    q=input()
    if(q=='s'):
        startTime = time.time()
        print("StopWatch Started . ... .")
        print("Press 'd' to stop the stop watch")
    elif q=='d' :
        endTime = time.time()
        print("StopWatch Stopped . ... .")
        print("Time = ",round(endTime-startTime,2)," seconds")
        break
    else:
        print("Sorry! Wrong Input :( ")
        print("Press 'd' to stop the stop watch")