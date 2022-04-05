#!/bin/python3

import subprocess
import argparse

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE='\e[97m'
    BLUE='\x1b[34;40;9;1m'
    C='\x1b[37;40;9;1m'
    RED='\x1b[31;40;9;1m'

link=argparse.ArgumentParser()
link.add_argument('link' ,help='Link of the Video !')
l=link.parse_args()

print("\n" + bcolors.BLUE + "The Link You Entered : " + l.link + "\n")
print(bcolors.RED + "Just Press Enter 4OUR Times To Proceed With 1080p Video With Audio To The Videos Folder !!! \n")

p1=subprocess.run(["yt-dlp","-F",l.link],capture_output=True)

print(bcolors.BOLD + bcolors.C + p1.stdout.decode() + bcolors.ENDC)

print(bcolors.RED + "Just Press Enter 4OUR Times To Proceed With 1080p Video With Audio To The Videos Folder !!! \n")

res=input(bcolors.BLUE + "Just Enter prefered resulution [Exampes: 480 ,720 ,1080 etc. Or Just Press Enter To Enter Video and Audio ID Manually !!!]: " + "\n")
if str(res) == "":
	v=input("Video ID: " + "\n")
	a=input("Audio ID: " + "\n")
else:
	v=""
	a=""

p=input("Download Path : " + "\n\n")

if p == "":
	p="~/Videos"
if v == "":
	v=137
if a == "":
	a=251

f="-f " + str(v)+"  +  "+str(a)
F=str(v)+"  +  "+str(a)

if str(res) == "":
	r=f
else:
	r="-S " + "res:" + str(res)

if str(res) != "":
	print(bcolors.C + "Downloading " + bcolors.RED + str(res) + "p")
else:
	print(bcolors.C + "Format : " + bcolors.RED + F)

print(bcolors.C + "File Wll Be Saved To : " + bcolors.RED + p + bcolors.ENDC + "\n")

subprocess.run(["yt-dlp","-P",p,str(r),"--embed-subs","--write-thumbnail","--write-playlist-metafiles","--embed-metadata","--split-chapters","--write-auto-subs","--progress","--write-description","--restrict-filenames","--cookies-from-browser","brave",l.link])
