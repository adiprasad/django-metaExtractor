from django.shortcuts import render
from .forms import URLForm
from .forms import MetaForm
from bs4 import BeautifulSoup
import requests


# Create your views here.
def home(request):
	title = "Hey there!"
	URL_form = URLForm(request.POST or None)
	signInPage = True

	context = {
		"form" : URL_form,
		"pg_1" : signInPage,
		"testMsg" : "Hey there",
	}

	if URL_form.is_valid():
		form_entry = URL_form.cleaned_data.get("url_name")
		print form_entry


		r = requests.get(form_entry)
		soup = BeautifulSoup(r.text,"html.parser")		#Store DOM tree in soup

		headTag = soup.head 		# extract the headTag

		titleString = soup.title.string  		#Store the title in titleString variable
		meta_desc = ''
		meta_key = ''

		meta_desc_obj = headTag.select('meta[name="description"]')  		#Select those meta childs of head Tag which have name = descrpiton
		meta_keywords_obj = headTag.select('meta[name="keywords]')			#Select those meta childs of head Tag which have name = keywords

		#print "Title : " + titleString			# Print the title (can be returned)
		if (meta_desc_obj):							# If any meta description was found
			meta_desc =  meta_desc_obj[0]['content']		#Print the content attribute of the first tag in the list of tags
		if (meta_keywords_obj):
			meta_key = meta_keywords_obj[0]['content']

		signInPage = False

		context = {
		"form" : URL_form,
		"title" : titleString,
		"desc" : meta_desc,
		"keys" : meta_key,
		"pg_1" : signInPage,
		}

	return render(request,"home.html",context)

def storeView(request):
	label = "Store"
	form_entry = request.POST.get("url_name","")

	r = requests.get(form_entry)
	soup = BeautifulSoup(r.text,"html.parser")		#Store DOM tree in soup

	headTag = soup.head 		# extract the headTag

	titleString = soup.title.string  		#Store the title in titleString variable
	meta_desc = ''
	meta_key = ''

	meta_desc_obj = headTag.select('meta[name="description"]')  		#Select those meta childs of head Tag which have name = descrpiton
	meta_keywords_obj = headTag.select('meta[name="keywords]')			#Select those meta childs of head Tag which have name = keywords

	#print "Title : " + titleString			# Print the title (can be returned)
	if (meta_desc_obj):							# If any meta description was found
		meta_desc =  meta_desc_obj[0]['content']		#Print the content attribute of the first tag in the list of tags
	if (meta_keywords_obj):
		meta_key = meta_keywords_obj[0]['content']

	form_pop = {'title': titleString,'description': meta_desc,'keywords': meta_key}

	store_form = MetaForm(initial = form_pop)
	
	context = {
	"form" : store_form,
	"button_text" : label,
	"title" : titleString,
	"desc" : meta_desc,
	"keys" : meta_key,
	"action_dest" : '/done/',
	}

	return render(request,"store.html",context)

def fetchView(request):
	fetch_form = URLForm()
	label = "Fetch"
	link_on_click = "/store/"

	context = {
	"form" : fetch_form,
	"button_text" : label,
	"action_dest" : link_on_click,
	}
	return render(request,"store.html",context)

def doneView(request):
	form = MetaForm(request.POST)

	if form.is_valid():
		instance = form.save(commit=False)
		print instance.title
		print instance.description
		instance.save()

	return render(request,"done.html")



