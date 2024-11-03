import graphene
from graphene_django import DjangoObjectType
from .models import *



class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'date_of_death']



class CreateAuthorMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        date_of_birth = graphene.Date(required=False)
        date_of_death = graphene.Date(required=False)
    
    author = graphene.Field(AuthorType)
    
    def mutate(self, info, first_name, last_name, date_of_birth=None, date_of_death=None):
        author = Author.objects.create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            date_of_death=date_of_death
        )

        return CreateAuthorMutation(author=author)


class DeleteAuthorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    message = graphene.String()
    
    def mutate(self, info, id):
        author = Author.objects.get(pk=id)
        author.delete()
        
        return DeleteAuthorMutation(message=f"Author by id={id} deleted!.")


class UpdateAuthorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        date_of_birth = graphene.Date(required=False)
        date_of_death = graphene.Date(required=False)

    author = graphene.Field(AuthorType)

    def mutate(self, info, id, first_name, last_name, date_of_birth=None, date_of_death=None):
        author = Author.objects.get(pk=id)

        author.first_name = first_name
        author.last_name = last_name
        
        if date_of_birth:
            author.date_of_birth = date_of_birth
        if date_of_death:
            author.date_of_death = date_of_death

        author.save()
        
        return UpdateAuthorMutation(author=author)



class Query(graphene.ObjectType):
    authors = graphene.List(AuthorType)
    author = graphene.Field(AuthorType, id=graphene.ID())

    def resolve_authors(self, info):
        return Author.objects.all()
    
    def resolve_author(self, info, id):
        return Author.objects.get(pk=id)
    
    
class Mutation(graphene.ObjectType):
    create_author = CreateAuthorMutation.Field()
    delete_author = DeleteAuthorMutation.Field()
    update_author = UpdateAuthorMutation.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)