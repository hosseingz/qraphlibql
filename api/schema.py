import graphene
from graphene_django import DjangoObjectType
from .models import *



class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'date_of_death']


class GenreType(DjangoObjectType):
    class Meta:
        model = Genre
        fields = ['id', 'name']


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
    
    
class Mutation(graphene.ObjectType):
    create_author = CreateAuthorMutation.Field()
    delete_author = DeleteAuthorMutation.Field()
    update_author = UpdateAuthorMutation.Field()
    
    create_genre = CreateGenreMutation.Field()
    delete_genre = DeleteGenreMutation.Field()
    update_genre = UpdateGenreMutatuin.Field()
    
    
    
schema = graphene.Schema(query=Query, mutation=Mutation)