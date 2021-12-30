from helpers import Street, Car, Intersection
from parse import parse_file
from submit import submit
# this function removes the cars whose total duration path exceeds the total time of the simulation
# we compute the path's total duration by parsing streets one by one for every car and then going to the
# dictionary streets to get the street_length
# This operation should not be so much expensive.
def excluding_cars():
    i = 0
    while i < len(cars):
        c = cars[i]
        total_duration = 0

        for street_name in c.path[:]:

            total_duration += streets[street_name].street_length

        if total_duration > D:
            print(f"Car {i} discarded")
            cars.pop(i)
        i = i + 1
                                
# for every road in the path of a car we increase total_cars 
def compute_cars_per_street():
    for c in cars:
        for street_name in c.path[:]:
            streets[street_name].total_cars += 1
                
filenames = ['a', 'b', 'c', 'd', 'e', 'f']
for file in filenames:
    input_filename = "./input/" + file + ".txt"
    output_filename = "./output/" + file + "_out.txt"

    D, I, S, V, F, streets, cars = parse_file(input_filename)
    print("-"*100)
    print(f"Filename: {file}")
    print(f"Duration: {D}, \nTotal Intersections: {I}, \nTotal Streets: {S}")
    print(f"Total Vehicles: {V}, \nScore for every car: {F}")

    excluding_cars()
    compute_cars_per_street()
    
    intersections = {}
    for name in streets.keys():
        i = streets[name].B
        if i not in intersections:
            intersections[i] = Intersection(i)
            
        intersections[i].add_cars_per_outgoing_street(name, streets[name].total_cars)
            
        i = streets[name].E
        if i not in intersections:
            intersections[i] = Intersection(i)
        intersections[i].add_cars_per_incoming_street(name, streets[name].total_cars)
      
    final_intersections = {}
    for i in intersections.keys():
        
#         intersections[i].assign_all_one()
        intersections[i].assign_time_percentage()
        
        if intersections[i].total_cars > 0:
            final_intersections[i] = intersections[i]
        

    submit(output_filename, final_intersections)
