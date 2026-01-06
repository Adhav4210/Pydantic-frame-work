import asyncio
import time

async def soru():
    print("Soru function started")
    await asyncio.sleep(2)   # non-blocking sleep
    print("Soru function finished")

async def kulambu():
    print("Kulambu function started")
    await asyncio.sleep(3)   # non-blocking sleep
    print("Kulambu function finished")

async def main():
    start_time = time.time()

    print("Program started")

    # run both functions concurrently
    await asyncio.gather(
        soru(),
        kulambu()
    )

    print("Program finished")

    end_time = time.time()

    total_seconds = end_time - start_time
    total_minutes = total_seconds / 60

    print(f"Total time taken: {total_seconds:.2f} seconds")
    print(f"Total time taken: {total_minutes:.2f} minutes")

# start async program
asyncio.run(main())
