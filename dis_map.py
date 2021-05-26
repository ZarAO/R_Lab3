import hazelcast

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


print("1")
distributed_map = client.get_map("new-distributed-map")
print("2")
print('--created bitch!--')
for i in range(1000):
	print(i)
	distributed_map.set(f"{i+1}", f"value {i+1}")

get_future = distributed_map.get("1000")
get_future.add_done_callback(lambda future: print(future.result()))

print("Map size: ", distributed_map.size().result())	

client.shutdown()
