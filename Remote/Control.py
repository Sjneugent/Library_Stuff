#Enable all computers in a text file for PSRemoting
#Control.py (-e | -d) txtfile.txt
import sys
import os
import subprocess

def main(argv):
  file_name = ''
  script_name = ''
  #python Test.py <computerListFile> -e/-d
  #psexec \\ComputerName psargs -e/-d (-e = enable, -d= disable)
  
  psexec = "psexec.exe "
  psargs = "-c -s -d  "
  
  computers = []
  
  #You can only have two arguments.  enable or disable AND a valid text file
  if(len(argv) != 2):
      print("Usage: python Test.py -e|-d <location of text File>")
      sys.exit()
  #if enabled, select remote.bat
  if(argv[0] == "-e"):
      script_name = "remote.bat"
  #if disabled, select disable remote
  elif(argv[0] == "-d"):
      script_name = "DisableRemote.bat"
  else:
      print("Usage: python Test.py -e|-d <location of text File>")
      sys.exit()
  file_name = argv[1]
  #make sure it's a real file
  if(os.path.isfile(file_name) ==  False):
    print(file_name+" is not a valid file")
    sys.exit()

  #Go through the text file line by line an put it into a list
  computers = [line.strip() for line in open(file_name)]

  
  for computer in computers:
	  #psexec.exe \\Computer -c -s -d remote/DisableRemote.bat
      cmdLine = psexec +"\\\\"+computer+ " " + psargs + " " + script_name
      #print(cmdLine)
      PID = subprocess.Popen(cmdLine, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    
	  #Uncomment out those two lines if you want to see the response it gets back from psexec
      #for line in PID.stdout:
         # print(line)
   
if __name__ == "__main__":
  main(sys.argv[1:])

