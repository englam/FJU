import random, csv

class Packet:
    def __init__(self,arrival_date,service_start,service_time):
        self.arrival_date = arrival_date
        self.service_start_date = service_start
        self.service_time = service_time
        self.service_end_date = self.service_start_date + self.service_time
        self.wait = self.service_start_date - self.arrival_date


def neg_exp(input_lambda):
        return random.expovariate(input_lambda)


def Queue_simulation(lambd=False,mu=False,simulation_time=False):
    if not lambd:
        lambd = input("Please input arrival rate: ")
    if not mu:
        mu = input("Please input Service rate")
    if not simulation_time:
        simulation_time = input("Please input simulation time: ")

    t = 0

    Packets = []


    while t < simulation_time:
        if len(Packets) == 0:
            arrival_date = neg_exp(lambd)
            print ("first arrival time : ",arrival_date,"\n")
            service_start_date = arrival_date
        else:
            arrival_date+=neg_exp(lambd)
            service_start_date = max(arrival_date,Packets[-1].service_end_date)
        service_time = neg_exp(mu)

        Packets.append(Packet(arrival_date,service_start_date,service_time))

        t = arrival_date


    Waits = [a.wait for a in Packets]



    Mean_Wait = sum(Waits) / len(Waits)


    System_Times = [a.wait + a.service_time for a in Packets]


    Mean_Time = sum(System_Times) / len(System_Times)

    Service_Times = [a.service_time for a in Packets]
    Mean_Service_time = sum(Service_Times) / len(Service_Times)

    Utilisation = sum(Service_Times) / t


    T = sum(System_Times) / len(Packets)


    print ("")
    print ("Summary Results:")
    print ("")
    print ("Number of Packets: " , len(Packets))
    print ("Average Service time: ", Mean_Service_time)
    print ("wait time", Mean_Wait)
    print ("Average Total time", Mean_Time)
    print ("Utilisation: ", Utilisation)

if __name__ == '__main__':
    Queue_simulation(1,2,10)
    Queue_simulation(0.25, 45, 10)
    #Queue_simulation(10, 9, 10)
