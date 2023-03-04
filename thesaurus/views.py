from django.shortcuts import render
from . import thesaurus

# Create your views here.

def thesaurus_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        output = thesaurus.thesaurus(original_text)
        return render(request, 'thesaurus.html', {'output_text': output, 'original_text':original_text})
    else:
        return render(request, 'thesaurus.html')