from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'attempt' in request.session:    
        request.session['attempt'] = request.session['attempt'] + 1
    else:
        request.session['attempt'] = 1
    context = {
    "attempt": request.session['attempt'],
    "random_word": get_random_string(length=14).upper()
    }
    return render(request,'generator/index.html', context)

def reset(request):
    try:
        del request.session['attempt']
    except KeyError:
        pass
    return redirect('/')
    
 
	