all: build test

build:
	docker build -t coverage-test .

test:
	docker run coverage-test 
