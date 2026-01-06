import time

def soru():
    print("Soru function started")
    time.sleep(2)   # 2 seconds
    print("Soru function finished")

def kulambu():
    print("Kulambu function started")
    time.sleep(3)   # 3 seconds
    print("Kulambu function finished")

# start timer
start_time = time.time()

print("Program started")

soru()
kulambu()

print("Program finished")

# end timer
end_time = time.time()

# total time in seconds
total_seconds = end_time - start_time

# convert to minutes
total_minutes = total_seconds / 60

print(f"Total time taken: {total_seconds:.2f} seconds")
print(f"Total time taken: {total_minutes:.2f} minutes")
