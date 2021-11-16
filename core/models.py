from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db import models
from django.urls import reverse

from django.utils import timezone
from datetime import datetime
class Header(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	icon = models.ImageField(null=True, blank=True)
	apple = models.ImageField(null=True, blank=True)
	navlogo = models.ImageField(null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	facebook_url = models.CharField(max_length=255, null=True, blank=True)
	instagram_url = models.CharField(max_length=255, null=True, blank=True)
	linkedin_url = models.CharField(max_length=255, null=True, blank=True)
	twitter_url = models.CharField(max_length=255, null=True, blank=True)
	tiktok_url = models.CharField(max_length=255, null=True, blank=True)
	slider_img = models.ImageField(null=True, blank=True)
	slider_text = models.CharField(max_length=255, null=True, blank=True)
	slider_header = models.CharField(max_length=255, null=True, blank=True)
	videofile= models.FileField(upload_to = 'videos/', null=True, verbose_name="")
	footer_img = models.ImageField(null=True, blank=True)
	footer_address1 = models.CharField(max_length=255, null=True, blank=True)
	footer_address2 = models.CharField(max_length=255, null=True, blank=True)
	footer_text = RichTextField(null=True, blank=True)
	googel_map_url = models.CharField(max_length=255, null=True, blank=True)
	working_hours = models.CharField(max_length=255, null=True, blank=True)
	def __str__(self):
		return self.title or ''

	@property
	def videofileURL(self):
		try:
			url = self.videofile.url
		except:
			url = ''
		return url

	@property
	def iconURL(self):
		try:
			url = self.icon.url
		except:
			url = ''
		return url

	@property
	def appleimageURL(self):
		try:
			url = self.apple.url
		except:
			url = ''
		return url

	@property
	def navlogoimageURL(self):
		try:
			url = self.navlogo.url
		except:
			url = ''
		return url

	@property
	def slider_imgimageURL(self):
		try:
			url = self.slider_img.url
		except:
			url = ''
		return url
	@property
	def footer_imgimageURL(self):
		try:
			url = self.footer_img.url
		except:
			url = ''
		return url
class Service_intro(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)
	intro = RichTextField(null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	Service_intro_image = models.ImageField(upload_to='photos/', max_length=254,null=True, blank=True)
	
	def __str__(self):
		return self.title or ''	
	@property
	def Service_intro_imageimageURL(self):
		try:
			url = self.Service_intro_image.url
		except:
			url = ''
		return url

	
class Category(models.Model):
	Category_name = models.CharField(max_length=255, null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	Category_description = RichTextField(null=True, blank=True)
	Category_icon = models.CharField(max_length=255, null=True, blank=True)
	Category_image_description = models.ImageField(upload_to='photos/', max_length=254,null=True, blank=True)
	Category_image_slider = models.ImageField(upload_to='photos/', max_length=254,null=True, blank=True)

	def __str__(self):
		return self.Category_name or ''
	@property
	def Category_image_descriptionimageURL(self):
		try:
			url = self.Category_image_description.url
		except:
			url = ''
		return url
	@property
	def Category_image_sliderimageURL(self):
		try:
			url = self.Category_image_slider.url
		except:
			url = ''
		return url
class Service(models.Model):
	service_name = models.CharField(max_length=255, null=True, blank=True)
	slug =  models.SlugField(max_length=250,null = True, blank = True)
	service_intro = RichTextField(null=True, blank=True)
	Service_description = RichTextField(null=True, blank=True)
	service_category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='Services')
	Service_image = models.ImageField(upload_to='photos/', max_length=254,null=True, blank=True)
	Service_image_slider = models.ImageField(upload_to='photos/', max_length=254,null=True, blank=True)
	def __str__(self):
		return self.service_name or ''
	@property
	def Service_imageimageURL(self):
		try:
			url = self.Service_image.url
		except:
			url = ''
		return url
	@property
	def Service_image_sliderimageURL(self):
		try:
			url = self.Service_image_slider.url
		except:
			url = ''
		return url

class Service_feature(models.Model):
	feature_name = models.CharField(max_length=255, null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	feature = RichTextField(null=True, blank=True)
	feature_icon = models.CharField(max_length=255, null=True, blank=True)
	service = models.ForeignKey(to=Service, on_delete=models.CASCADE)
	def __str__(self):
		return self.feature_name or ''
class Portfolio(models.Model):
	header = models.CharField(max_length=255, null=True, blank=True)
	body = RichTextField(null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	def __str__(self):
		return self.header or ''
class Project(models.Model):
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	Service = models.ForeignKey(Service,on_delete=models.CASCADE,related_name="Projects")
	project_name = models.CharField(max_length=200,null = True, blank = True)
	project_details = RichTextField(null=True, blank=True)
	project_client = models.CharField(max_length=200,null = True, blank = True)
	project_url = models.URLField(max_length = 200,null = True, blank = True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	img_1 =models.ImageField(upload_to='project/',null=True,blank=True)
	img_2 =models.ImageField(upload_to='project/',null=True,blank=True)
	img_3=models.ImageField(upload_to='project/',null=True,blank=True)
	date = models.DateTimeField(null = True, blank = True)

	def get_absolute_url(self):
		return reverse('Project_list')

	def __str__(self):
		return self.project_name or ''
	@property
	def img_1imageURL(self):
		try:
			url = self.img_1.url
		except:
			url = ''
		return url
	@property
	def img_2imageUrl(self):
		try:
			url = self.img_2.url 

		except :
			url = ''
		return url

	@property
	def img_3imageUrl(self):
		try:
			url = self.img_3.url 
		except :
			url = ''
		return url

class Blog_intro(models.Model):
	header = models.CharField(max_length=255, null=True, blank=True)
	body = RichTextField(null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	cover_img = models.ImageField(upload_to='blog/',null=True,blank=True)
	def __str__(self):
		return self.header or ''
	@property
	def cover_imgimageUrl(self):
		try:
			url = self.cover_img.url 

		except :
			url = ''
		return url		
class Blog(models.Model):
	header = models.CharField(max_length=255, null=True, blank=True)
	body = RichTextField(null=True, blank=True)
	img = models.ImageField(upload_to='blog/',null=True,blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	time = models.CharField(max_length=255, null=True, blank=True)
	def __str__(self):
		return self.header or ''  
	@property
	def imgimageUrl(self):
		try:
			url = self.img.url 

		except :
			url = ''
		return url		  
class Whyus(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	body = RichTextField(null=True, blank=True)
	img = models.ImageField(upload_to='photos/', max_length=254,null=True, blank=True)
	def __str__(self):
		return self.title or ''

	@property
	def imgimageURL(self):
		try:
			url = self.img.url
		except:
			url = ''
		return url

	
class About(models.Model):
	header = models.CharField(max_length=255, null=True, blank=True)
	intro = RichTextField(null=True, blank=True)
	body = RichTextField(null=True, blank=True)
	about_image = models.ImageField(upload_to='photos/', max_length=254,null=True, blank=True)
	number_of_project = models.IntegerField(null=True , blank=True)
	number_of_workers=models.IntegerField(null=True , blank=True)
	Years_of_experience=models.IntegerField(null=True , blank=True)
	number_of_client= models.IntegerField(null=True , blank=True)
	plan = RichTextField(null=True, blank=True)
	mission = RichTextField(null=True, blank=True)
	vission = RichTextField(null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	def __str__(self):
		return self.header or ''

	@property
	def about_imageimageURL(self):
		try:
			url = self.about_image.url
		except:
			url = ''
		return url


class Work_Process(models.Model):
	process = models.CharField(max_length=255, null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	icon = models.CharField(max_length=255, null=True, blank=True)	
class Client_intro(models.Model):
	header = models.CharField(max_length=255, null=True, blank=True)
	body = RichTextField(null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	def __str__(self):
		return self.header or ''


class Client(models.Model):
	client_name = models.CharField(max_length=200)
	review_message = RichTextField(null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	img = models.ImageField(upload_to='client/', max_length=254,null=True, blank=True)
	def __str__(self):  
		return self.client_name or ''  
	@property
	def imgimageURL(self):
		try:
			url = self.img.url
		except:
			url = ''
		return url   


class Contact_intro(models.Model):
	header = models.CharField(max_length=255, null=True, blank=True)
	body = RichTextField(null=True, blank=True)
	slug = models.SlugField(max_length=250,null = True, blank = True)
	def __str__(self):
		return self.header or ''
class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=12)
	subject = models.CharField(max_length=100)
	message = models.TextField(blank=True)
	contact_date = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.email
	
class Team_intro(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)
	about_team = RichTextField(null=True, blank=True)
	def __str__(self):
		return self.title or ''
class Team(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	profile_img = models.ImageField(null=True, blank=True)
	position = models.CharField(max_length=255, null=True, blank=True)
	url_slug = models.CharField(max_length=255, null=True, blank=True)
	def __str__(self):
		return self.name or ''
	@property
	def profile_imgimageURL(self):
		try:
			url = self.profile_img.url
		except:
			url = ''
		return url	

class Cts(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)
	text = RichTextField(null=True, blank=True)
	call_icon = models.CharField(max_length=255, null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	url_slug = models.CharField(max_length=255, null=True, blank=True)
	def __str__(self):
		return self.title or ''