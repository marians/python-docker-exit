from time import sleep
import sys
import signal

def sigterm_handler(_signo, _stack_frame):
    print("sigterm_handler executed, %s, %s" % (_signo, _stack_frame))
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sigterm_handler)
    try:
        while True:
            print("Doing something")
            sleep(3)
    finally:
        print("Exiting")
