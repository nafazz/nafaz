from modeltranslation.translator import translator, TranslationOptions
from .models import Header,Service_intro,Team_intro,Category ,Service,Service_feature,Portfolio ,Project,Blog_intro,Blog, Whyus,About ,Work_Process,Client_intro,Client,Contact_intro ,Team, Cts 

class HeaderTranslationOptions(TranslationOptions):
	fields = ('title', 'slider_text','slider_header','footer_address1','footer_address2',)

translator.register(Header, HeaderTranslationOptions)
class ServiceIntroTranslationOptions(TranslationOptions):
	fields = ('title', 'intro',)

translator.register(Service_intro, ServiceIntroTranslationOptions)
class CategoryTranslationOptions(TranslationOptions):
	fields = ('Category_name', 'Category_description',)

translator.register(Category, CategoryTranslationOptions)
class ServiceTranslationOptions(TranslationOptions):
	fields = ('service_name', 'service_intro','Service_description','service_category',)

translator.register(Service, ServiceTranslationOptions)
class Service_featureTranslationOptions(TranslationOptions):
	fields = ('feature_name', 'feature',)

translator.register(Service_feature, Service_featureTranslationOptions)
class PortfolioTranslationOptions(TranslationOptions):
	fields = ('header','body',)

translator.register(Portfolio, PortfolioTranslationOptions)



class ProjectTranslationOptions(TranslationOptions):
	fields = ('project_name','project_details','Service','category','project_client')

translator.register(Project, ProjectTranslationOptions)
class BlogIntroTranslationOptions(TranslationOptions):
	fields = ('header', 'body',)

translator.register(Blog_intro, BlogIntroTranslationOptions)
class BlogTranslationOptions(TranslationOptions):
	fields = ('header', 'body',)

translator.register(Blog, BlogTranslationOptions)
class WhyusTranslationOptions(TranslationOptions):
	fields = ('title', 'body',)

translator.register(Whyus, WhyusTranslationOptions)
class AboutTranslationOptions(TranslationOptions):
	fields = ('header','intro', 'body','mission','vission','plan',)

translator.register(About, AboutTranslationOptions)
class WorkProcessTranslationOptions(TranslationOptions):
	fields = ('process',)

translator.register(Work_Process, WorkProcessTranslationOptions)



class ClientTranslationOptions(TranslationOptions):
	fields = ('client_name','review_message',)

translator.register(Client, ClientTranslationOptions)
class Contact_introTranslationOptions(TranslationOptions):
	fields = ('header', 'body',)

translator.register(Contact_intro, Contact_introTranslationOptions)
class Client_introTranslationOptions(TranslationOptions):
	fields = ('header', 'body',)

translator.register(Client_intro, Client_introTranslationOptions)


class Team_introTranslationOptions(TranslationOptions):
	fields = ('title', 'about_team',)
translator.register(Team_intro, Team_introTranslationOptions)

class TeamTranslationOptions(TranslationOptions):
	fields = ('name','position',)

translator.register(Team, TeamTranslationOptions)

class CtsTranslationOptions(TranslationOptions):
	fields = ('title', 'text',)

translator.register(Cts, CtsTranslationOptions)