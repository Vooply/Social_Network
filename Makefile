
migrations:
	@docker exec -it -w /Social_Network Social_Network_apii python src/manage.py makemigrations

migrate:
	@docker exec -it -w /Social_Network Social_Network_apii python src/manage.py migrate

app:
	@mkdir -p src/app/$(name)
	@docker exec -it -w /Social_Network Social_Network_api python src/manage.py startapp $(name) src/app/$(name)

start_compose:
	@docker-compose -f docker-compose-dev.yml up

test_env:
	@cat ./docker/envs/env_example > ./docker/envs/.env-local

test_user:
	@docker exec -it -w /Social_Network Social_Network_api python src/manage.py createsuperuser

build_compose:
	@docker-compose -f docker-compose-dev.yml build