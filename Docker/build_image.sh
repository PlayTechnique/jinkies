#!/bin/bash

set -e

THIS_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd ${THIS_SCRIPT_DIR}

THIS_SCRIPT_NAME=$(basename $0)
ENV_FILE="${THIS_SCRIPT_DIR}/build.env"
SHOW_HELP="false"

for arg in $@
do
  case $arg in
    "--env-file"       )  shift; ENV_FILE=$arg; shift;;
    "-h" | "--help"    )  SHOW_HELP="true"; shift;;
  esac
done

function usage() {
  cat <<EOS
Usage: ${THIS_SCRIPT_NAME} --env-file - builds the container\n
Arguments:\n
\t--env-file\t/path/to/foo.env. Provides an alternate set of definitions for environment variables \n
\t\t\t(defaults to built in build.env)
EOS
}

if [[ "${SHOW_HELP}" == "true" ]]; then
  echo -e $(usage)
  exit 0
fi

if [[ ! -f "${ENV_FILE}" ]]; then
  echo "ERROR: No such variables file <${ENV_FILE}>. This must exist and be readable."
  exit 1
fi

source "${ENV_FILE}"

docker build -t "${IMAGE_TAG}:${IMAGE_VERSION}" . --build-arg cask_jenkins_config="${CASC_JENKINS_CONFIG}" \
                                                  --build-arg jenkins_home="${JENKINS_HOME}" \
                                                  --build-arg jenkins_java_opts="${JENKINS_JAVA_OPTS}"
