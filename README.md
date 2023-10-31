# Your Birthday Application PoC
```bash
1. Design and code a simple "Hello World" appication tht exposes the following HTTP-base APIs:

Description: saves/updates the given user's name and date of birth in the database.
Request PUT /hello/<username> { "dateOfBirth": "YYYY-MM-DD" }
Response: 204 No content

Note:
<username> must contain only letters.
YYYY-MM-DD must be a date before the today date.

Description: Returns hello birthday message for the given user
Request: Get /hello/<username>
Response: 200 OK

Response Examples:
A. If username's birthday is in N days:
    { "message": "Hello, <username>! Your birthday is in N day(s)}

B. If username's birthday is today:
    { "message": "Hello, <username>! Happy birthday!"}

```
### Prerequisites
Install [Docker](https://docs.docker.com/get-docker/)

Install [docker-compose](https://docs.docker.com/compose/install/)

### Install
```bash
mkdir /var/birthday_app
git clone git@github.com:mariuschicinas/birthday_app.git
docker-compose build
docker-compose up
```
### Usage
- Insert user revolut with date of birth July 1, 2015
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"dateOfBirth": "2015-07-01"}' http://localhost:5000/hello/revolut
```
- Get user birthday
```bash
curl -XGET http://localhost:5000/hello/revolut
```