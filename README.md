# Setup

Optional: modify `Dockerfile` to override version of `channels-redis`

Build and start:
```sh
docker-compose build
docker-compose up
```

## Check that basic consumer works

```sh
curl --http1.1 -v \
  -H 'Upgrade: websocket' \
  -H 'Connection: Upgrade' \
  -H 'Sec-WebSocket-Key: pM1jwIzQ+y37rax5wirNog==' \
  -H 'Sec-WebSocket-Version: 13' \
  'http://localhost:8001/ws/ok/'
```

## Try consumer that denies requests

```sh
curl --http1.1 -v \
  -H 'Upgrade: websocket' \
  -H 'Connection: Upgrade' \
  -H 'Sec-WebSocket-Key: pM1jwIzQ+y37rax5wirNog==' \
  -H 'Sec-WebSocket-Version: 13' \
  'http://localhost:8001/ws/denied/'
```

## Trigger leak of redis connections

```sh
while true; do curl --http1.1 -v \
  -H 'Upgrade: websocket' \
  -H 'Connection: Upgrade' \
  -H 'Sec-WebSocket-Key: pM1jwIzQ+y37rax5wirNog==' \
  -H 'Sec-WebSocket-Version: 13' \
  'http://localhost:8001/ws/denied/'
done
```

## Show open redis connections

```sh
docker-compose exec app sh -c "lsof -c daphne | grep :6379"
```

## Open Django shell

```sh
docker-compose exec app django-admin shell
```