from kafka import KafkaProducer
from faker import Faker
import time

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094']
)

for _ in range(100):
    producer.send('names', fake.name().encode('utf-8'))
time.sleep(20)