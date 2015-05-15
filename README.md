# python-docker-exit

#### Build the image, run the container

	docker-compose up -d

#### Check

	docker-compose ps

#### Stop it

This should take far less than 10 seconds.

	time docker-compose stop

#### Check the exit code

	docker-compose ps

The exit code should be 0.
