import heapq

def insert(heap, x):
    heapq.heappush(heap,x)
    return f"insert {x}"

def getMin(heap, x):
    log_operations = []
    if len(heap) ==0:
        log_operations.append(insert(heap,x))
    while len(heap) >0 and heap[0] <x:
        op = removeMin(heap)
        log_operations.append(op[0])
    if len(heap) ==0 or heap[0] > x:
        log_operations.append(insert(heap,x))
    log_operations.append(f"getMin {x}")
    return log_operations

def removeMin(heap):
    log_operations = []
    if len(heap)==0:
        log_operations.append(insert(heap,0))
    heapq.heappop(heap)
    ouput = "removeMin"
    log_operations.append(ouput)
    return log_operations
        

n_log = int(input())
h = []
heapq.heapify(h)
output_log = []
for cmd in range(n_log):
    commands = input().strip().split()
    if commands[0] == "insert":
        val = int(commands[1])
        output_log.append(insert(h, val))
    elif commands[0] == "getMin":
        val = int(commands[1])
        for op in getMin(h, val):
            output_log.append(op)
    else:
        for op in removeMin(h):
            output_log.append(op)

print(len(output_log))
for log in output_log:
    print(log)



        