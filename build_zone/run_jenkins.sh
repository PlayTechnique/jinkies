#!/bin/bash -el

THIS_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd ${THIS_SCRIPT_DIR}

source build.env

docker run -d -p ${HOST_JENKINS_PORT}:${CONTAINER_JENKINS_PORT} --name ${CONTAINER_SHORT_NAME} ${IMAGE_TAG}:${IMAGE_VERSION}

echo "http://localhost:${HOST_JENKINS_PORT}"
