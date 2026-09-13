# *** Intersting work system sleep 🤔😍😍**** Try you and see magic

import time

wait_time = 1
max_retry = 5
attempts = 0
while attempts < max_retry:
    print("Attempt ", attempts + 1, "-wait time",wait_time,)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1

