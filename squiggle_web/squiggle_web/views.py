"""
Top level views. used to render the top-level home page.

TODO: is this the correct location for this view?

"""
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


def home(request):
    """
    This function renders the home page and includes a form that allows file
    uploads.

    TODO: restrict uploads to fasta files.
    TODO: needs error checking. Error if the user clicks upload and no file
        selected.
    """
    print("simple_upload")
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'home.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'home.html')
