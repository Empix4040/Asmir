from django.contrib import admin

# Register your models here.
from .models import PansionGallery,QuadGallery,RaftingGallery,PansionNeretva,QuadAdvantures,RaftingAdrenaline,MiddleSection,OfferOne,OfferTwo,OfferThree,OfferFour,OfferFive,Footer,MainContent,PhoneNumber
MyModels = [PansionGallery,QuadGallery,RaftingGallery,PansionNeretva,QuadAdvantures,RaftingAdrenaline,MiddleSection,OfferOne,OfferTwo,OfferThree,OfferFour,OfferFive,Footer,MainContent,PhoneNumber]
admin.site.register(MyModels)