from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('airquality',auto_offset_reset='earliest', enable_auto_commit=False,
                         group_id='aq-group',
                         bootstrap_servers=['kafka:9092'])

print("Consumer")
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
