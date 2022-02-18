import schedule
import time
  
# Functions setup
def geeks():
    print("Shaurya says Geeksforgeeks")
  
# Task scheduling
# After every 10mins geeks() is called. 
schedule.every(10).seconds.do(geeks)

while True:
  
    # Checks whether a scheduled task 
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)