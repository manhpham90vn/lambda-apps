# Lambda
## Version
```shell
Python 3.9.18
SAM CLI, version 1.107.0
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

## Invoke Local
```shell
sam local invoke GetLamdaIPFunction --event events/event.json
```

## Invoke remote
```shell
sam remote invoke --stack-name lambda-apps --event-file events/event.json GetLamdaIPFunction
```

## Deploy guided
```shell
sam deploy --guided
```

## Deploy
```shell
sam deploy
```

## Fix bug docker
```shell
export DOCKER_HOST=unix:///home/manh/.docker/desktop/docker.sock
```