#! /usr/bin/env python3
import os
from os import sys
from os import system

if os.geteuid() != 0:
    print("\033[31mError: \033[0mScript must be run as root")
    exit()

if not os.path.exists("/usr/bin/runit"):
    print("\033[31mError: \033[0mRunit isn't installed")
    exit()

def startProcess(s):
    if os.path.exists(f"/etc/sv/{s}"):
        print(f"\033[35mAlert: \033[0mStarting \033[34m/etc/sv/{s}\033[0m")
        system(f"sudo sv up /etc/sv/{s}")
        
def enableProcess(s):
    if os.path.exists(f"/etc/sv/{s}"):
        if os.path.exists(f"/var/service/{s}"):
            print(f"\033[35mAlert: \033[33m{s}\033[0m is already available in \033[34m/var/service\033[0m... Want to overwrite?:")
            inp = str(input("\033[36m[y/n]: \033[0m"))
            if inp == "yes" or inp.__contains__("ye") or inp == "y":
                print(f"\033[35mAlert: \033[0mCreating symlink \033[34m/etc/sv/{s}\033[0m -> \033[33m/var/service/{s}\033[0m")
                system(f"sudo ln -s /etc/sv/{s} /var/service")
            elif inp == "no" or inp.__contains__("no") or inp == "n":
                print(f"\033[35mAlert \033[0mUser has abandoned symlink process as directory exists")
            else:
                print("\033[31mError: \033[0mExiting process due to unexpected input")
        else:
            print(f"\033[35mAlert: \033[0mCreating symlink \033[34m/etc/sv/{s}\033[0m -> \033[33m/var/service/{s}\033[0m")
            system(f"sudo ln -s /etc/sv/{s} /var/service")
    else:
        print(f"\033[31mError: \033[0mServoce \033[34m{s}\033[0m not available in \033[35m/etc/sv/\033[0m")

def disableProcess(s):
    if os.path.exists(f"/var/service/{s}"):
        if not os.path.exists(f"/etc/sv/{s}"):
            print("\33[35mAlert: \033[0msymlink will be removed from \033[35m/var/service\033[[0m but it doesn't exist from \033[34m/etc/sv\033[0m. Continue?:")
            inp = str(input("\033[35m[y/n]: \033[0m"))
            if inp == "y" or inp == "yes" or inp.__contains__("ye"):
                system(f"sudo rm -rf /var/service/{s}")
            elif inp == "n" or inp == "no" or inp.__contains__("no"):
                print("\033[35mAlert: \033[0mUser has aborted `symunlink` process")
            else:
                print("\033[31mError: \033[0mUnexpected input.... Automatically exiting") 
        else:
            print(f"\033[35mAlert: \033[0mremoving symlink \033[34m{s}\033[0m from \033[35m/var/service\033[0m")
            system(f"sudo rm -rf /var/service/{s}")
    elif not os.path.exists(f"/var/service/{s}"):
        print(f"\033[31mError:\033[0m symlink \033[34m{s}\033[0m not available in \033[35m/var/service\033[0m")
def listProcesses(s):
    if s == "etc":
        system("ls /etc/sv")
    elif s == "var":
        system("ls /var/service")

def main():   
    if len(sys.argv) > 1:
        for x in range(len(sys.argv)):
            if sys.argv[x] == "start":
                try:
                    x = sys.argv[x+1]
                    startProcess(x)
                except:
                    print("\033[31mError: \033[0mNot specified which service to start")
            elif sys.argv[x] == "enable":
                try:
                    x = sys.argv[x+1]
                    enableProcess(x)
                except:
                    print("\033[31mError: \033[0mNot specified which service to enable")
            elif sys.argv[x] == "disable":
                try:
                    x = sys.argv[x+1]
                    disableProcess(x)
                except:
                    print("\033[31mError: \033[0mNot specified which service to disable")
            elif sys.argv[x] == "list":
                try:
                    a = sys.argv[x+1]
                    if a == "all":
                        system("ls /etc/sv/")
                    elif a == "enabled":
                        system("ls /var/service/")
                    else:
                        system("ls /etc/sv")
                except:
                    system("ls /etc/sv")

    else:
        print("\033[31mError: \033[0mNo operation has been defined")
        exit()

main()