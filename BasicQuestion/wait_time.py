import time

attempts = 0
max_attempts = 5
wait_time = 1

while(attempts < max_attempts):
    print("Attempt no:", attempts+1, "Wait time:", wait_time, "seconds")
    time.sleep(wait_time)
    attempts += 1
    wait_time *= 2

    