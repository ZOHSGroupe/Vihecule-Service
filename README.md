## Description

Vihecule-Service is an Application Programming Interface (API) to add,delete,updateand get vihecule .
## Installation :
```bash
# install requirements
$ pip install -r requirements.txt 
```
## Running the app : 
```bash
# Run application
$ gunicorn -c gunicorn_config.py main:app
```
## Build Docker image : 
```bash
# build a docker image
$ docker build -t vihecule-service .
```
## Running the app in the Docker : 
```bash
# Run docker image
$ docker run -p 5000:5000 vihecule-service
```
## Stay in touch :
- Author - [Ouail Laamiri](https://www.linkedin.com/in/ouaillaamiri/)
- Test - [Postman](https://www.postman.com/avionics-meteorologist-32935362/workspace/postman-api-fundamentals-student-expert/collection/29141176-57204b79-8446-4853-aa1c-d5b9f2ab26eb?action=share&creator=29141176)
- Documentation - [Postman](https://documenter.getpostman.com/view/29141176/2s9YsDkF4R
)

## License

Email-Service is [MIT licensed](LICENSE).

