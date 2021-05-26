import hazelcast 
import time 
 
client = hazelcast.HazelcastClient( 
    cluster_name="dev", 
    cluster_members=[ 
        "127.0.0.1:6001",
        "127.0.0.1:6002",
        "127.0.0.1:6003"
    ] 
) 
queue = client.get_queue("lab3_2") 
time.sleep(10) 
while True: 
    item = queue.take().result() 
    print('Consumed: ' + str(item)) 
    time.sleep(0.7) 
    if item==-1: 
        print('Consumed -1') 
        break 
 
print('Consumer finished') 