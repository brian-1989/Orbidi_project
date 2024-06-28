# **Orbidi Project**

## **Description**
---
The Orbidi project is a web application developed with FastAPI. It allows users to add new locations and categories, as well as offering recommendations for exploring places. These recommendations prioritize locations that have never been visited and those that have not been visited in the last 30 days.

## **Table of Contents**
---
1. [Installation](#instalación)
2. [Use](#use)
3. [Endpoints](#endpoints)
4. [Models](#models)
5. [To contribute](#to contribute)

## **Installation**
---

### **Prerequisites**
- Python 3.9+
- Git

### Clone the repository
```bash
git clone https://github.com/brian-1989/Orbidi_project.git
```

### **Create and Activate a Virtual Environment**
```bash
python -m venv env
source env/bin/activate
```

## **Use**
---
### **Run the application**
```bash
uvicorn app.main:app --reload
```

## **Endpoints**
---
### - **Create Location**
1. **Descripción:**
This endpoint creates a new location in the database using the provided latitude and longitude values.

2. **Path:**
/api/v1/create_location

3. **Http Method:**
POST

4. **Usage Example:**
    ```python
    # Request to create a new location with latitude 40.7128 and longitude -74.0060
    response = client.post(
        "/api/v1/create_location",
        json={"latitude": 40.7128, "longitude": -74.0060}
    )
    # Expected output: JSON response with the newly created location data and status code 201.
    ```

### - **Create Category**
1. **Descripción:**
This endpoint creates a new category in the database using the provided category information, containing the name of the place for the new category.
2. **Path:**
/api/v1/create_category
3. **Http Method:**
POST
4. **Usage Example:**
    ```python
    # Request to create a new category
    response = client.post(
        "/create_category",
        json={"place_name": "Park"}
    )
    # Expected output: JSON response with the details of the newly created category and status 201.
    ```

### - **Create Location Category Reviewed**
1. **Descripción:**
This endpoint creates a new record in the database for a reviewed location category combination.
2. **Path:**
/api/v1/create_location_category_reviewed
3. **Http Method:**
POST
4. **Usage Example:**
    ```python
    # Request to create a new location category reviewed record
    response = client.post(
        "/api/v1/create_location_category_reviewed",
        json={"location_id": 1, "category_id": 1}
    )
    # Expected output: JSON response with the newly created location category reviewed record and status 201.
    ```

### - **Get Recomendations**
1. **Descripción:**
This function retrieves a list of 10 location-category combinations that have not been reviewed in the last 30 days from the database.
2. **Path:**
/api/v1/get_recomendations
3. **Http Method:**
GET
4. **Usage Example:**
    ```python
    # Request to get recomendations.
    response = client.get("/api/v1/get_recomendations")
    # The `recomendations` variable will contain a list of 10 location-category combinations that have not been reviewed in the last 30 days and status 200.
    ```
