
from django.shortcuts import render, redirect
from .models import Header,Service_intro,Category ,Service,Service_feature,Portfolio ,Project,Blog,Blog_intro,Whyus,About ,Work_Process,Client_intro,Client,Contact_intro,Team,Cts,Team_intro
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect 
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import activate, get_language_info
from django.utils import translation
import  django.utils.translation 
from website import settings
from django.utils.translation import LANGUAGE_SESSION_KEY

# Create your views here.
def home(request):
	headers = Header.objects.all()
	abouts = About.objects.all()
	whyuss = Whyus.objects.all()
	service_intro = Service_intro.objects.all()
	category = Category.objects.all()
	portfolio = Portfolio.objects.all()
	project = Project.objects.order_by('-date')[:6]
	blog_intro = Blog_intro.objects.all()
	blog = Blog.objects.order_by('-created_at')[:4]
	client_intro = Client_intro.objects.all()
	client = Client.objects.all()
	contact_intro = Contact_intro.objects.all()
	ctss = Cts.objects.all()

	context = {
		'headers':headers, 
		'abouts':abouts,
		'whyuss':whyuss,
		'category':category,
		'portfolio':portfolio,
		'service_intro':service_intro,
		'project':project,
		'blog_intro':blog_intro,
		'blog':blog,
		'client_intro':client_intro,
		'client':client,
		'contact_intro':contact_intro,
		'ctss':ctss,
		}
	return render(request,'core/home.html', context)


def about(request):
	headers = Header.objects.all()
	abouts = About.objects.all()
	whyuss = Whyus.objects.all()
	workprocess = Work_Process.objects.all()
	team = Team.objects.all()
	team_intro = Team_intro.objects.all()
	client_intro = Client_intro.objects.all()
	client = Client.objects.all()
	category = Category.objects.all()

	context = {
		'headers':headers,
		'abouts':abouts,
		'whyuss':whyuss,
		'workprocess':workprocess,
		'team':team,
		'team_intro':team_intro,
		'client':client,
		'client_intro':client_intro,
		'category':category,

	}
	return render(request, 'core/about.html', context)

def category_details(request,slug):
	headers = Header.objects.all()
	category = Category.objects.all()
	category_details = Category.objects.get(slug=slug)
	service = Service.objects.filter(service_category=category_details)
	context = {
		'headers':headers,
		'category':category,
		'service':service,
		'category_details':category_details
	}
	return render(request, 'core/category.html', context)
def service_details(request,slug):
	headers = Header.objects.all()
	service = Service.objects.get(slug=slug)
	servicefeature = Service_feature.objects.filter(service=service)
	project = Project.objects.filter(Service=service)
	category = Category.objects.all()
	context = {
		'headers':headers,
		'project':project,
		'service':service,
		'servicefeature':servicefeature,
		'category':category,
	}
	return render(request, 'core/service.html', context)
def blog_list(request):
	headers = Header.objects.all()
	blog = Blog.objects.all()
	context = {
		'headers':headers,
		'blog':blog,
	  
	}
	return render(request, 'core/blog_list.html', context)
def blog_details(request,slug):
	headers = Header.objects.all()
	blog = Blog.objects.get(slug=slug)
	context = {
		'headers':headers,
		'blog':blog,
	  
	}
	return render(request, 'core/blog_details.html', context)
def portofolio(request):
	headers = Header.objects.all()
	service=Service.objects.all()
	project = Project.objects.all()
	portfolio = Portfolio.objects.all()
	category = Category.objects.all()
	context = {
		'headers':headers,
		'project':project,
		'service':service,
		'category':category,
		'portfolio':portfolio,
	}
	return render(request, 'core/portofolio.html', context)






def change_language(request):
	current_language = translation.get_language() 
	if current_language == "ar":
		lang_code ="en"
	else:
		lang_code = "ar"
	response = HttpResponseRedirect(request.POST.get('return_url',''))
	response.set_cookie(settings.LANGUAGE_COOKIE_NAME,lang_code)
	translation.activate(lang_code)
	return response

def contact(request):
	headers = Header.objects.all()
	if request.method == 'POST':
		subject = request.POST.get('subject')
		Message = request.POST.get('message')
		email = request.POST.get('email')
		name = request.POST.get('name')
		message = f"name:{name}\nemail:{email}\nmessage:{Message}"
		send_mail(subject,message, email,
		[settings.EMAIL_HOST_USER,], fail_silently=False)
		return render(request, 'core/contact.html', {'email': email,'headers':headers,})

	return render(request, 'core/contact.html', {'headers':headers,})
