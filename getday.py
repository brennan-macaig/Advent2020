from urllib.request import Request, urlopen, HTTPError as httperr
from environ import header

baseURL = "https://adventofcode.com/2020/day/"
def get_data(day):
    print("get: waiting for response...")
    req = Request(baseURL + str(day) + "/input")

    req.add_header("cookie", header)
    try:
        content = urlopen(req).read().decode('utf-8')
    except httperr as err:
        print("http error - " + str(err.reason))
        return 1
    
    filename = "inputs/day" + str(day) + ".txt"
    f = open(filename, "w")
    f.write(content)
    f.close()
    print("done. wrote " + str(len(content)) + " chars to " + filename)

if len(sys.argv) != 2:
    print("usage: getday <day>")
else:
    arg1 = sys.argv[1]
    if not (str(arg1).isnumeric()):
        print("day must be a number")
    else:
        get_data(int(arg1))
