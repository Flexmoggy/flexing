### User Profile view

- Endpoint Path: /profile/{id}
- Endpoint method: GET

- Headers:

  - Authorization: Bearer token

- Response: User profile view
- Response body:
  '''JSON
  {
  "username": "billgoat57"
  "profile_pic": "picture url"
  "first_name": "Timmy"
  "last_name": "Tester"
  "email": "Testmail@company.com"
  "interests": "Blah, Blah, Blah"
  "skills": "Blah, Blah, Blah"
  "bio": "Long text of user's life"
  "reviews": {
  "reviewer": "asshatreviewer"
  "post_date": "date/time"
  "rating": "int value from 1-5"
  "review_text": "long text value"
  }
  }

### List Profiles

- Endpoint path: /list
- Endpoint method: GET

- Response: a list of relevent user profiles
- Response Body:
  '''JSON
  {
  "users": [
  {
  "username": "exampleName123",
  "profile_pic": "picture url",
  }
  ]
  }

### Create new User

- Endpoint path: /new
- Endpoint method: POST

- Response: sign up form
- Response body:
  '''JSON
  {
  "username": "billgoat57"
  "profile_pic": "picture url"
  "first_name": "Timmy"
  "last_name": "Tester"
  "email": "Testmail@company.com"
  "interests": "Blah, Blah, Blah"
  "skills": "Blah, Blah, Blah"
  "bio": "Long text of user's life"
  }

### Delete User

- Endpoint path: /profile/{id}
- Endpoint method: DELETE

- Header:

  - Authorization: Bearer token

- Response: delete user profile

### Update User Profile

- Endpoint path: /profile/{id}
- Endpoint method: PUT

- Header:

  - Authorization: Bearer token

- Response: update user profile
- Response body:
  '''JSON
  {
  "username": "updated"
  "profile_pic": "updated url"
  "first_name": "updated"
  "last_name": "updated"
  "email": "Testmail@company.com"
  "interests": "Blah, Blah, Blah"
  "skills": "Blah, Blah, Blah"
  "bio": "Long text of user's life"
  }
