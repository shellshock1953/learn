# Remote Learning Lab

Used for shared GoTTY (web terminal) sessions per student.

### Images hub:
[Docker Hub](https://hub.docker.com/r/2xnone/study)

### passgen:
```
python3 sike_passwd.py --file docker-compose.yml --user vasya
```

### Run
```
docker-compose up -d
```

### Stop
```
docker-compose stop
```

### Remove
```
docker-compose down -v
# or
docker-compose stop
docker-compose rm -f
```
