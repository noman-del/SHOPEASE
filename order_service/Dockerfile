FROM openjdk:11-jre-slim
VOLUME /tmp
COPY target/order-service-1.0-SNAPSHOT.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
