# DockerSLC
Repositorio designado para la actividad 1.5 acerca de la continuación con el trabajo de Docker y GitPod

# Correr Dockerfile
docker build -t webapp:v1 . 

# Crear contenedor 
docker run -it -p 8080:8080 -v /workspace/DockerSLC/docker:/docker --name webapp -h webapp webapp:v1

# Docker commit 
# docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
docker commit webapp dockerslc:v1

# Guardar la imagen creada
docker save -o respaldo.tar.gz dockerslc:v1

# Elimar la imagen 
docker rmi 928bef6d0b84

# Restaurar la imagen 
docker load -i respaldo.tar.gz

# Última modificación 
10/06/2021
