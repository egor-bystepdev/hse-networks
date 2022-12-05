import argparse
import subprocess
import platform
import time

parser = argparse.ArgumentParser(description='PMTUD')
parser.add_argument('-c', help='count of ping by one discovery, by default 1')
parser.add_argument('-v', help='verbose mod', action='store_true')
parser.add_argument('host', help='discovery host')

args = parser.parse_args()

host = args.host
count = args.c
verbose = args.v

if count is None:
    count = 1
elif not count.isnumeric():
    print("c is not number")
    exit(1)
else:
    count = int(count)

if verbose:
    print("VERBOSE MOD ON!")
    print("pings per one discovery", count)
    
def do_request(MTU):
    command = ["ping", host, "-c", str(count), "-D", "-t", "255", "-s", str(MTU)]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if platform.system().lower() == "darwin": # because i do not have linux machine, only macos :) idw add windows support
        if result.returncode == 0:
            return 0, "", ""
        elif result.returncode == 2:
            return 1, result.stdout, result.stderr
        else:
            return 2, result.stdout, result.stderr
    else:
        return result.returncode, result.stdout, result.stderr
    


L = 64 - 28 # 8 bytes is header, minimal reacing frame size
R = 1519 - 28 # minimal not reaching frame size

resultcode, out, err = do_request(L)

if resultcode != 0:
    print("FAILED!!!!")
    print(err)
    exit(1)

while L + 1 < R:
    M = (L + R) // 2
    resultcode, out, err = do_request(M)
    if verbose:
        print("PAYLOAD", M, "Ping output:", resultcode, out, err)
        print("Curr PAYLOAD borders", L, R)
    if resultcode == 0:
        L = M
    elif resultcode == 1:
        R = M
    else:
        print("FAILED!!!!")
        print(err)
        exit(1)
    time.sleep(2)

print("SUCCESS!!!")
print("MAX MTU IS", L + 28)
    

    

