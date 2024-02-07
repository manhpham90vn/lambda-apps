# Lambda
## Version
```shell
Python 3.9.18
SAM CLI, version 1.107.0
```

## Create venv
```shell
python -m venv venv
```

## Active venv
```shell
source ./venv/bin/activate
```

## Install dependency
```shell
pip install celery
```

## Update requirements.txt
```shell
pip freeze > requirements.txt
```

## Install from requirements.txt
```shell
pip install -r requirements.txt
```

## Install sam
```shell
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html
```

## Validate
```shell
sam validate
```

## Build
```shell
sam build --use-container
```

## Invoke Local (need export QUEUE_URL)
```shell
sam local invoke ProducerFunction --event events/event.json

```

## Invoke remote (not work)
```shell
sam remote invoke --stack-name lambda-apps ProducerFunction --event-file events/event.json
```

## Deploy guided
```shell
sam deploy --guided
```

## Deploy
```shell
sam deploy
```

## Destroy
```shell
sam delete --stack-name lambda-apps
```

## Fix bug docker for docker desktop app
```shell
export DOCKER_HOST=unix:///home/manh/.docker/desktop/docker.sock
```