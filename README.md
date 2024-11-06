# ShopEase Microservices

## Overview

ShopEase is an e-commerce platform composed of three microservices: User Service, Product Service, and Order Service.

## Technologies Used

- User Service: Python Flask
- Product Service: Node.js
- Order Service: Java Spring Boot
- Databases: PostgreSQL, MongoDB, MySQL

## Running the Project

1. Make sure Docker and Docker Compose are installed.
2. Clone this repository.
3. Navigate to the project root directory.
4. Run `docker-compose up --build` to start all services.

## API Endpoints

### User Service

- **Register User**
  - `POST /register`
  - Request Body:
    ```json
    {
        "username": "testuser",
        "password": "password123"
    }
    ```
  
- **Login User**
  - `POST /login`
  - Request Body:
    ```json
    {
        "username": "testuser",
        "password": "password123"
    }
    ```

### Product Service

- **Create Product**
  - `POST /products`
  - Request Body:
    ```json
    {
        "name": "Product1",
        "price": 10.0
    }
    ```

- **Get Products**
  - `GET /products`

### Order Service

- **Create Order**
  - `POST /orders`
  - Request Body:
    ```json
    {
        "productName": "Product1",
        "quantity": 2
    }
    ```

- **Get Orders**
  - `GET /orders`
 
