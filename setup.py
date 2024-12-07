import os
from datetime import date
import requests
import shutil
import argparse

parser = argparse.ArgumentParser("Setup.py")
parser.add_argument('-f', '--force', action='store_true')
parser.add_argument('-d', '--day')
args = parser.parse_args()

year, _, day = str(date.today()).split("-")
day = args.day if args.day else day.lstrip('0')
path = f"./{year}/day{day}"

try:
    os.makedirs(path)
except:
    print(f"Setup already exists for day {day} {year}")
    if not args.force:
        exit()

shutil.copyfile('template.py', f"{path}/run.py")

session = requests.session()
cookie = open("./.session", "r").readline().splitlines()[0]
session.cookies.set("session", cookie, domain=".adventofcode.com")
response = session.get(f"https://adventofcode.com/{year}/day/{day}/input")

failIfExists = "x"
if args.force: failIfExists = "w"

open(f"{path}/input.txt", failIfExists).write(response.text)
open(f"{path}/part1Sample.txt", failIfExists).write("")
open(f"{path}/part2Sample.txt", failIfExists).write("")

print(f"Creating setup for day {day}")