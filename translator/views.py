from django.shortcuts import render
from deep_translator import GoogleTranslator
from .models import TranslationHistory

def home(request):

    translated = ""
    text=""
    source = "en"
    target = "ta"
    if request.method == "POST":

        text = request.POST.get("text")
        source = request.POST.get("source")
        target = request.POST.get("target")

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        TranslationHistory.objects.create(
            original_text=text,
            translated_text=translated,
            source_language=source,
            target_language=target
        )

    return render(
        request,
        "home.html",
        {"translated": translated,
         "text":text}
    )