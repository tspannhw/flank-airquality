## flank-airquality

Timothy Spann's demo for sending airquality data from Spring-Kafka Java to Kafka.   And from NiFi to Kafka from REST.


![FLaNK Diagram](https://raw.githubusercontent.com/tspannhw/flank-airquality/main/images/airqualityflank2.png)


### Demo


![Maven Build](https://raw.githubusercontent.com/tspannhw/flank-airquality/main/images/mavenbuild.png)

![Spring Run](https://raw.githubusercontent.com/tspannhw/flank-airquality/main/images/springrun.png)

![AQ Produced Run](https://raw.githubusercontent.com/tspannhw/flank-airquality/main/images/airqualityproducedrun.png)

![AQ Schema](https://raw.githubusercontent.com/tspannhw/flank-airquality/main/images/airqualityschema.png)

![SMM Kafka Records](https://raw.githubusercontent.com/tspannhw/flank-airquality/main/images/smmkafkarecords.png)




### Setup

* Visual Code with Spring & Java 11
* Set an environment variable with your api key code from airnow
* Point to your Apache Pulsar cluster, if you are using StreamNative cloud I have SSL and configuration in the config class

### Configuration

````

airnowapi.api.key=${API_KEY}
airnowapi.url=https://www.airnowapi.org/aq/observation/zipCode/current
airnowapi.uri=/?format=application/json&distance=250&zipCode=
airnowapi.key.name=&API_KEY=
zipcodes=08520,94027,02199,11962,94957,90402,94301,07070,90265,90272,10013,10007,94123,77449,11368,60629,79936,75034
topic.name=airquality
producer.name=airqualitykafka
send.timeout=60
security.mode=off
server.port=8999
#kafka
kafka.bootstrapAddress=kafka:9092
kafka.topic.name=airquality
logging.level.root=INFO
logging.level.dev.datainmotion.airquality=INFO


````

### Build

mvn package


### Run

mvn spring-boot:run

### Environment Variables

export API_KEY=<valueFromYourthing>

### Producing data

````

// send as json string

        UUID uuidKey = UUID.randomUUID();
        ProducerRecord<String, String> producerRecord = new ProducerRecord<>(topicName,
                uuidKey.toString(),
                DataUtility.serializeToJSON(message));
       kafkaTemplate.send(producerRecord);

````

### Consume AirQuality Topic

See:   consumeairquality.py

### Consume OpenAQ Topic

See:   consumeopenaq.py


##### 1️⃣  Air Quality References

Let's use the new Spring to read a ton of Air Quality data for the area.  
This is a REST feed, no extra equipment needed.

* https://github.com/tspannhw/spring-pulsar-airquality
* https://github.com/tspannhw/airquality
* https://github.com/tspannhw/airquality-kafka-consumer
* https://github.com/tspannhw/airquality-mqtt-consumer
* https://github.com/tspannhw/FLiPN-AirQuality-REST
* https://medium.com/@tspann/timeplus-plus-pulsar-is-pure-perfection-a1a4d253031f
* https://github.com/tspannhw/pulsar-airquality-timeplus
* https://github.com/tspannhw/FLiPN-AirQuality-Checks
* https://github.com/tspannhw/airquality-datastore
* https://github.com/tspannhw/airquality-amqp-consumer
* https://kafka-python.readthedocs.io/en/master/usage.html
