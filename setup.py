import os
from datetime import date
from requests import get
import requests
import shutil


year, _, day = str(date.today()).split("-")
day = day.lstrip('0')
path = f"./{year}/day{day}"

try:
    os.makedirs(path)
except:
    print("Directory already exists for today")
    exit()

shutil.copyfile('template.py', f"{path}/run.py")

open(f"{path}/part1Sample.txt", "x").write("")

open(f"{path}/part2Sample.txt", "x").write("")

cookie = open("./.session", "r").readline().splitlines()[0]

s = requests.session()
s.cookies.set("session", cookie, domain=".adventofcode.com")
response = s.get(f"https://adventofcode.com/{year}/day/{day}/input")

open(f"{path}/input.txt", "x").write(response.text)

print("Creating directory for day" + str(day))