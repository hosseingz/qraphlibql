# GraphQL Queries

This document provides an overview of how to use GraphQL queries and REST APIs in your project. We'll cover setting up GraphQL, making queries, and using the REST endpoints.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setting Up the Project](#setting-up-the-project)
- [GraphQL Playground](#graphql-playground)
- [Queries](#queries)
  - [Authors Queries](#authors-queries)
  - [Genres Queries](#genres-queries)
  - [Books Queries](#books-queries)
- [Mutations](#mutations)
  - [Authors Mutations](#authors-mutations)
  - [Genres Mutations](#genres-mutations)
  - [Books Mutations](#books-mutations)
- [Error Handling](#error-handling)

## Prerequisites
1. Python 3.x installed on your machine.
2. A virtual environment (recommended).


## Setting Up the Project
1. **Clone the repository**:
   ```bash
   git clone https://github.com/hosseingz/qraphlibql.git
   cd qraphlibql
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install project dependencies**:
   
   ```bash
   pip install -r requirements.txt
   ```


4. **Create the `.env` file:**

   In the root directory of your Django project (where `manage.py` is located), create a new file called `.env`. This file will hold all your environment variables.

5. **Add the following variables to `.env`:**

   Below is an example of the required environment variables for your Django project. You can copy and modify them based on your project setup.

   ```ini
   # .env

   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ```

   - `SECRET_KEY`: This is a sensitive key used by Django for cryptographic signing. Make sure it is kept secret and unique for your environment.
   - `DEBUG`: Set to `True` for development and `False` for production.

   > **Important:** Never commit your `.env` file to version control (e.g., Git). Add it to your `.gitignore` file to ensure it stays private:
   ```
   .env
   ```



6. **Run migrations** (if necessary):
   ```bash
   python manage.py migrate
   ```

7. **Run the server**:
   ```bash
   python manage.py runserver
   ```

## GraphQL Playground
Once the server is running, navigate to [http://localhost:8000/graphql](http://localhost:8000/graphql) to access the GraphiQL interface. This interface allows you to interact with the GraphQL API and test your queries and mutations.

## Queries
### Authors Queries
To fetch authors, you can use the following queries:
```graphql
# Fetch all authors
query {
  authors {
    id
    firstName
    lastName
    dateOfBirth
    dateOfDeath
  }
}

# Fetch a specific author by ID
query {
  author(id: 1) {
    id
    firstName
    lastName
    age  # It's a computed field
  }
}
```

### Genres Queries
To fetch genres, use these queries:
```graphql
# Fetch all genres
query {
  genres {
    id
    name
  }
}

# Fetch a specific genre by ID
query {
  genre(id: 1) {
    id
    name
  }
}
```

### Books Queries
To fetch books, you can use the following queries:
```graphql
# Fetch all books
query {
  books {
    id
    title
    summary
    author {
      id
      firstName
      lastName
    }
    genre {
      id
      name
    }
    publishedDate
    pageCount
  }
}

# Fetch a specific book by ID
query {
  book(id: 1) {
    id
    title
    summary
    author {
      id
      firstName
      lastName
    }
    genre {
      id
      name
    }
    publishedDate
    pageCount
  }
}
```

## Mutations
### Authors Mutations
To create, update, or delete authors, use the following mutations:
```graphql
# Create a new author
mutation {
  createAuthor(firstName: "John", lastName: "Doe", dateOfBirth: "1990-01-01") {
    author {
      id
      firstName
      lastName
    }
    message
  }
}

# Update an existing author
mutation {
  updateAuthor(id: 1, firstName: "Jane") {
    author {
      id
      firstName
    }
    message
  }
}

# Delete an existing author
mutation {
  deleteAuthor(id: 1) {
    message
  }
}
```

### Genres Mutations
To manage genres, you can use the following mutations:
```graphql
# Create a new genre
mutation {
  createGenre(name: "Fiction") {
    genre {
      id
      name
    }
    message
  }
}

# Update an existing genre
mutation {
  updateGenre(id: 1, name: "Science Fiction") {
    genre {
      id
      name
    }
    message
  }
}

# Delete an existing genre
mutation {
  deleteGenre(id: 1) {
    message
  }
}
```

### Books Mutations
For managing books, use these mutations:
```graphql
# Create a new book
mutation {
  createBook(title: "New Book", authorId: 1, summary: "A great story", genresId: [1, 2]) {
    book {
      id
      title
    }
    message
  }
}

# Update an existing book
mutation {
  updateBook(id: 1, title: "Updated Book Title") {
    book {
      id
      title
    }
    message
  }
}

# Delete an existing book
mutation {
  deleteBook(id: 1) {
    message
  }
}
```


## REST API

The REST API endpoints are structured in a way that reflects the resources. Here are some key endpoints:




### `Authentication`

#### **User Registration**
- **POST** `/api/signup/`
  - Registers a new user.
  - **Request body**:
    ```json
    {
      "username": "john_doe",
      "email": "john.doe@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "password": "password123"
    }
    ```
  - **Response**:
    ```json
    {
      "username": "john_doe",
      "message": "User successfully created!"
    }
    ```

#### **User Login**
- **POST** `/api/login/`
  - Authenticates a user and returns a success message.
  - **Request body**:
    ```json
    {
      "username": "john_doe",
      "password": "password123"
    }
    ```
  - **Response**:
    ```json
    {
      "username": "john_doe",
      "message": "Login successful!"
    }
    ```

### `Authors`

#### **List All Authors**
- **GET** `/api/authors/`
  - Retrieves a list of all authors.
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "1980-01-01",
        "date_of_death": null
      },
      {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Smith",
        "date_of_birth": "1990-05-15",
        "date_of_death": null
      }
    ]
    ```

#### **Create a New Author**
- **POST** `/api/authors/`
  - Creates a new author.
  - **Request body**:
    ```json
    {
      "first_name": "George",
      "last_name": "Orwell",
      "date_of_birth": "1903-06-25",
      "date_of_death": "1950-01-21"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 3,
      "first_name": "George",
      "last_name": "Orwell",
      "date_of_birth": "1903-06-25",
      "date_of_death": "1950-01-21"
    }
    ```

#### **Retrieve an Author by ID**
- **GET** `/api/authors/<id>/`
  - Retrieves an author by their ID.
  - **Example**: `/api/authors/1/`
  - **Response**:
    ```json
    {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe",
      "date_of_birth": "1980-01-01",
      "date_of_death": null
    }
    ```

#### **Update an Author**
- **PUT** `/api/authors/<id>/`
  - Updates an author's information.
  - **Request body**:
    ```json
    {
      "first_name": "Johnathan",
      "last_name": "Doe",
      "date_of_birth": "1980-01-01",
      "date_of_death": null
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "first_name": "Johnathan",
      "last_name": "Doe",
      "date_of_birth": "1980-01-01",
      "date_of_death": null
    }
    ```

#### **Delete an Author**
- **DELETE** `/api/authors/<id>/`
  - Deletes an author by their ID.
  - **Example**: `/api/authors/1/`
  - **Response**:
    - Status: 204 No Content

---

### `Genres`

#### **List All Genres**
- **GET** `/api/genres/`
  - Retrieves a list of all genres.
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Fiction"
      },
      {
        "id": 2,
        "name": "Non-fiction"
      }
    ]
    ```

#### **Create a New Genre**
- **POST** `/api/genres/`
  - Creates a new genre.
  - **Request body**:
    ```json
    {
      "name": "Science Fiction"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 3,
      "name": "Science Fiction"
    }
    ```

#### **Retrieve a Genre by ID**
- **GET** `/api/genres/<id>/`
  - Retrieves a genre by its ID.
  - **Example**: `/api/genres/1/`
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Fiction"
    }
    ```

#### **Update a Genre**
- **PUT** `/api/genres/<id>/`
  - Updates a genre by its ID.
  - **Request body**:
    ```json
    {
      "name": "Fantasy"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Fantasy"
    }
    ```

#### **Delete a Genre**
- **DELETE** `/api/genres/<id>/`
  - Deletes a genre by its ID.
  - **Example**: `/api/genres/1/`
  - **Response**:
    - Status: 204 No Content

---

### `Books`

#### **List All Books**
- **GET** `/api/books/`
  - Retrieves a list of all books.
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "title": "1984",
        "author": {
          "id": 1,
          "first_name": "George",
          "last_name": "Orwell"
        },
        "summary": "A dystopian novel about totalitarianism.",
        "genre": [
          {
            "id": 1,
            "name": "Fiction"
          }
        ],
        "published_date": "1949-06-08",
        "page_count": 328
      }
    ]
    ```

#### **Create a New Book**
- **POST** `/api/books/`
  - Creates a new book.
  - **Request body**:
    ```json
    {
      "title": "1984",
      "author": {
        "first_name": "George",
        "last_name": "Orwell"
      },
      "summary": "A dystopian novel about totalitarianism.",
      "genre": [
        {
          "name": "Fiction"
        }
      ],
      "published_date": "1949-06-08",
      "page_count": 328
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "title": "1984",
      "author": {
        "id": 1,
        "first_name": "George",
        "last_name": "Orwell"
      },
      "summary": "A dystopian novel about totalitarianism.",
      "genre": [
        {
          "id": 1,
          "name": "Fiction"
        }
      ],
      "published_date": "1949-06-08",
      "page_count": 328
    }
    ```

#### **Retrieve a Book by ID**
- **GET** `/api/books/<id>/`
  - Retrieves a book by its ID.
  - **Example**: `/api/books/1/`
  - **Response**:
    ```json
    {
      "id": 1,
      "title": "1984",
      "author": {
        "id": 1,
        "first_name": "George",
        "last_name": "Orwell"
      },
      "summary": "A dystopian novel about totalitarianism.",
      "genre": [
        {
          "id": 1,
          "name": "Fiction"
        }
      ],
      "published_date": "1949-06-08",
      "page_count": 328
    }
    ```

#### **Update a Book**
- **PUT** `/api/books/<id>/`
  - Updates a book's information by its ID.
  - **Request body**:
    ```json
    {
      "title": "1984",
      "author": {
        "id": 1,
        "first_name": "George",
        "last_name": "Orwell"
      },
      "summary": "A dystopian novel about totalitarianism.",
      "genre": [
        {
          "id": 1,
          "name": "Fiction"
        }
      ],
      "published_date": "1949-06-08",
      "page_count": 328
    }
    ```
  - **Response**:
    ```json
    {
      "title": "1984 (Updated)",
      "author": {
        "id": 1,
        "first_name": "George",
        "last_name": "Orwell"
      },
      "summary": "A dystopian novel about totalitarianism.",
      "genre": [
        {
          "id": 1,
          "name": "Fiction"
        }
      ],
      "published_date": "1949-06-08",
      "page_count": 328
    }
    ```

#### **Delete a Book**
- **DELETE** `/api/books/<id>/`
  - Deletes a book by its ID.
  - **Example**: `/api/books/1/`
  - **Response**:
    - Status: 204 No Content


## Error Handling
When performing queries or mutations, error messages will be returned in case of any issue (e.g., missing fields, invalid IDs). Always ensure to handle these errors gracefully and provide appropriate feedback to users.

## Conclusion
With GraphQL, you have fine-grained control over the data retrieved from the server. Utilize the GraphiQL interface to explore more about queries and mutations available in this project. Happy coding!