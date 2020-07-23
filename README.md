# automeet

# created by BAZ
AUTOMEET is designed to allow a logged in Google user to automatically attend google meet meetings. Primarily to be used to personal college lectures, it has an extensible timetable file which can be used to input various meet links and times, along with days.

This script uses image recognition and emulates human input using pyautogui and win32api. 

Meetings are exited automatically when present time exceeds meeting end time.

CONFIGURATION VARIABLES:
add_to_url: Need to set this variable in python script. Must check ?authuser=var in URL from meet url opened in Chrome and accessing meet homepage with preferred login 
(default = 2) 
xp: list of extra parameters to find in window title to get window_id if meetid is not found in title
daystarttime=:	#efines day start time to not have entire program run before start time (default = 08:00)
dayendtime: when do all classes end, to stop program (default = 17:00)
ttpath: text file with timetable (default = "\timetable.txt")
