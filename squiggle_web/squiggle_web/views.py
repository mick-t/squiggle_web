"""
Top level views. used to render the top-level home page. 

TODO: is this the correct location for this view?

"""
from django.shortcuts import render

def home(request):
    """
    This function renders the home page. This is as basic as one can get
    """
    template = 'home.html'
    
    return render(request, template )
    
    
    
    