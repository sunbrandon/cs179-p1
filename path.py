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
    print()
    
if __name__ == "__main__":
    main()