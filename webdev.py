import urllib.request
import sys
import time
import os
import json
import math

#returns the string contents of the page at url, or "" if there is an error
def read_url(url):
	fail_count = 0
	sleep_time = 0.01
	
	while fail_count < 10:
		time.sleep(sleep_time)
		try:
			fp = urllib.request.urlopen(url)
			mybytes = fp.read()
			mystr = mybytes.decode(sys.stdout.encoding)
			fp.close()
			return mystr
		except:
			fail_count += 1
			sleep_time = sleep_time * 2.5
			print("Failed to read " + url + "(#" + str(fail_count) + "), sleeping for " + str(sleep_time) + "seconds before retrying...")
	print("COULD NOT READ THE URL!")
	return ""