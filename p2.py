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

distributed_map = client.get_map("no_lock_map")
switch = '1'
distributed_map.put(switch, 1)
print('lets go')

for i in range(1000):
    if i % 100 == 0:
        pass
    old_val = distributed_map.get(switch).result()
    time.sleep(0.01)
    new_val = old_val + 1
    distributed_map.put(switch, new_val)
print('--YESSS--')
print("Done no locks results: ", distributed_map.get(switch).result())

client.shutdown()
