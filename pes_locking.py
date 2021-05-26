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

distributed_map = client.get_map("pes")
switch = '1'
distributed_map.set(switch, 1)
print('lets go')
for i in range(1000):
    distributed_map.lock(switch)
    temp = distributed_map.get(switch).result()
    time.sleep(0.01)
    temp += 1
    distributed_map.set(switch, temp)
    try:
        distributed_map.unlock(str(i))
    except IllegalMonitorStateError:
        print("error")

print("Done pes locking: ", distributed_map.get(switch).result())

client.shutdown()
