import os

from django.conf import settings
from django.shortcuts import render_to_response
from squiggle.cli import visualize_inner

# a fasta file to use:
fasta_file = str(
        os.path.abspath(
            os.path.join(
                settings.BASE_DIR,
                'static/example_seqs/human_HBB.fasta'
                )
            )
        )

# Create your views here.

def index(request):
    # the 'file' needs to be of type click.Path which is a tuple
    file_tuple = (fasta_file,)

    script, div = visualize_inner(file_tuple, web=True)
    pass

    return render_to_response(
        'squiggle_views/squiggle.html',
        {'script': script, 'div': div}
    )

