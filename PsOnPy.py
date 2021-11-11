import subprocess
import sys
import os


def copy_memory(targetPath, tmpFile):
    command = "powershell -ExecutionPolicy ByPass -File Usb_File_Copy.ps1 -TargetFolder "+\
                  targetPath + " -ResultFile " + tmpFile 
    print(command)
    powerShellResult = subprocess.run(command, stdout=subprocess.PIPE)

