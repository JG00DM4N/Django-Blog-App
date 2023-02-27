from django.shortcuts import render
from . import translate

# Create your views here.

def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        language = request.POST['language']
        print(original_text)
        print(language)
        if original_text == '':
            return render(request, 'translator.html', {'output_text':"", 'original_text':"You need to type something here!"})
        elif language == '':
            return render(request, 'translator.html', {'output_text':"You need to select a language!", 'original_text':original_text})
        else:
            output = translate.translate(original_text, language)
            return render(request, 'translator.html', {'output_text':output, 'original_text':original_text})
    else:    
        return render(request, 'translator.html')