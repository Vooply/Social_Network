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


### First step after run project
- create user on url, user/register/
- if you set up an email in setting or env-local file (this better) and gave valid email, than
check email for verification user
  
- after register, go url user/auth for authenticate and get a jwt token
- token lives 30000 sec :)
- now you can create post and comments for posts
- post on url posts/, comments - comments/
- after creation, you can like, unlike, get who liked on url id(posts or comments)/like or /unlike or /fans


