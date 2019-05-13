from django.shortcuts import render
from django.http import HttpResponse
from requests import request

from . import larker

def cardify(universe):
    universe_dict = {}
    for i in universe:
        universe_dict[i] = ''
    for i in universe:
        for j in i:
            universe_dict[i] = universe_dict[i] + ' {}'.format(j)
    return universe_dict

def index(request):
    uni = larker.Universe().universeCreate()
    cards = cardify(uni)
    context = {'universe': cards}
    
    if request.method == 'POST':
        post_transform = larker.parser.parse(request.POST['solution'])
        solution_transform = larker.CalcTransformer(uni).transform(post_transform)
        tree_data = solution_transform.children

        return HttpResponse(tree_data)
    
    return render(request, 'onsets/index.html', context)