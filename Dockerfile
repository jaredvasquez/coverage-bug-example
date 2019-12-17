FROM python:3.6.9-slim-buster

WORKDIR /workdir/

# Install Requirements
ADD requirements_dev.txt .
RUN pip install -r requirements_dev.txt

# Install the rest of everything
ADD . .
RUN pip install -e .

# Run tests
CMD ["bash", "./show_example.sh"]
