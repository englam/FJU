import random

class Packet:
    def __init__(self,arrival_date,service_start,service_time):
        self.arrival_date = arrival_date
        self.service_start_date = service_start
        self.service_time = service_time
        self.service_end_date = self.service_start_date + self.service_time
        self.wait = self.service_start_date - self.arrival_date
        self.timePacketProdcut = self.service_end_date - self.service_start_date


def neg_exp(input_lambda):
    if input_lambda == 0.02:
        return 0.02
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
            service_start_date = arrival_date
        else:
            arrival_date+=neg_exp(lambd)
            service_start_date = max(arrival_date,Packets[-1].service_end_date)
            #service_start_date = Packets[-1].service_end_date
        service_time = neg_exp(mu)
        Packets.append(Packet(arrival_date,service_start_date,service_time))

        #t = arrival_date
        t = Packets[-1].service_end_date
        #print ("t time : ",t,"\n")



    System_Times = [a.wait + a.service_time for a in Packets]
    #print ("System_Times ",sum(System_Times))

    Service_Times = [a.service_time for a in Packets]
    Service_Times_sum = sum(Service_Times)

    service_start_date = [a.service_start_date for a in Packets]
    service_end_date = [a.service_end_date for a in Packets]

    timePacketProdcut = [a.timePacketProdcut for a in Packets]


    print ("packets : ", len(Packets))
    end_Times = [a.service_end_date for a in Packets]
    #print ("end time", end_Times[-1])


    Utilisation = sum(Service_Times) / t
    print ("sum service times : ", sum(Service_Times))
    print ("Utilisation: ", Utilisation)

    print (end_Times[-1])


    #N1 = (sum(timePacketProdcut) /end_Times[-1] )
    N =  sum(timePacketProdcut) / simulation_time
    N = N / (1-N)
    T = sum(System_Times) / len(Packets)

    print ("N: ", N)
    print ("T: ", T)



def run_queue_homework(rate,u):
    print("---------Start ---------", u, "------------------------", "\n")
    for i in rate:
        Queue_simulation(i,u, 10000)

    print ("---------finish ---------",u,"------------------------","\n")

if __name__ == '__main__':
    a = [0.05,1,3,5,7 ,9]
    b = [0.1,2,6,10,14,18]
    c = [0.25, 5, 15, 25, 35, 45]
    run_queue_homework(a , 10)
    run_queue_homework(b , 20)
    run_queue_homework(c , 50)
    run_queue_homework(c , 0.02)


