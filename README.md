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

Docker build a image from a files configuration.

```
docker build -t docker-hadoop docker-hadoop
```

Docker remove all stopped containers, dangling images, and unused network. Use the -f or --force option to bypass the prompt. By default, the command doesn’t remove unused volumes to prevent losing important data. To remove all unused volumes, pass the --volumes option

```
docker system prune
```

Docker remove image (f:force)

```
docker image rmi -f hadoop-docker
```

Starting a "centos" container.

```
docker start "centos".
```

Listing all containers.

```
docker ps -a
```

Docker online: https://labs.play-with-docker.com

## Hadoop Configuration in Docker

## Spark Configuration in Docker

## Elasticsearch configuration in Docker

## Logstash configuration in Docker

## Kibana configuration in Docker

## Architectures in AWS

- https://d1.awsstatic.com/events/reinvent/2019/Building_on_AWS_The_architecture_of_the_Siemens_MindSphere_platform_MFG202.pdf

## Dataframes with Javascript 

- https://stackoverflow.com/questions/30610675/python-pandas-equivalent-in-javascript

## MongoDB 
- https://riptutorial.com/Download/mongodb-es.pdf
- https://riptutorial.com/mongodb/example/23688/sharding-environment-setup
