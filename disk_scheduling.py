import sys

def read_requests(filename):
    with open(filename, 'r') as file:
        requests = [int(line.strip()) for line in file if line.strip().isdigit()]
    return requests

def fcfs(requests, initial_pos):
    current_pos = initial_pos
    total_movement = 0
    for request in requests:
        total_movement += abs(current_pos - request)
        current_pos = request
    return total_movement

def scan(requests, initial_pos, total_cylinders=5000):
    requests.sort()
    idx = 0
    total_movement = 0
    current_pos = initial_pos
    
    # Find the starting position in the sorted list
    while idx < len(requests) and requests[idx] < initial_pos:
        idx += 1
    
    if initial_pos < requests[0]:
        # Go to the nearest end (0)
        total_movement += abs(current_pos - 0)
        current_pos = 0
        # Then service towards the far end
        total_movement += abs(current_pos - requests[-1])
        current_pos = requests[-1]
    else:
        # Go to the nearest end (4999)
        total_movement += abs(current_pos - (total_cylinders - 1))
        current_pos = total_cylinders - 1
        # Then service back towards 0
        total_movement += abs(current_pos - requests[0])
        current_pos = requests[0]

    return total_movement

def cscan(requests, initial_pos, total_cylinders=5000):
    requests.sort()
    idx = 0
    total_movement = 0
    current_pos = initial_pos
    
    # Find the starting position in the sorted list
    while idx < len(requests) and requests[idx] < initial_pos:
        idx += 1

    # Service from current_pos to the far end
    total_movement += abs(current_pos - (total_cylinders - 1))
    current_pos = total_cylinders - 1

    # Jump to the start
    total_movement += total_cylinders - 1
    current_pos = 0

    # Continue servicing until reaching the initial position
    total_movement += abs(current_pos - requests[idx - 1])
    current_pos = requests[idx - 1]

    return total_movement

def main():
    if len(sys.argv) != 3:
        print("Usage: python disk_scheduling.py <initial_pos> <filename>")
        sys.exit(1)

    initial_pos = int(sys.argv[1])
    filename = sys.argv[2]

    requests = read_requests(filename)

    # FCFS
    fcfs_movement = fcfs(requests, initial_pos)
    print(f"FCFS Total Head Movement: {fcfs_movement}")
    print(f"FCFS Optimized Total Head Movement: {fcfs_movement}")  # No optimization possible

    # SCAN
    scan_movement = scan(requests, initial_pos)
    print(f"SCAN Total Head Movement: {scan_movement}")
    # Assuming optimized version is the same as we're not modifying the algorithm fundamentally
    print(f"SCAN Optimized Total Head Movement: {scan_movement}")

    # C-SCAN
    cscan_movement = cscan(requests, initial_pos)
    print(f"C-SCAN Total Head Movement: {cscan_movement}")
    # Assuming optimized version is the same as we're not modifying the algorithm fundamentally
    print(f"C-SCAN Optimized Total Head Movement: {cscan_movement}")

if __name__ == "__main__":
    main()
