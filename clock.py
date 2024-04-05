from playsound import playsound
import time

CLEAR= "\033[2J"
CLEAR_AND_RETURN= "\033[H]" #to clear and return to the same position



def alarm(seconds):
    time_elapsed=0
    
    print(CLEAR)
    
    while time_elapsed < seconds:
        time.sleep(1) #wait for 1 sec
        time_elapsed+=1
        
        time_left= seconds-time_elapsed #how much time is remaining
        minutes_left= time_left//60  
        seconds_left= time_left%60
        
        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left}")
        
    playsound("alarm.mp3")
    
minutes= int(input("Set the time in minutes to wait"))
seconds= int(input("Set the time in seconds to wait"))
total_seconds = minutes*60*seconds
        
alarm(total_seconds)