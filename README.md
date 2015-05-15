# python-docker-exit

#### Build the image, run the container

	docker-compose up -d

#### Check

	docker-compose ps

#### Stop it

This will likely take a bit more than 10 seconds.

	time docker-compose stop

#### Check the exit code

This will likely be `137`.

	docker-compose ps

