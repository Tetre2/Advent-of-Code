import os
from datetime import date
from requests import get
import requests

year, _, day = str(date.today()).split("-")
day = day.lstrip('0')
path = f"./{year}/day{day}"



try:
    os.makedirs(path)
except:
    print("Directory already exists for today")
    exit()
    
open(f"{path}/run1star.py", "x").write("f = open('input.txt', 'r')\ndata = f.readlines()\n\nt = open('test1star.txt', 'r')\ntestdata = t.readlines()\n\nresults = ''\n\n\n\n\nprint(results)\n")

open(f"{path}/run2star.py", "x").write("f = open('input.txt', 'r')\ndata = f.readlines()\n\nt = open('test2star.txt', 'r')\ntestdata = t.readlines()\n\nresults = ''\n\n\n\n\nprint(results)\n")

open(f"{path}/test1star.txt", "x").write("")

open(f"{path}/test2star.txt", "x").write("")

cookie = open("./.session", "r").readline().splitlines()[0]

s = requests.session()
s.cookies.set("session", cookie, domain=".adventofcode.com")
response = s.get(f"https://adventofcode.com/{year}/day/{day}/input")

open(f"{path}/input.txt", "x").write(response.text)

print("Creating directory for day" + str(day))