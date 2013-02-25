#!/usr/bin/python2
import subprocess
import os
import sys
import subprocess

print len(sys.argv)
if len(sys.argv) == 3:
		search = sys.argv[1]
		directory = sys.argv[2]
		count = len(directory)
		if directory[count -1] != "/":
			directory = directory + "/"
else:
	print "Try: ./linkcheck.py searchquery directory"
	print "Where searchquery is a word to grep for in the name of the link"
	print "And where directory is the directory to search for links in"
	sys.exit()

os.system("touch fi.file")

linkz = subprocess.Popen(['ls','msf*'], stdout=subprocess.PIPE, shell=True)
(out, err) = linkz.communicate()
links = out
f = open("fi.file","a")
f.write(links)
f.close()

f = open("fi.file","r")
for link in f:
       if search in link:
		linkloc = directory + link
		print "\n" + linkloc
		os.system("readlink " + linkloc)
		print "\n"
f.close()
os.system("rm ./fi.file")           
