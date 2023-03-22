## airquality

Timothy Spann

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
