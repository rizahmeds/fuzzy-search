from django.shortcuts import render
from django.http import HttpResponse
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def search(request):
	word = request.GET.get('word')
	import pandas as pd

	path_to_file = os.path.join(BASE_DIR, 'dataset')

	user_info = pd.read_csv(path_to_file+'/word_search.tsv',delimiter='\t',encoding='utf-8')
	print(list(user_info.columns.values)) #file header
	print(user_info.head(35)) #last N rows

	return HttpResponse("Implement here :: "+word)
