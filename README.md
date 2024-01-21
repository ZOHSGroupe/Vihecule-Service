### To install requirements :
pip install -r requirements.txt 
### To run app : 
gunicorn -c gunicorn_config.py main:app
### Build Docker image : 
docker build -t email-service .
### Run the Docker container : 
docker build -t email-service
### Link to test api via Postman :
https://www.postman.com/avionics-meteorologist-32935362/workspace/postman-api-fundamentals-student-expert/collection/29141176-57204b79-8446-4853-aa1c-d5b9f2ab26eb?action=share&creator=29141176
### Documentation of api in postman :
https://documenter.getpostman.com/view/29141176/2s9YsDkF4R