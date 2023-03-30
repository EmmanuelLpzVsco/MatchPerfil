environment ?= dev

build:
	docker-compose build

start: build
	docker-compose down && rm -rf dynamodb_data && docker-compose up 

down:
	docker-compose down && rm -rf dynamodb_data

lint:
	flake8 src && flake8 test && flake8 app.py && flake8 flask_src

fix-code:
	black src && black test && black app.py && black flask_src

order-imports:
	isort src && isort test && isort app.py && isort flask_src

remove-unused-imports:
	autoflake --remove-all-unused-imports -r --in-place src && autoflake --remove-all-unused-imports -r --in-place flask_src && autoflake --remove-all-unused-imports -r --in-place test

clean-code: remove-unused-imports order-imports fix-code

deploy: 
	serverless deploy --stage=$(environment)

remove:
	serverless remove --stage=$(environment)

migrate:
	serverless invoke --stage=$(environment) -f scripts-seeders -l
