COMPOSE=docker-compose -f docker-compose.yml

build: 
	$(COMPOSE) build

no-cache: 
	$(COMPOSE) build --no-cache

up:
	$(COMPOSE) up

down:
	$(COMPOSE) down

clean:
	$(COMPOSE) up --build --force-recreate --no-deps

tail:
	$(COMPOSE) logs -f

stop:
	$(COMPOSE) down --remove-orphans

shell:
	$(COMPOSE) exec -it django /bin/sh
