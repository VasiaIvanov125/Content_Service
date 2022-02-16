from django.shortcuts import render, redirect
from .translate import translate_csv
from .models import Images
from .forms import ImagesForm
import random


def main_window(request):
    form = ImagesForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        search_string = r''.join([i for i in list(form.cleaned_data.values()) if i])
        category_matches = Images.objects.filter(categories__iregex=search_string).values()
        rnd_category_matches = random.choice(category_matches)
        return render()

    data = {
        'form': form
    }
    return render(request, 'one_app/one_window.html', data)


def csv_to_database(request):
    Arr = translate_csv()

    for row in Arr:
        Images.objects.get_or_create(
            image_url=row[0],
            amount_show=row[1],
            categories=row[2]
        )
    category_matches = Images.objects.filter(categories__iregex=r'nature').values()
    print(category_matches)
    print(random.choice(category_matches))
    return redirect('main_window')