#!/bin/bash


RETRY=3
WAIT_SEC=5
PROJECT_PATH=

start-docker() {
    systemctl --quiet start docker.service
}

check-docker() {
    systemctl --quiet is-active docker.service
}

check-dependencies() {
    command -v docker docker-compose > /dev/null
}


if ! check-dependencies; then
    echo "Dependency error"
    exit 1
fi

for n in {1..$RETRY}; do
    check-docker && break
    echo "Starting docker service #$n ..."
    start-docker
    sleep ${WAIT_SEC}
done

if check-docker; then
    echo "Docker service running, spawning decryption containers"
    docker-compose -p app -f "${PROJECT_PATH}/docker-compose.app.yml" down

    if docker-compose -p startup -f "${PROJECT_PATH}/docker-compose.startup.yml" up; then
        echo "Decryption done, spawning app services"
        docker-compose -p app -f "${PROJECT_PATH}/docker-compose.app.yml" up -d
    fi
else
    echo "Docker cannot be started, exiting !"
fi
