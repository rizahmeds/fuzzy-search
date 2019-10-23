from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def index(request):
	return render(request, 'home.html')

def search(request):
	word = request.GET.get('word')

	path_to_file = os.path.join(BASE_DIR, 'dataset')

	df = pd.read_csv(path_to_file+'/word_search.tsv', sep='\t', header=None, engine='python', 
		na_filter=False)

	df.rename(columns = {0: "word", 1:"usage"}, inplace = True)
	df['word_length'] = df['word'].str.len()

	# list of all searched words
	fuzzy_words = df[df['word'].str.contains(word)].head(25)

	# list of words start with searched word
	start_with_word = fuzzy_words[fuzzy_words['word'].str.startswith(word)]
	start_with_word = start_with_word.sort_values('word_length')

	# list of words contains the searched word
	contain_words = fuzzy_words[~(fuzzy_words['word'].str.startswith(word))]
	contain_words = contain_words.sort_values('word_length')
	
	result = start_with_word.append(contain_words)
	
	print ( result )

	return HttpResponse(result.to_json(orient='records'))

def starts_with(df, word):
	try:
		result = df[df['word'].str.startswith(word)]
		return result.to_json()
	except Exception as e:
		raise e
