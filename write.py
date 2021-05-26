import hazelcast
import time

if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
        cluster_name="dev",
        cluster_members=[
            "127.0.0.1:6001",
            "127.0.0.1:6002",
            "127.0.0.1:6003"
        ],
		lifecycle_listeners=[
			lambda state: print("Lifecycle event >>>", state),
		]

    )


my_map = client.get_queue("lab3_2").blocking() 
 
for i in range(100): 
    time.sleep(0.2) 
    my_map.put(f"{i}")

client.shutdown()
