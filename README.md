## Description

Vehicule-Service is an Application Programming Interface (API) to add,delete,updateand get vehicule .
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
$ docker build -t vehicule-service .
```
## Running the app in the Docker : 
```bash
# Run docker image
$ docker run -p 5000:5000 vehicule-service
```


## Available Endpoints

### 1. Get All Vehicules

- **Endpoint:** `/vehicule`
- **Method:** GET
- **Description:** Retrieve a list of all Vehicules.
- **Response:**
  - `200`: Successful retrieval with a list of Vehicules.
  - `500`: Internal Server Error.

### 2. Create Vehicules

- **Endpoint:** `/vehicule`
- **Method:** POST
- **Description:** Create a new Vehicule.
- **Request Body:**
  - `marque`: String - Brand of the Vehicule.
  - `genre`: String - Genre of the Vehicule.
  - `typeVehicule`: String - Type of the Vehicule.
  - `numberOfPorts` : Integer - Number of ports.
  - `fuelType`: String - Fuel type of the Vehicule.
  - `vehiculeIdentificationNumber`: String - Vehicle Identification Number.
  - `cylinderCount`: Integer - Number of cylinders.
  - `taxIdentificationNumber`: String - Tax Identification Number.
  - `taxHorsepower`: Integer - Tax Horsepower.
  - `licensePlateNumber`: String - License Plate Number.
  - `emptyWeight`: Float - Empty Weight of the Vehicule.
  - `grossVehiculeWeightRating`: Float - Gross Vehicle Weight Rating.
  - `currentCarValue`: Float - Current Car Value.
  - `manufacturingDate`: String (ISO format) - Manufacturing Date.
  - `status`: String - Status of the Vehicule.
  - `client_id`: String - ID of the associated client.
  - `number_of_ports` : Int - Number of ports.
- **Response:**
  - `201`: Vehicule created successfully.
  - `404`: Client not found (if the specified client_id does not exist).
  - `500`: Internal Server Error.

### 3. Delete Vehicule by ID

- **Endpoint:** `/vehicule/<string:vehicule_id>`
- **Method:** DELETE
- **Description:** Delete a Vehicule by ID.
- **Response:**
  - `200`: Vehicule deleted successfully.
  - `404`: Vehicule not found.
  - `500`: Internal Server Error.

### 4. Get Vehicule by ID

- **Endpoint:** `/vehicule/<string:vehicule_id>`
- **Method:** GET
- **Description:** Retrieve a Vehicule by ID.
- **Response:**
  - `200`: Successful retrieval with Vehicule details.
  - `404`: Vehicule not found.
  - `500`: Internal Server Error.

### 5. Get Vihecules by Client ID

- **Endpoint:** `/vehicule/client/<string:client_id>`
- **Method:** GET
- **Description:** Retrieve a list of Vehicules associated with a specific client.
- **Response:**
  - `200`: Successful retrieval with a list of Vehicules.
  - `404`: Client NOT FOUND with "client_id".
  - `500`: Internal Server Error.





## Stay in touch :
- Author - [Ouail Laamiri](https://www.linkedin.com/in/ouaillaamiri/)
- Test - [Postman](https://www.postman.com/avionics-meteorologist-32935362/workspace/postman-api-fundamentals-student-expert/collection/29141176-57204b79-8446-4853-aa1c-d5b9f2ab26eb?action=share&creator=29141176)
- Documentation - [Postman](https://documenter.getpostman.com/view/29141176/2s9YsDkF4R
)

## License

Vehicule-Service is [GPL licensed](LICENSE).

