FROM registry.prod.bbdops.com/common/openjdk:8u252

ENV TZ Asia/Shanghai

WORKDIR /app
ADD target/ai-server-1.0-SNAPSHOT.jar app.jar
EXPOSE 8080
CMD ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "app.jar"]