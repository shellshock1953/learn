#!/bin/bash
set -e
SLEEP=1
MAIN_COMPOSE=docker-compose.yml
log_i() {
  echo -e "[--]\t${1}"
}
log_e() {
  echo -e "[!!]\t${1}"
}

files=(
  docker-compose.yml
  docker-compose.kb21.yml
)

for file in "${files[@]}"; do
  if [ -f "$file" ]; then
    log_i "Found ${file}"
    services=$(cat ${file}| yq '.services | to_entries[].key')
    for service in $services; do
      log_i "docker-compose -f ${file} up -d $service"
      docker-compose -f ${MAIN_COMPOSE} -f ${file} up -d ${service//\"}
      sleep $SLEEP
      log_i "${service//\"} is running..."
      echo ""
    done
  else
    log_e "No such file ${file}"
  fi
done