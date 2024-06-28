# **Orbidi Project**

## **Description**
The Orbidi project is a web application developed with FastAPI. It allows users to add new locations and categories, as well as offering recommendations for exploring places. These recommendations prioritize locations that have never been visited and those that have not been visited in the last 30 days.

## **Table of Contents**
1. [Installation](#instalación)
2. [Use](#use)
3. [Endpoints](#endpoints)
4. [Models](#models)
5. [Autor](#autor)

## **Installation**

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

### **Run the application**
```bash
uvicorn app.main:app --reload
```

### **Run Unit Tests**
```bash
pytest test/
```

## **Endpoints**

### - **Create Location**
1. **Description:**
This endpoint creates a new location in the database using the provided latitude and longitude values.

2. **Path:**
/api/v1/create_location

3. **HTTP Method:**
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
1. **Description:**
This endpoint creates a new category in the database using the provided category information, containing the name of the place for the new category.

2. **Path:**
/api/v1/create_category

3. **HTTP Method:**
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
1. **Description:**
This endpoint creates a new record in the database for a reviewed location category combination.

2. **Path:**
/api/v1/create_location_category_reviewed

3. **HTTP Method:**
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
1. **Description:**
This function retrieves a list of 10 location-category combinations that have not been reviewed in the last 30 days from the database.

2. **Path:**
/api/v1/get_recomendations

3. **HTTP Method:**
GET

4. **Usage Example:**
    ```python
    # Request to get recomendations.
    response = client.get("/api/v1/get_recomendations")
    # The `recomendations` variable will contain a list of 10 location-category combinations that have not been reviewed in the last 30 days and status 200.
    ```

## **Models**

### - **Create Location**
1. **Description:**
Defines a model for storing location data in a database table.

2. **Fields:**
    - **id**: An integer field serving as the primary key of the table.
    - **latitude**: A float field to store the latitude coordinate of a location, and not nullable.
    - **longitude**: A float field to store the longitude coordinate of a location, and not nullable.

3. **Usage Example:**
    ```python
    # Creating a new location entry
    new_location = Location(id=1, latitude=40.7128, longitude=-74.0060)
    # Accessing location attributes
    print(f"Location ID: {new_location.id}")
    print(f"Latitude: {new_location.latitude}")
    print(f"Longitude: {new_location.longitude}")
    ```

### - **Create Category**
1. **Description:**
Define a model for storing the placename data in a database.

2. **Fields:**
    - **id**: An integer field serving as the primary key of the table.
    - **place_name**: An string field with a maximum length of 100 characters, unique, and not nullable.

3. **Usage Example:**
    ```python
    # Creating a new category instance
    new_category = Category(id=1, place_name='Restaurant')
    # Accessing the fields of the category instance
    print(new_category.id)  # Output: 1
    print(new_category.place_name)  # Output: 'Restaurant'
    ```

### - **Create Location Category Reviewed**
1. **Description:**
Define a model for storing information about reviewed location categories.

2. **Fields:**
    - **id**: An integer field serving as the primary key of the table.
    - **location_id**: An integer field, foreign key referencing the locations table, and not nullable.
    - **category_id**: An integer field, foreign key referencing the categories table, not nullable.
    - **last_reviewed**: An datetime field to store the timestamp of the last review. and not nullable.

3. **Usage Example:**
    ```python
    # Creating a new entry in the location_category_reviewed table
    new_review = LocationCategoryReviewed(
        location_id=1,
        category_id=3,
        last_reviewed=datetime.now()
    )
    session.add(new_review)
    session.commit()
    ```

## **Autor**
:man_technologist: **Brian Zapata**
* [LinkedIn](https://www.linkedin.com/in/briayan-zapata/)
