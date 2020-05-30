#!/usr/bin/python
#A System Information Gathering Script
import subprocess

def uname():
    #Command 1
    uname = 'uname'
    uname_arg = '-a'
    print("Gathering system information with %s command:\n" % uname)
    subprocess.call([uname, uname_arg])
    
def diskspace():    
    #Command 2
    diskspace = 'df'
    diskspace_arg = '-h'
    print("Gathering diskspace information %s command:\n" % diskspace)
    subprocess.call([diskspace, diskspace_arg])

def main():
    uname()
    diskspace()

if __name__ == "__main__":
    main()
