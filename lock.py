import sys, os
import time


open_times = 0

def lock(must_wait=False, wait_time=0):
	if(must_wait is True or wait_time is not 0):
		time.sleep(wait_time)
	os.system("adb shell input keyevent 26")
	if(must_wait is True or wait_time is not 0):
		time.sleep(wait_time)

def unlock(must_wait=False, wait_time=0):
	if(must_wait is True or wait_time is not 0):
		time.sleep(wait_time)
	os.system("adb shell input keyevent 26")
	if(must_wait is True or wait_time is not 0):
		time.sleep(wait_time)

def open_screen(must_wait=False, wait_time=0):
	os.system("adb shell input swipe 540 960 -1000 960")
	if(must_wait is True or wait_time is not 0):
		time.sleep(wait_time)
	lock(must_wait=must_wait, wait_time=wait_time)
	unlock(must_wait=must_wait, wait_time=wait_time)
	os.system("adb shell input swipe 540 960 1000 960")
	

def loop(open_times, must_wait=False, wait_time=0, max_times=10):
	if(open_times < max_times):
		print("Times unlocked: %i"%(open_times))
		lock(must_wait=must_wait, wait_time=wait_time)
		if(must_wait is True or wait_time is not 0):
			time.sleep(wait_time)
		unlock(must_wait=must_wait, wait_time=wait_time)
		if(must_wait is True or wait_time is not 0):
			time.sleep(wait_time)
		open_screen(must_wait=must_wait, wait_time=wait_time)
		if(must_wait is True or wait_time is not 0):
			time.sleep(wait_time)
		open_times += 1
		loop(open_times)
	else:
		print("Max times reached!")

loop(open_times, wait_time=0.9)
