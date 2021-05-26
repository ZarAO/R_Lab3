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

    )
	
distributed_map = client.get_map("opt1")
switch = '1'
distributed_map.put(switch, 1)
print('lets go')
for i in range(1000):
    while True:
        old = distributed_map.get(switch).result()
        time.sleep(0.05)
        new = old + 1
        if distributed_map.replace_if_same(switch, old, new):
            break

print("That`s all!")

print("Done opt locking: ", distributed_map.get(switch).result())

client.shutdown()
