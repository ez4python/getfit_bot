restart:
	docker compose down
	docker rmi getfit_bot-bot:latest
	docker compose up

stop:
	docker compose down
	docker rmi getfit_bot-bot:latest