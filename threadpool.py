
import concurrent.futures

def works():
    print("hai")

pool=concurrent.futures.ThreadPoolExecutor(max_workers=3)

pool.submit(works)
pool.submit(works)
pool.submit(works)

pool.shutdown(wait=True)
print("main thread")