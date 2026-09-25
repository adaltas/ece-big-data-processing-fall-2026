# %%
from confluent_kafka.admin import AdminClient, NewTopic

# %%
config =  {
  'bootstrap.servers': 'localhost:9092',
}

admin_client = AdminClient(config)

# %%
topic='timer'
admin_client.create_topics(
  [NewTopic(topic, num_partitions=1, replication_factor=1)]
)

# %%
x = admin_client.list_topics()
for  t in x.topics.keys():
  print(t)

# %%
#admin_client.delete_topics([topic])

# %%
