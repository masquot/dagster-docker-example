# set base image (host OS)
FROM python:3.7-slim

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY complex_asset_graph.py .
COPY test_complex_asset_graph.py .

# install dependencies
RUN pip install dagster dagit pandas pytest

# command to run on container start
CMD [ "dagit", "-h", "0.0.0.0", "-p", "3000", "-f", "complex_asset_graph.py" ]
