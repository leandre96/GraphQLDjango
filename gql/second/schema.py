from graphene import relay, ObjectType
from graphene_django import DjangoObjectType,DjangoModelFormMutation
from graphene_django.filter import DjangoFilterConnectionField

from .models import Animal
from .forms import AnimalForm

# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class AnimalNode(DjangoObjectType):
    class Meta:
        model = Animal
        # Provide more complex lookup types
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'genus': ['exact'],
            'is_domesticated': ['exact'],
        }
        interfaces = (relay.Node, )
        
class AnimalMutation(DjangoModelFormMutation):
    class Meta:
        form_class = AnimalForm
        
class Query(ObjectType):
    animal = relay.Node.Field(AnimalNode)
    all_animals = DjangoFilterConnectionField(AnimalNode)
