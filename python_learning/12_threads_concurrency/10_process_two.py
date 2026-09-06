
import time
from multiprocessing import Process


def cpu_heavy():
    print("Crunching some numbers....")
    total = 0
    for _ in range(10**9):
        total += 1
    print("DONE ✅ ")


start = time.time()
processes = [Process(target=cpu_heavy) for _ in range(2)]

# The problem is that with spawn, each new process starts a fresh 
# Python interpreter and loads your program again.
# for this we use the name variable that checks calls is from main program

if __name__ == "__main__":
    [p.start() for p in processes]
    [p.join() for p in processes]

    print(f"Time taken: {time.time() - start:.2f} seconds")
