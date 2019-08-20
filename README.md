# Dockerizing-DRF-Next-Level

### Requirements
* Docker(Linux, MacOS or Windows)
* Docker Compose
### Run
In the root directory you have to open cmd and run following commands <br/>
$ docker volume create --name=hamzacms-db <br/>
$ docker-compose up <br/>


And access API endpoints on <br/> 
http://localhost:8000/api/v1//users/ <br/>
http://localhost:8000/api/v1/projects/ <br/>


### Endpoints

#### Users
GET /       http://localhost:8000/api/v1/users/ <br/>
POST /      http://localhost:8000/api/v1/users/ <br/>
GET :id/    https://localhsot:8000/api/v1/users/id/ <br/>

#### Projects
GET /       http://localhost:8000/api/v1/projects/ <br/>
POST /      http://localhost:8000/api/v1/projects/ <br/>
GET :id/    https://localhsot:8000/api/v1/projects/id/ <br/>
PUT :id/    https://localhsot:8000/api/v1/projects/id/ <br/>
