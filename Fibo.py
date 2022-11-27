

import time
recursive_count = 0
non_recursive_count = 0

def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        recursive[n] = 1
        return 1 
    recursive[n] = fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    global recursive_count
    recursive_count += 1
    return recursive[n]



def fibonacci(n):
    for i in range(2,n):
        global non_recursive_count
        non_recursive_count += 1
        non_recursive[i] = non_recursive[i-1] + non_recursive[i-2]

n = int(input())


recursive = [0] * (n + 1)
start_time = time.time()
fibonacci_recursive(n)
end_time = time.time()
print("Time required for recursive is : ",end_time-start_time)
print(recursive[0:n])
print("recursive Count: ", recursive_count)

non_recursive = [0] * (n)
non_recursive[1] = 1
start_time = time.time()
fibonacci(n)
end_time = time.time()
print("time required for non recursive is : ",end_time-start_time)
print(non_recursive)
print("recursive Count: ", non_recursive_count)




