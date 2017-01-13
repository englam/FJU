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



    System_Times = [a.wait + a.service_time for a in Packets]
    service_start_date = [a.service_start_date for a in Packets]
    service_end_date = [a.service_end_date for a in Packets]
    Mean_Time = sum(System_Times) / len(System_Times)

    Service_Times = [a.service_time for a in Packets]
    Mean_Service_time = sum(Service_Times) / len(Service_Times)

    Utilisation = sum(Service_Times) / t

    print ("packets : ", len(Packets))



if __name__ == '__main__':
    Queue_simulation(0.25,10,10000)

