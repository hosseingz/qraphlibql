import graphene
from graphene_django import DjangoObjectType
from .models import *



class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = "__all__"


class GenreType(DjangoObjectType):
    class Meta:
        model = Genre
        fields = "__all__"


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"



# Author CRUD

class CreateAuthorMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        date_of_birth = graphene.Date(required=False)
        date_of_death = graphene.Date(required=False)
    
    author = graphene.Field(AuthorType)
    message = graphene.String(required=False)
    
    def mutate(self, info, first_name, last_name, date_of_birth=None, date_of_death=None):
        author = Author.objects.create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            date_of_death=date_of_death
        )

        return CreateAuthorMutation(author=author, message='Author successfully created.')


class DeleteAuthorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    message = graphene.String()
    
    def mutate(self, info, id):
        try:
            author = Author.objects.get(pk=id)
            author.delete()
            return DeleteGenreMutation(message=f"Successfully deleted author with ID: {id}.")
        except Author.DoesNotExist:
            return DeleteGenreMutation(message=f"Error: Author with ID {id} does not exist.")


class UpdateAuthorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        date_of_birth = graphene.Date(required=False)
        date_of_death = graphene.Date(required=False)

    author = graphene.Field(AuthorType)
    message = graphene.String(required=False)

    def mutate(self, info, id, first_name=None, last_name=None, date_of_birth=None, date_of_death=None):
        try:
            author = Author.objects.get(pk=id)

            if first_name:
                author.first_name = first_name
            if last_name:
                author.last_name = last_name
            if date_of_birth:
                author.date_of_birth = date_of_birth
            if date_of_death:
                author.date_of_death = date_of_death

            author.save()
        
            return UpdateAuthorMutation(author=author, message=f"Successfully updated author with ID: {id}.")
        except Author.DoesNotExist:
            return UpdateAuthorMutation(message=f"Error: Author with ID {id} does not exist.")
        
        


# Genre CRUD

class CreateGenreMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
    
    genre = graphene.Field(GenreType)
    message = graphene.String(required=False)
    
    def mutate(self, info, name):
        genre = Genre.objects.create(name=name)
        
        return CreateGenreMutation(genre=genre, message='Genre successfully created.')


class DeleteGenreMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    message = graphene.String()
    
    def mutate(self, info, id):
        try:
            genre = Genre.objects.get(pk=id)
            genre.delete()
            return DeleteGenreMutation(message=f"Successfully deleted genre with ID: {id}.")
        except Genre.DoesNotExist:
            return DeleteGenreMutation(message=f"Error: Genre with ID {id} does not exist.")


class UpdateGenreMutatuin(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)

    genre = graphene.Field(GenreType)
    message = graphene.String(required=False)
    
    def mutate(self, info, id, name):
        try:
            genre = Genre.objects.get(pk=id)
            genre.name = name
            genre.save()
            return UpdateGenreMutatuin(genre=genre, message=f"Successfully updated genre with ID: {id}.")
        except Genre.DoesNotExist:
            return UpdateGenreMutatuin(message=f"Error: Genre with ID {id} does not exist.")
       


# Book CRUD

class CreateBookMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        author_id = graphene.ID(required=False)
        summary = graphene.String()
        genres_id = graphene.List(of_type=graphene.ID)
        published_date = graphene.Date(required=False)
        page_count = graphene.Int(required=False)
    
    book = graphene.Field(BookType)
    message = graphene.String(required=False)
    
    def mutate(self, info, title, summary, genres_id, published_date=None, page_count=None, author_id=None):
        try:
            book = Book.objects.create(
                title=title,
                summary=summary,
                published_date=published_date,
                page_count=page_count
            )

            if author_id:
                author = Author.objects.get(pk=author_id)
                book.author = author
                   
            for id in genres_id:
                genre, _ = Genre.objects.get_or_create(pk=id)
                book.genre.add(genre)
            
            book.save()
            
            return CreateBookMutation(book=book, message='Book successfully created.')
            
        except Author.DoesNotExist:
            return CreateBookMutation(message=f"Error: Author with ID {id} does not exist.")
        except Genre.DoesNotExist:
            return CreateBookMutation(message=f"Error: Genre with ID {id} does not exist.")
        
        
               

class DeleteBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    message = graphene.String()
    
    def mutate(self, info, id):
        try:
            book = Book.objects.get(pk=id)
            book.delete()
            return DeleteBookMutation(message=f"Successfully deleted book with ID: {id}.")
        except Book.DoesNotExist:
            return DeleteBookMutation(message=f"Error: Book with ID {id} does not exist.")


class UpdateBookMutatuin(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        author_id = graphene.ID(required=False)
        summary = graphene.String()
        genres_id = graphene.List(of_type=graphene.ID)
        published_date = graphene.Date(required=False)
        page_count = graphene.Int(required=False)

    book = graphene.Field(BookType)
    message = graphene.String(required=False)
    
    def mutate(self, info, id, title=None, author_id=None, summary=None, genres_id=None, published_date=None, page_count=None):
        
        try:
            book = Book.objects.get(pk=id)

            if title:
                book.title = title
            if author_id:
                author = Author.objects.get(pk=author_id)
                book.author = author
            if summary:
                book.summary = summary
            if genres_id:
                book.genre.clear() 
                for id in genres_id:
                    genre, _ = Genre.objects.get_or_create(pk=id)
                    book.genre.add(genre)
            if published_date:
                book.published_date = published_date
            if page_count:
                book.page_count = page_count
                            
            book.save()
            
            return UpdateBookMutatuin(book=book, message=f"Successfully updated book with ID: {id}.")
        except Book.DoesNotExist:
            return UpdateBookMutatuin(message=f"Error: Book with ID {id} does not exist.")
        except Author.DoesNotExist:
            return UpdateBookMutatuin(message=f"Error: Author with ID {id} does not exist.")
        except Genre.DoesNotExist:
            return UpdateBookMutatuin(message=f"Error: Genre with ID {id} does not exist.")
    
        


class Query(graphene.ObjectType):
    authors = graphene.List(AuthorType)
    author = graphene.Field(AuthorType, id=graphene.ID())
    
    def resolve_authors(self, info):
        return Author.objects.all()
    
    def resolve_author(self, info, id):
        return Author.objects.get(pk=id)
    
    
    genres = graphene.List(GenreType)
    genre = graphene.Field(GenreType, id=graphene.ID())
    
    def resolve_genres(self, info):
        return Genre.objects.all()
    
    def resolve_genre(self, info, id):
        return Genre.objects.get(pk=id)
    
    
    books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.ID())
    
    def resolve_books(self, info):
        return Book.objects.all()
    
    def resolve_book(self, info, id):
        return Book.objects.get(pk=id)
    
    
    
class Mutation(graphene.ObjectType):
    create_author = CreateAuthorMutation.Field()
    delete_author = DeleteAuthorMutation.Field()
    update_author = UpdateAuthorMutation.Field()
    
    create_genre = CreateGenreMutation.Field()
    delete_genre = DeleteGenreMutation.Field()
    update_genre = UpdateGenreMutatuin.Field()
    
    create_book = CreateBookMutation.Field()
    delete_book = DeleteBookMutation.Field()
    update_book = UpdateBookMutatuin.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)