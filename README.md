# DockerSLC
Repositorio designado para la actividad 1.5 acerca de la continuación con el trabajo de Docker y GitPod

# Correr Dockerfile
docker build -t webapp:v1 . 

# Crear contenedor 
docker run -it -p 8080:8080 -v /workspace/DockerSLC/docker:/docker --name webapp -h webapp webapp:v1
