1. What does REST stand for?
    - Representational State Transfer (REST)

2. REST APIs are designed around a resource(any kind of object, data, or service that can be accessed by the client).

3. What is an identifier of a resource? Give an example.
    - a “Uniform Resource Identifier" (URI) that the distinguishes resources from one another.

    `cats.com/short-nose/long-hair --- long hair is the URI`

4. What are the most common HTTP verbs?
    - GET
    - POST
    - PUT
    - DELETE


5. What should the URIs be based on?
    - it should represent the data and its uniqueness with nouns.

6. Give an example of a good URI.

  `cats.com/short-hair/russian-gray`

7. What does it mean to have a ‘chatty’ web API? Is this a good or a bad thing?
    - not a good thing, chatty web apis send multiple requests to find data it needs

8. What status code does a successful GET request return?

    - 200

9. What status code does an unsuccessful GET request return?

    - 404

10. What status code does a successful POST request return?
    - 201

11. What status code does a successful DELETE request return?

    - 204

---------

1. Status Codes
    - 100s= informational codes that tell us (the client) teh header part of the request went through, server will try to transmit.
    - 200’s = SUCCESS...sort of!!! Request was accepted. With async (202) the request was not fully processed, but the request met the validation requirements.
    - 300’s = Redirection codes when resource we request aren't available at the location we're searching in.
    - 400’s = CLIENT ERROR codes for invalid requests. EX: incorrect client input, timeouts etc
    - 500’s = SERVER ERROR codes, can happen when server is ovewhelmed with requests or server is down.

2. 202 = Request accepted, but still processing. Used by async processing.

3. 308 = Permanent redirect, a new url is used to accessed the resource for a more direct route.

4. 204 (no content) is used if an update didn’t return data to a client

5. 410 (gone) is used if a resource used to exist but no longer does

6. ‘Forbidden’ status code = 403

Why do we need to pull our MongoDB database string out of our server and put it into our .env?
What is middleware?
What does app.use(express.json()) do?
What does the /:id mean in a route?
What is the difference between PUT and PATCH?
How do you make a default value in a schema?
7. 500 = Server error, request was not completed by server. 
8. 200 request was received and processed, 201 request was successful and CREATED.


