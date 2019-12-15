import time

times = time.strftime("%Y-%m-%d", time.localtime())
for _ in range(2):
    filename = time.time()
    print(filename)