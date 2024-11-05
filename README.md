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
3. Django and Graphene-Django installed in your environment.

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

4. **Run migrations** (if necessary):
   ```bash
   python manage.py migrate
   ```

5. **Run the server**:
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

- **Authors**
   - `POST /api/authors/create/`: Create a new author.
   - `GET /api/authors/`: List all authors.
   - `GET /api/authors/<id>/`: Retrieve an author by ID.
   - `PUT /api/authors/update/<id>/`: Update an author by ID.
   - `DELETE /api/authors/delete/<id>/`: Delete an author by ID.

- **Genres**
   - `POST /api/genres/create/`: Create a new genre.
   - `GET /api/genres/`: List all genres.
   - `GET /api/genres/<id>/`: Retrieve a genre by ID.
   - `PUT /api/genres/update/<id>/`: Update a genre by ID.
   - `DELETE /api/genres/delete/<id>/`: Delete a genre by ID.

- **Books**
   - `POST /api/books/create/`: Create a new book.
   - `GET /api/books/`: List all books.
   - `GET /api/books/<id>/`: Retrieve a book by ID.
   - `PUT /api/books/update/<id>/`: Update a book by ID.
   - `DELETE /api/books/delete/<id>/`: Delete a book by ID.


## Error Handling
When performing queries or mutations, error messages will be returned in case of any issue (e.g., missing fields, invalid IDs). Always ensure to handle these errors gracefully and provide appropriate feedback to users.

## Conclusion
With GraphQL, you have fine-grained control over the data retrieved from the server. Utilize the GraphiQL interface to explore more about queries and mutations available in this project. Happy coding!