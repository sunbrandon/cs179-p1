import math
import random

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

def strawman(locations):
    distance = 0
    landingPad = locations[0]

    for i in range(len(locations)-1):
        distance += computeEuclideanDistance(locations[i],locations[i+1])

    #for last loc
    distance += computeEuclideanDistance(locations[-1],landingPad)
    return distance

def strawmanAnytime(locations, bestSoFar):
    while (1): #fix to abandon on enter
        random.shuffle(locations)
        distance = strawman(locations)
        if (distance < bestSoFar):
            bestSoFar = distance
            print(bestSoFar)


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

    bestSoFar = strawman(locations)
    print(bestSoFar)
    strawmanAnytime(locations, bestSoFar)

    
if __name__ == "__main__":
    main()