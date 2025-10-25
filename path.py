import math
import random
import time
import threading

stop_flag = False

# Abandon on Enter from user input
def wait_for_enter():
    global stop_flag
    input() # waits for Enter
    stop_flag = True

def read_locations(filename):
    locations = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split()
                if len(parts) == 2:
                    x = float(parts[0])
                    y = float(parts[1])
                    locations.append((x, y))
    
    return locations

def strawman(locations, bestSoFar):
    distance = 0
    landingPad = locations[0]

    for i in range(len(locations)-1):
        distance += computeEuclideanDistance(locations[i],locations[i+1])
        if distance >= bestSoFar:
            return float('inf')

    #for last loc
    distance += computeEuclideanDistance(locations[-1],landingPad)
    if distance >= bestSoFar:
        return float('inf')

    return distance

def strawmanAnytime(locations, bestSoFar):
    global stop_flag
    start_time = time.time()

    while not stop_flag:
        if time.time() - start_time > 300:
            break

        random.shuffle(locations)
        distance = strawman(locations, bestSoFar)
        if distance < bestSoFar:
            bestSoFar = distance
            print(f"{bestSoFar:.1f}")

    return bestSoFar

def computeEuclideanDistance(coord1, coord2):
    return math.sqrt(((coord2[0]-coord1[0])**2) + ((coord2[1]-coord1[1])**2))

def main():
    print("ComputeDronePath")
    print()
    
    filename = input("Enter the name of file: ")
    
    if not filename:
        print("No filename entered.")
        return
    
    locations = read_locations(filename)
    
    if locations is None:
        return
    
    n = len(locations)
    print(f"There are {n} nodes, computing route...")
    print("Shortest Route Discovered So Far")

    threading.Thread(target=wait_for_enter, daemon=True).start()

    bestSoFar = strawman(locations, float('inf'))
    print(f"{bestSoFar:.1f}")
    strawmanAnytime(locations, bestSoFar)

    
if __name__ == "__main__":
    main()