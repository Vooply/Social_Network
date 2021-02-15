# Setup

#### Before running project

- Create local env file and set up an email in it
- Build containers
- Run project

#### Create local env file

Just run `make test_env`

#### Build containers

`docker-compose -f docker-compose-dev.yml build` or `make build_compose`

#### Run project

`docker-compose -f docker-compose-dev.yml up` or `make start_compose`

#### When project is running

- Apply db migrations `make migrations` and `make migrate`
- Create superuser `make test_user`. After that you will be able to login into Admin
- Be happy

#### Create new app

`make app name=<app_name>`


#### All commands you can find in `Makefile`

# Django project description:
The project is like a Social Network with posts,comments and likes.

