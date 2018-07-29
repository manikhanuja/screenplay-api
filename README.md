# screenplay-api
Rest APIs using DJango
# Docker Tutorial
## links for Docker download
[Docker for Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows)

[Docker for Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac)

---

## How to execute Docker
- if you are using command line simply go to `cd screenplay-api` *(root folder)*

- in the root folder, execute `docker-compose up`
    - this will read the `Dockerfile` and execute the script and use `requirements.txt` to download the Django dependencies and use the `docker-compose.yml` as structure reference.

    - you can also specify `docker-compose up -d` to detach from the process and have it running in the background. This is helpful if you need to do things other than watch the logs.

- to see the containers, execute `docker container ls`
    - this is helpful for when you need to see various information (container ID, ports, etc) regarding your containers.

- to connect to a container while it is still running your command, execute `docker exec -it CONTAINER_ID /bin/bash`
    - example: `docker exec -it c5c493e1e98e /bin/bash`
    - to exit the container, simple type `exit`

- Docker will serve two containers
	- one for the postgresql database
	- one for the Django API

## Deleting everything Docker created

One thing noticed is that docker will create images and tends to accumulate data. 
A useful command to run to delete all containers, images, etc is `docker system prune`

- ### WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all dangling images
  - all build cache
By default, volumes are not removed to prevent important data from being deleted if there is currently no container using the volume. 
Use the --volumes flag when running the command to prune volumes as well.
So, to also remove the volumes (--volumes), any unused images (--all), as well as override the confirmation prompt (--force):

`docker system prune --all --force --volumes`

- ### WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all volumes not used by at least one container
  - all images without at least one container associated to them
  - all build cache
        
- prune can also be used on just one aspect:
  - docker container prune # Remove all stopped containers
  - docker volume prune # Remove all unused volumes
  - docker image prune # Remove unused images

---

## Useful links for Docker
https://docs.docker.com/compose/

https://docs.docker.com/get-started/

https://docs.docker.com/engine/examples/postgresql_service/

https://docs.docker.com/samples/library/python/#create-a-dockerfile-in-your-python-app-project

https://docs.docker.com/config/containers/multi-service_container/

https://medium.com/the-code-review/clean-out-your-docker-images-containers-and-volumes-with-single-commands-b8e38253c271
