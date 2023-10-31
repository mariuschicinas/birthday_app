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