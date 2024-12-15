# Secure and Scalable Application

A project offers a Secure&Scalable web application with Docker, NGINX, and FastAPI.

---

## **1. Network Infrastructure**
- **Docker Compose**: Creates segmented networks:
  - **backend**: For app communication.
  - **frontend**: For load balancer communication.
- CIDR Ranges:
  - Backend: `192.168.1.0/24`
  - Frontend: `192.168.2.0/24`

---

## **2. Security**
- HTTPS enabled via self-signed SSL certificate.
- Certificate files are located in `nginx/ssl/`.

---

## **3. REST API**
- Developed using FastAPI.
- Endpoints:
  - `GET /items`: Retrieves items.
  - `POST /items`: Creates a new item.
  - `PUT /items/{id}`: Updates an item.
  - `DELETE /items/{id}`: Deletes an item.

---

## **Running the Application**
1. Build and run the containers:
   ```bash
   docker-compose up --build
