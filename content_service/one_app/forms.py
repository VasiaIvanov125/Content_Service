from django.forms import Form, CharField, TextInput


class ImagesForm(Form):

    cat_1 = CharField(widget=TextInput(attrs={'class': 'text_categories', 'placeholder': 'Category 1'}),
                      required=False)
    cat_2 = CharField(widget=TextInput(attrs={'class': 'text_categories', 'placeholder': 'Category 2'}),
                      required=False)
    cat_3 = CharField(widget=TextInput(attrs={'class': 'text_categories', 'placeholder': 'Category 3'}),
                      required=False)
    cat_4 = CharField(widget=TextInput(attrs={'class': 'text_categories', 'placeholder': 'Category 4'}),
                      required=False)
    cat_5 = CharField(widget=TextInput(attrs={'class': 'text_categories', 'placeholder': 'Category 5'}),
                      required=False)
    cat_6 = CharField(widget=TextInput(attrs={'class': 'text_categories', 'placeholder': 'Category 6'}),
                      required=False)
    cat_7 = CharField(widget=TextInput(attrs={'class': 'text_categories', 'placeholder': 'Category 7'}),
                      required=False)
    cat_8 = CharField(widget=TextInput(attrs={'class': 'text_categories', 'placeholder': 'Category 8'}),
                      required=False)
    cat_9 = CharField(widget=TextInput(attrs={'class': 'text_categories', 'placeholder': 'Category 9'}),
                      required=False)
    cat_10 = CharField(widget=TextInput(attrs={'class': 'text_categories', 'placeholder': 'Category 10'}),
                       required=False)
