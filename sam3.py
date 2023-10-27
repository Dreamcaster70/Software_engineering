import datetime
import time
def main():
    for i in range(5):
        dt_now = datetime.datetime.now()
        time.sleep(1)
        print(dt_now)
if __name__ == '__main__':
    main()
