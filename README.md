# README

I discovered a bug in `coveragepy` when running in Docker images. I haven't been able to identify the source but this repo provides a reproducible example.

Simply run the `make` command with Docker running locally. This will build and run a new Docker image which will run some tests and output the `.coverage` file.

The `.coverage` file is corrupted with lots of non-UTF characters and what looks like artifacts from sqlite3. 
