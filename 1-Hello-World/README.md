# Hello world in Docker
To get this example running, follow these instructions:

1. Open a Powershell, navigate to the folder that contains the Dockerfile, and insert the following command:
```
docker build -t hello-world .
```
This command builds an image with the tag hello-world.

2. Once finished step one, run the following command in order to run the containerized script:
```
docker run --name the-container hello-world
```
The --name option gives the posibility to name a container. In this case, the name is *the-container*.

3. When the script ends, let's stop the container:
```
docker stop the-container
```
4. Once stopped, delete it:
```
docker rm the-container
```

5. Finally, delete the image:
```
docker rmi hello-world
```