class Street():
    def __init__(self, street_name, B, E, street_length):
        self.street_name = street_name
        self.B = B # starting intersection ID
        self.E = E # ending intersection ID
        # time it takes for a car to cross this road, reaching Intersection E from B
        self.street_length = street_length 
        # variable we added to see the total number of cars that will be crossing this road.
        self.total_cars = 0
        # The following metric is based on an idea to categorize streets on avenues and small streets
        # so that we can schedule their lights accordingly
        self.avenue_metric = 0
        self.is_avenue = False
    
    def __str__(self):
        return f"Starting from intersection {self.B} ending {self.E} & length {self.street_length} total cars {self.total_cars}"   

    def add_car(self):
        self.total_cars += 1

    def update_avenue_metric(self):
        # the more cars inserting the road and the smallest the street length
        # means that more cars will be waiting on the traffic lights
        self.avenue_metric = self.total_cars / self.street_length


class Car():
    def __init__(self, path):
        self.path = path # number of streets
        self.dc = {}
        for street in path:
            self.dc[street] = 0

    def __str__(self):
        return ', '.join(self.path)

class Intersection():
    def __init__(self, i):
        self.i = i
        self.cars_per_incoming_street = {}
        self.cars_per_outgoing_street = {}
        self.traffic_lights = {}
        self.total_cars = 0

    def add_cars_per_incoming_street(self,street_name, total_cars):
        self.cars_per_incoming_street[street_name] = total_cars

    def add_cars_per_outgoing_street(self,street_name, total_cars):
        self.cars_per_outgoing_street[street_name] = total_cars
        
    # this function sets all traffic lights to one if there is at least one car in this road.
    # also it sorts the traffic lights based on the number of cars that use them. This matters because 
    # the final order determines which street will start becoming green earlier.
    def assign_all_one(self):

        self.total_cars = sum(self.cars_per_incoming_street.values())
        if self.total_cars == 0:
            return

        self.cars_per_incoming_street = {k: v for k, v in sorted(self.cars_per_incoming_street.items(), key=lambda item: item[1], reverse=True)}

        for street in self.cars_per_incoming_street.keys():
            if self.cars_per_incoming_street[street] > 0:
                self.traffic_lights[street] = 1
                
                
    def assign_time_percentage(self):
        self.total_cars = sum(self.cars_per_incoming_street.values())
        if self.total_cars == 0:
            return
        
        percentages = {}
        for street in self.cars_per_incoming_street.keys():
            if self.cars_per_incoming_street[street] > 0:
                percentages[street] = self.cars_per_incoming_street[street] / self.total_cars
        
        # find the min percentage that is not equal to 0
        # assuming we have percentages 0.2, 0.3, 0.5 then factor will be 1/0.2 = 5
        factor = 1 / min(percentages.values())
        
        # sort percentages
        percentages = {k: v for k, v in sorted(percentages.items(), key=lambda item: item[1],reverse = True)}
        
        # so we set traffic lights equal to 1.0, 1.5, 2.5 which become 1, 1, 2 since we are converting them to ints
        for street in percentages.keys():
            p = percentages[street]
            self.traffic_lights[street] = max(1,int(p*factor))
