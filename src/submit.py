from helpers import Street, Car, Intersection
from parse import parse_file

def submit(filename, intersections):
    with open(filename, 'w') as f:
        
        total_intersections = len(intersections)
        
        f.write(str(total_intersections) + "\n")

        for i in intersections.keys():
            inter = intersections[i]
            # print(inter.traffic_lights)
            # if inter.total_cars == 0:
            #     continue
            f.write(f"{inter.i}\n")
            f.write(f"{len(inter.traffic_lights)}\n")
            for street in inter.traffic_lights.keys():
                f.write(f"{street} {inter.traffic_lights[street]}\n")
#                 f.write(f"{street} {1}\n")

def submit_all_one():

    filenames = ['a', 'b', 'c', 'd', 'e', 'f']
        
    for file in filenames:
        print(file)
        input_filename = "./input/" + file + ".txt"
        output_filename = "./output/" + file + "_out.txt"
        D, I, S, V, F, streets, cars = parse_file(input_filename)


        intersections = {}


        for name in streets.keys():
            int_id = streets[name].E
            if int_id not in intersections:
                intersections[int_id] = ([name], 0)
            else:
                intersections[int_id][0].append(name)
        
        for c in cars:
            for street_name in c.path:
                intersections[streets[street_name].E][0] += 1

        with open(output_filename, 'w') as f:
            total_intersections = len(intersections)

            f.write(str(total_intersections) + "\n")