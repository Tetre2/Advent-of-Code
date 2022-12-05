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
    
open(f"{path}/run.py", "x").write("f = open('input.txt', 'r')\ndata = f.readlines()\n\n\n\n")

cookie = open("./.session", "r").readline().splitlines()[0]

s = requests.session()
s.cookies.set("session", cookie, domain=".adventofcode.com")
respons = s.get(f"https://adventofcode.com/{year}/day/{day}/input")

open(f"{path}/input.txt", "x").write(respons.text)

print("Creating directory for day" + str(day))