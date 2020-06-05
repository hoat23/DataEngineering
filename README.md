# DATA ENGINEERING

This repository is for a quick installation and configuration of software using Docker.

## Docker commands

Steps to create a container Docker.

<div align="center">
<img src="https://github.com/hoat23/DataEngineering/blob/master/img/crating-a-docker-container.png" width="800" align="center"/>
</div>

- Create an image from a Dockerfile using docker build.

- Create a container layer from an image, use the command docker create.

- Finally, after you have launched a container from an existing image, you start its service and run the application.

<div align="center">
<img src="https://github.com/hoat23/DataEngineering/blob/master/img/img01.png" width="400" align="center"/>
</div>

Listing all images
```
docker images ps
```

Docker run "centos". Running a "centos" image.  

```
docker run -it centos
```

Starting a "centos" container.

```
docker start "centos".
```

Listing all containers.
```
docker ps -a
```
## Hadoop Configuration in Docker

## Spark Configuration in Docker

## Elasticsearch configuration in Docker

## Logstash configuration in Docker

## Kibana configuration in Docker
