#Enable all computers in a text file for PSRemoting
import sys
import os
import subprocess
import time 

fname = "PC.txt"

computers = []
computers = [line.strip() for line in open(fname)]
psexecloc = "psexec.exe"
psargs = "-c -s -n 30 remote.bat"
for computer in computers:
    cmdLine = psexecloc + psargs
    print(cmdLine)
    PID = subprocess.Popen(cmdLine, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    
    for line in PID.stdout:
        print(line)
   


