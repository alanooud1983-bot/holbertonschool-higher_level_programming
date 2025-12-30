## Basics of HTTP/HTTPS

### Difference between HTTP and HTTPS
HTTP (Hypertext Transfer Protocol) is used for communication between clients and servers on the web. It transfers data in plain text, which makes it vulnerable to interception.

HTTPS (Hypertext Transfer Protocol Secure) is the secure version of HTTP. It uses SSL/TLS encryption to protect data during transmission, ensuring confidentiality and data integrity.

---

### Structure of an HTTP Request and Response

**HTTP Request:**
- Method (GET, POST, PUT, DELETE)
- URL
- Headers
- Body (optional)

**HTTP Response:**
- Status Code (e.g., 200, 404, 500)
- Headers
- Body (response data)

---

### Common HTTP Methods

- **GET**: Retrieves data from the server.
- **POST**: Sends data to the server to create a new resource.
- **PUT**: Updates an existing resource.
- **DELETE**: Removes a resource from the server.

---

### Common HTTP Status Codes

- **200 OK**: The request was successful.
- **201 Created**: A new resource was successfully created.
- **400 Bad Request**: The request is invalid or malformed.
- **404 Not Found**: The requested resource does not exist.
- **500 Internal Server Error**: The server encountered an error.
