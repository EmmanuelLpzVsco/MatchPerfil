# ProfileMatcher-Core

The following component pretends to be a manager for Clients, Projects, and Profiles and administrate their lifecycle.

# Requirements

- [**Node JS**](https://stackoverflow.com/questions/47008159/how-to-downgrade-node-version) version v14.15.4
- [**Serverless framework**](https://www.serverless.com/framework/docs/getting-started/) version 1.71.1
- [**Docker**](https://docs.docker.com/get-docker/) and [**docker-compose**](https://docs.docker.com/compose/install/)
- [**npm**](https://www.npmjs.com/get-npm) version 7.4.3
- [**Flask**](https://flask.palletsprojects.com/en/1.1.x/installation/) version 1.1.2 (in the case that you want to avoid the use of **docker** and **docker-compose**)
- [**AWS Cli V2**](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

# How to setup the project

ProfileMatcher-Core could be execute in the following environments:

- Local Environment using Python Flask 
- Cloud for Production and Dev Environment on AWS using serverless framework

## On local environment

Only for the first time type:
```sh
npm install
```

You need to type the following command in your code directory:
```sh
make start
```

The migrations will be executed everytime you type the above command.

If you want to stop the local environment type:
```sh
make down
```

## On Amazon AWS
Only for the first time type:
```sh
npm install
```

First you need to have AWS cli installed and your credentials from AWS Account, then for deploy on aws you need to type:

```sh
make deploy environment=[dev|prod]
```
For this  project the environments allowed are **dev** and **prod**, if you omit the options dev or prod the default option is **dev**.

For execute the migrations to DynamoDB in **dev** | **prod** type:
```sh
make migrate environment=[dev|prod]
```

If you don't specify the environment the default is **dev**.
For turn down the previous deployis with the following command:
```sh
make remove environment=[dev|prod]
```

For consume the rest services you could invoke the lambda functions something like this:
```sh
serverless invoke -f profiles-create -d'{ "body": "{\"firstName\": \"Roberto Leroy\",\"lastName\": \"Monroy Ruiz\",\"email\": \"bluedrayco@gmail.com\"}" }' -l
```

Or consume directly using **curl** or **Postman**.

# Branching naming, commit strategy and pull requests

## Branching naming
The project has three type of motivations for typing code on this microservice:

- **Feature**: new functionality in the microservice.
- **Hotfix**: problem in a production that needs to be solved.
- **Refactor**: modify/adding code without change the previous behaviour in order to create a resilient code or make a better maintainable code.

Keep in mind these names because when you need to create a branch the structure must have the following shape:
```
Type/text-about-why-the-code
```

For example:
```
Feature/login-with-oauth2
```

## Branching origin
But... If you need to create a new branch what is the correct root's branch for that?, well, these are some cases and which branche we need to choose:

- **Hotfix**: if your functionality is a problem in the production environment you need to create your branch from **master**.
- **Feature**: if your functionality is a new feature you need to create your branch from **dev**.
- **Feature**: if you need to add some documentation or improve the existing **dev**.
- **Refactor**: if you want to improve the microservice with a new functonality or other features you need to create your branch from **dev**.

Remember that the first letter must be in capital.

## Commit strategy
The structure for the commit must have the following shape:

```
Type: text explaining the functionality to merge
```

for example:

```
Feature: Rest service for create a new project
```

## Pull requests
When you want to integrate your code after finish your functionalities you need to create a MR (merge request) on gitlab webpage to the origin branch of your functionality, for example, if you create a **Feature** branch you need to create a MR to **dev** branch.

Your MR must fullfit the following requirements:

- The branch needs to have only **one** commit.
- The branch needs to be rebased to master or dev branches (depends of the type of functionality).
- Has the naming format for branching (see Branching naming section).
- The text commit needs to have the right format (see commit strategy section).
- You cannot add/modify more than 600 lines of code per MR.
- You cannot delete more than 1000 lines of code per MR.
- For merge the code the MR must be approved by at least two partners.

# Useful commands

## Remove unused imports
```bash
make remove-unused-imports
```

## Fix code (according python standards)
```bash
make clean-code
```

## Check if the code is aligned according standards
```bash
make lint
```

## Build the images for docker-compose
```bash
make build
```