
# Hulu REST API with Flask and MongoDB

This project is a Flask-based REST API designed to interact with a MongoDB database containing Hulu records. It provides endpoints for creating, reading, updating, and deleting records.

---

## Features

- **Fetch All Records**: Retrieve all records from the database.
- **Fetch Specific Record**: Retrieve a record by title.
- **Add New Record**: Insert a new record into the database.
- **Update Record**: Update a record by its title.
- **Delete Record**: Delete a record by its title.

---

## Requirements

Before running this application, ensure you have the following installed:

1. **Python 3.7+**  
   - Download: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **MongoDB Atlas** (or Local MongoDB Server)  
   - MongoDB Atlas: [https://www.mongodb.com/atlas/database](https://www.mongodb.com/atlas/database)  
   - MongoDB Community Edition: [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)

3. **Postman** (for API testing)  
   - Download: [https://www.postman.com/downloads/](https://www.postman.com/downloads/)

4. **Python Dependencies**:  
   Install required Python libraries using pip:  
   ```bash
   pip install flask pymongo
   ```

---

## Setup Instructions

1. Clone the repository:  
   ```bash
   git clone https://github.com/Swathi-Reddy1408/Hulu-Database-Management-API.git
   cd Hulu-Database-Management-API
   ```

2. Configure MongoDB Atlas or Local MongoDB:  
   - Replace the placeholder `<username>` and `<password>` in the MongoDB connection string in `PROG_ASSIGN_23915_700743277.py`:  
     ```python
     client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.hlrnkae.mongodb.net/?retryWrites=true&w=majority")
     ```

3. Run the application:  
   ```bash
   python PROG_ASSIGN_23915_700743277.py
   ```

4. Open Postman or your browser and interact with the API at `http://127.0.0.1:5000`.

---

## API Endpoints

### 1. **Fetch All Records**  
   - **URL**: `/api`  
   - **Method**: `GET`  
   - **Response**: JSON array of all records.  
   - **Example**:  
     ```bash
     curl -X GET http://127.0.0.1:5000/api
     ```

---

### 2. **Fetch Specific Record by Title**  
   - **URL**: `/api/<string:title>`  
   - **Method**: `GET`  
   - **Parameters**:  
     - `title`: The title of the Hulu record.  
   - **Response**: JSON object of the matching record or a message if no record is found.  
   - **Example**:  
     ```bash
     curl -X GET http://127.0.0.1:5000/api/Friends
     ```

---

### 3. **Add a New Record**  
   - **URL**: `/api`  
   - **Method**: `POST`  
   - **Body**: JSON object containing the required fields.  
   - **Required Fields**:  
     - `id`, `title`, `description`, `score`, `rating`, `clips_count`, `episodes_count`, `genres`, `seasons_count`, `company`, `released_at`.  
   - **Response**: Confirmation message.  
   - **Example**:  
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{
       "id": "12345",
       "title": "Friends",
       "description": "A sitcom about six friends living in New York.",
       "score": 8.9,
       "rating": "PG-13",
       "clips_count": 20,
       "episodes_count": 236,
       "genres": ["Comedy", "Drama"],
       "seasons_count": 10,
       "company": "Warner Bros.",
       "released_at": "1994-09-22"
     }' http://127.0.0.1:5000/api
     ```

---

### 4. **Update Record by Title**  
   - **URL**: `/api/<string:title>`  
   - **Method**: `PATCH`  
   - **Body**: JSON object containing the updated fields (`id`, `title`, `description`, `score`, `rating`).  
   - **Response**: Confirmation message or error message if the record is not found.  
   - **Example**:  
     ```bash
     curl -X PATCH -H "Content-Type: application/json" -d '{
       "id": "12345",
       "title": "Friends",
       "description": "Updated description",
       "score": 9.0,
       "rating": "PG"
     }' http://127.0.0.1:5000/api/Friends
     ```

---

### 5. **Delete Record by Title**  
   - **URL**: `/api/<string:title>`  
   - **Method**: `DELETE`  
   - **Parameters**:  
     - `title`: The title of the Hulu record to delete.  
   - **Response**: Confirmation message.  
   - **Example**:  
     ```bash
     curl -X DELETE http://127.0.0.1:5000/api/Friends
     ```
