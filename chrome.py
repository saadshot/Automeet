import time
import pyautogui
import win32gui
import win32process
import win32con
from subprocess import Popen
'''find urls, enter them in list'''
url="www.google.com"
urlcur = 'https://meet.google.com/mip-hfvd-xnq?authuser=2'
'''
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application//chrome.exe"))
webbrowser.get('chrome').open_new(url)'''
def callback(hwnd,hwnds):
	if win32gui.IsWindowVisible (hwnd) and win32gui.IsWindowEnabled (hwnd):
		hwnds=hwnds.append(hwnd)

def gethwnd(hwnds,pid):
	for i in hwnds:
		if win32gui.GetWindowText(i).find("Meet") != -1 and win32gui.GetWindowText(i).find("Google Chrome") != -1:
			print("f")
			return i
	return None

def open_browser_window(urlcur):
	browser=Popen(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe","--new-window",urlcur], shell=True)
	time.sleep(3)
	hwnds=[]
	win32gui.EnumWindows (callback, hwnds)
	x=gethwnd(hwnds,browser.pid)
	if x != None:
		bwindow=x
		return bwindow
	return None

def maximize_bwindow(bwindow):
	win32gui.ShowWindow(bwindow,win32con.SW_MAXIMIZE)
	pyautogui.click(1520,229)

def joinclass(urlcur):
	bwindow=open_browser_window(urlcur)
	maximize_bwindow(bwindow)
	time.sleep(3)
	cc=[]	#click coordinates
	cc.append(pyautogui.locateOnScreen('join2.png'))
	cc.append(pyautogui.locateOnScreen('cam_on.png'))
	cc.append(pyautogui.locateOnScreen('meetlogo.png'))
	cc.append(pyautogui.locateOnScreen('mic_unmuted.png'))
	if(cc[0]!=None):
		for i in cc:
			if i != None:
				i=pyautogui.center(i)
		if(cc[2]!=None):
			pyautogui.rightClick(cc[2])
			cc.append(pyautogui.locateOnScreen('mutesite.png'))
			if(cc[4] != None):
				cc[4]=pyautogui.center(cc[4])
				pyautogui.center(cc[4])
		if(cc[1]!=None):
			pyautogui.click(cc[1])
		if(cc[3]!=None):
			pyautogui.click(cc[3])
		pyautogui.click(cc[0])
	else:
		pass
	
joinclass(urlcur)
