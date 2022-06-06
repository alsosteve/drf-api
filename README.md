# drf-api
# Python 401d1818
## Labs 31: Django REST Framework & Docker
### Authors: Steve Ngo
​
## Overview
Rebuild a custom version of Things API demo project from scratch
​
## Implementation Notes:
Demo file [demo repo](https://github.com/codefellows/seattle-python-401d18/tree/main/class-31)

## Feature Tasks and Requirements
* Rebuild a custom version of `Things API` demo project from scratch.
  * Replace `things_project` and `Thing` with your own application and model.
  * Your model must have at least as many fields as demo’s model.
  * Your model must have one field that is a foreign key to user.
  * **NOTE**: You are not required to build any templates for this lab.

### Docker
* **NOTE** Refer to the class demo for built out `Dockerfile` and `docker-compose.yml` examples.
* Update `Dockerfile` and `docker-compose.yml` if needed.

## User Acceptance Tests
* Modify provided unit tests in demo to work for your project.

## Configuration
Create a virtual environment inside `drf-api`.

Use the `drf-api` folder as the root of your project’s git repository.

## Stretch Goals
* Research using a production server vs. the built in development server.
* Research using postgres instead of sqlite as database.