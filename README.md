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


## Available Endpoints

### 1. Get All Vihecules

- **Endpoint:** `/vihecule`
- **Method:** GET
- **Description:** Retrieve a list of all Vihecules.
- **Response:**
  - `200`: Successful retrieval with a list of Vihecules.
  - `500`: Internal Server Error.

### 2. Create Vihecule

- **Endpoint:** `/vihecule`
- **Method:** POST
- **Description:** Create a new Vihecule.
- **Request Body:**
  - `marque`: String - Brand of the Vihecule.
  - `genre`: String - Genre of the Vihecule.
  - `typeVihecule`: String - Type of the Vihecule.
  - `fuelType`: String - Fuel type of the Vihecule.
  - ... (Other fields)
- **Response:**
  - `201`: Vihecule created successfully.
  - `404`: Client not found (if the specified client_id does not exist).
  - `500`: Internal Server Error.

### 3. Delete Vihecule by ID

- **Endpoint:** `/vihecule/<string:vihecule_id>`
- **Method:** DELETE
- **Description:** Delete a Vihecule by ID.
- **Response:**
  - `200`: Vihecule deleted successfully.
  - `404`: Vihecule not found.
  - `500`: Internal Server Error.

### 4. Get Vihecule by ID

- **Endpoint:** `/vihecule/<string:vihecule_id>`
- **Method:** GET
- **Description:** Retrieve a Vihecule by ID.
- **Response:**
  - `200`: Successful retrieval with Vihecule details.
  - `404`: Vihecule not found.
  - `500`: Internal Server Error.

### 5. Get Vihecules by Client ID

- **Endpoint:** `/vihecule/client/<string:client_id>`
- **Method:** GET
- **Description:** Retrieve a list of Vihecules associated with a specific client.
- **Response:**
  - `200`: Successful retrieval with a list of Vihecules.
  - `500`: Internal Server Error.





## Stay in touch :
- Author - [Ouail Laamiri](https://www.linkedin.com/in/ouaillaamiri/)
- Test - [Postman](https://www.postman.com/avionics-meteorologist-32935362/workspace/postman-api-fundamentals-student-expert/collection/29141176-57204b79-8446-4853-aa1c-d5b9f2ab26eb?action=share&creator=29141176)
- Documentation - [Postman](https://documenter.getpostman.com/view/29141176/2s9YsDkF4R
)

## License

Vihecule-Service is [MIT licensed](LICENSE).

