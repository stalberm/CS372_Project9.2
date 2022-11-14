import threading
import time

def sum_range(t_id, start, end, results):
  total = sum(range(start, end+1))
  results[t_id] = total

ranges = [
    [10, 20],
    [1, 5],
    [70, 80],
    [27, 92],
    [0, 16]
]

n = len(ranges)

result = [0] * n   # Create an array of `n` zeros
threads = []

for i in range(n):
  t = threading.Thread(target=sum_range, args=(i, *ranges[i], result))
  t.start()
  threads.append(t)

for t in threads:
    t.join()

print(f"{result}\n{sum(result)}")