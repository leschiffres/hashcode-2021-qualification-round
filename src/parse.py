from helpers import Street, Car

def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

        D, I, S, V, F = [int(w) for w in lines[0].strip().split()]
        
        streets = {}
        cars = []
        
        for i in range(1, S+1):
            B, E, street_name, street_length = [w for w in lines[i].strip().split()]
            B = int(B)
            E = int(E)
            street_length = int(street_length)
            
            streets[street_name] = Street(street_name, B, E, street_length)
            
        for i in range(S+1, len(lines)): 
             cars.append(Car([w for w in lines[i].strip().split()[1:]]))
            
            
    return D, I, S, V, F, streets, cars