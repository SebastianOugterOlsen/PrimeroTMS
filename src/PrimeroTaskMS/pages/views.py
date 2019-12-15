from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):    # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")    # String of HTML code  Meget basic
    my_context = {
        "my_text" : "This is about me",
        "my_number" : 123,
        "my_list" : [123, 321, 456, 654]

    }
    return render(request, "home.html", my_context)