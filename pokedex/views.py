from django.shortcuts import render

# Create your views here.
def index(request):
    pokemons =['Pikachu','Charmander','Bulbasaur','Squirtle','Charizard']
    return render(request,'index.html',{''
    'pokemons':pokemons
    })

def pokemon_detail(request,pokemon):
    return render(request,'pokemon_details.html',{
        'pokemon':pokemon
    })