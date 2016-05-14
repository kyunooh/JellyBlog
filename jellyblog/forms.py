from django import forms


class SearchForm(forms.Form):
    search_query = forms.CharField(label="search", min_length=2, max_length=100)