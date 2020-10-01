import time
print("Press 's' to start the StopWatch") #asking the user to press s if user wants to start the stopwatch

while True:    #loop will run while the condition is true 
    q=input()
    if(q=='s'): # if q = s then stopwatch will start running
        startTime = time.time()
        print("StopWatch Started . ... .")
        print("Press 'd' to stop the stop watch") # asking the user to press d if he wants to stop the watch
    elif q=='d' :  # checking condition for stoping the watch 
        endTime = time.time()
        print("StopWatch Stopped . ... .")
        print("Time = ",round(endTime-startTime,2)," seconds")
        break
    else:   # if the user gives a invalid input to start or stop then the following loop will be executed 
        print("Sorry! Wrong Input :( ")
        print("Press 'd' to stop the stop watch")
