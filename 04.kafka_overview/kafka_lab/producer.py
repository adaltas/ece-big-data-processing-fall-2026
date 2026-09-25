# %%
import socket
import time
from confluent_kafka import Producer
from datetime import datetime, timedelta


# %%
print(datetime.now().strftime("%H:%M"))
# %%
conf = {'bootstrap.servers': 'localhost:9092',
        'client.id': socket.gethostname()}

producer = Producer(conf)

# %%
topic='timer'
message='The time is now '
# %% Streaming Query
duration = 5 # Streaming window in minutes
start_time = datetime.now() # Current clock time
stop_time = start_time + timedelta(minutes=duration) #start+duration=stop

while datetime.now() < stop_time:
  time_now = datetime.now().strftime("%H:%M:%S")
  producer.produce(
    topic=topic,
    value=message + time_now
  )
  print(message + time_now)
  time.sleep(1)

producer.flush()
producer.close()
