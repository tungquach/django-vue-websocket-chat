WD := $(shell pwd)
SA := $(word 2, $(MAKECMDGOALS))

pip_install:
	@printf "starting install $(SA)\n"
	docker-compose exec web pip install $(SA)
	@printf "completed install $(SA)\n"

test:
	@printf "starting local testing\n"
	docker-compose exec web pytest --ds=core.settings
	@printf "completed local testing\n"
