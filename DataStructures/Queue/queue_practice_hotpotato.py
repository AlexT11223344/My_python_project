from queue_1 import *


def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)
        while sim_queue.size() > 1:
            for i in range(num):
                sim_queue.enqueue(sim_queue.dequeue())
            sim_queue.dequeue()
        return sim_queue.dequeue()

l_name = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(hot_potato(l_name, 7))