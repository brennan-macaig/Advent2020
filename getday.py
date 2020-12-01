from environ import header
import sys
import browser_cookie3
import requests

baseURL = "https://adventofcode.com/2020/day/"
def get_data(day):
    print("get: fetching cookie")
    cj = browser_cookie3.chrome()
    print("get: waiting for response...")
    r = requests.get(f"https://adventofcode.com/2020/day/{day}/input", cookies = cj)
    
    with open(f"input/day{day}.txt","w") as f:
        f.write(r.text)
    print("done!")

if len(sys.argv) != 2:
    print("usage: getday <day>")
else:
    arg1 = sys.argv[1]
    if not (str(arg1).isnumeric()):
        print("day must be a number")
    else:
        get_data(int(arg1))
