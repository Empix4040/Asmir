from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import *

def home(request):
    MainContent_objects = MainContent.objects.get()
    Pansion = PansionNeretva.objects.get()
    Quad = QuadAdvantures.objects.get(id=2)
    Rafting  = RaftingAdrenaline.objects.get()
    Middle =MiddleSection.objects.get()
    FirstOffer = OfferOne.objects.get()
    SecondOffer = OfferTwo.objects.get()
    ThirdOffer = OfferThree.objects.get()
    FourthOffer = OfferFour.objects.get()
    FifthOffer = OfferFive.objects.get()
    FooterSection = Footer.objects.get()
    Phone = PhoneNumber.objects.get()
   
    if request.method == "POST":
        Full_Name         = request.POST.get('Full_Name')
        Email             = request.POST.get('Email')
        Phone_Number      = request.POST.get('Phone_Number')
        Activity          = request.POST.get('Activity')
        number_of_people  = request.POST.get('number_of_people')
        message           = request.POST.get('message')
        arrival           = request.POST.get('arrival')
        transmision = ""
        if Full_Name:
            SmallTitle = "Thank you for choosing us!"
            MainDescription = "We will call you shortly!"
        else:
            SmallTitle = MainContent_objects.TitleSmall
            MainDescription = MainContent_objects.Content
        if len(arrival) < 1:
            transmision = f"{Full_Name} has reserved {Activity} for {number_of_people} people, \n  His number is {Phone_Number} \n Guest will arrive at {arrival}"
        else:
            transmision =  f"{Full_Name} has reserved {Activity} for {number_of_people} people, \n  His number is {Phone_Number} \n Guest will arrive at {arrival} and guest said \n{message}"
        send_mail(
            "NEW RESERVATION",
            transmision,
            Email,
            ["emir.m.4040@gmail.com"],

        )
        return render(request, 'index.html', {

        "MainTitle": MainContent_objects.Title,
        "SmallTitle": SmallTitle,
        "MainDescription": MainDescription,
        "PansionTitle": Pansion.Title,
        "PansionOpenGallery": Pansion.Link,
        "PansionContent": Pansion.Content,
        "QuadTitle": Quad.Title,
        "QuadOpenGallery": Quad.Link,
        "QuadContent": Quad.Content,
        "RaftingTitle": Rafting.Title,
        "RaftingOpenGallery": Rafting.Link,
        "RaftingContent": Rafting.Content,
        "MiddleSectionTitle": Middle.Title,
        "MiddleSectionContent": Middle.Content,
        "FirstOfferTitle": FirstOffer.Title,
        "FirstOfferPrice": FirstOffer.Price,
        "FirstOfferContent1": FirstOffer.Content1,
        "FirstOfferContent2": FirstOffer.Content2,
        "FirstOfferContent3": FirstOffer.Content3,
        "FirstOfferContent4": FirstOffer.Content4,
        "FirstOfferContent5": FirstOffer.Content5,
        "FirstOfferContent6": FirstOffer.Content6,
        "FirstOfferContent7": FirstOffer.Content7,
        "FirstOfferContent8": FirstOffer.Content8,
        "SecondOfferTitle": SecondOffer.Title,
        "SecondOfferPrice": SecondOffer.Price,
        "SecondOfferContent1": SecondOffer.Content1,
        "SecondOfferContent2": SecondOffer.Content2,
        "SecondOfferContent3": SecondOffer.Content3,
        "SecondOfferContent4": SecondOffer.Content4,
        "SecondOfferContent5": SecondOffer.Content5,
        "SecondOfferContent6": SecondOffer.Content6,
        "SecondOfferContent7": SecondOffer.Content7,
        "SecondOfferContent8": SecondOffer.Content8,
        "ThirdOfferTitle": ThirdOffer.Title,
        "ThirdOfferPrice": ThirdOffer.Price,
        "ThirdOfferContent1": ThirdOffer.Content1,
        "ThirdOfferContent2": ThirdOffer.Content2,
        "ThirdOfferContent3": ThirdOffer.Content3,
        "ThirdOfferContent4": ThirdOffer.Content4,
        "ThirdOfferContent5": ThirdOffer.Content5,
        "ThirdOfferContent6": ThirdOffer.Content6,
        "ThirdOfferContent7": ThirdOffer.Content7,
        "ThirdOfferContent8": ThirdOffer.Content8,
        "FourthOfferTitle": FourthOffer.Title,
        "FourthOfferPrice": FourthOffer.Price,
        "FourthOfferContent1": FourthOffer.Content1,
        "FourthOfferContent2": FourthOffer.Content2,
        "FourthOfferContent3": FourthOffer.Content3,
        "FourthOfferContent4": FourthOffer.Content4,
        "FourthOfferContent5": FourthOffer.Content5,
        "FourthOfferContent6": FourthOffer.Content6,
        "FourthOfferContent7": FourthOffer.Content7,
        "FourthOfferContent8": FourthOffer.Content8,
        "FifthOfferTitle": FifthOffer.Title,
        "FifthOfferPrice": FifthOffer.Price,
        "FifthOfferContent1": FifthOffer.Content1,
        "FifthOfferContent2": FifthOffer.Content2,
        "FifthOfferContent3": FifthOffer.Content3,
        "FifthOfferContent4": FifthOffer.Content4,
        "FifthOfferContent5": FifthOffer.Content5,
        "FifthOfferContent6": FifthOffer.Content6,
        "FifthOfferContent7": FifthOffer.Content7,
        "FifthOfferContent8": FifthOffer.Content8,
        "FooterTitle": FooterSection.Title,
        "FooterContent": FooterSection.Content,
        "PhoneDigits": Phone.number,
            })
    else:
        return render(request, 'index.html', {
        "MainTitle": MainContent_objects.Title,
        "SmallTitle": MainContent_objects.TitleSmall,
        "MainDescription": MainContent_objects.Content,
        "PansionTitle": Pansion.Title,
        "PansionOpenGallery": Pansion.Link,
        "PansionContent": Pansion.Content,
        "QuadTitle": Quad.Title,
        "QuadOpenGallery": Quad.Link,
        "QuadContent": Quad.Content,
        "RaftingTitle": Rafting.Title,
        "RaftingOpenGallery": Rafting.Link,
        "RaftingContent": Rafting.Content,
        "MiddleSectionTitle": Middle.Title,
        "MiddleSectionContent": Middle.Content,
        "FirstOfferTitle": FirstOffer.Title,
        "FirstOfferPrice": FirstOffer.Price,
        "FirstOfferContent1": FirstOffer.Content1,
        "FirstOfferContent2": FirstOffer.Content2,
        "FirstOfferContent3": FirstOffer.Content3,
        "FirstOfferContent4": FirstOffer.Content4,
        "FirstOfferContent5": FirstOffer.Content5,
        "FirstOfferContent6": FirstOffer.Content6,
        "FirstOfferContent7": FirstOffer.Content7,
        "FirstOfferContent8": FirstOffer.Content8,
        "SecondOfferTitle": SecondOffer.Title,
        "SecondOfferPrice": SecondOffer.Price,
        "SecondOfferContent1": SecondOffer.Content1,
        "SecondOfferContent2": SecondOffer.Content2,
        "SecondOfferContent3": SecondOffer.Content3,
        "SecondOfferContent4": SecondOffer.Content4,
        "SecondOfferContent5": SecondOffer.Content5,
        "SecondOfferContent6": SecondOffer.Content6,
        "SecondOfferContent7": SecondOffer.Content7,
        "SecondOfferContent8": SecondOffer.Content8,
        "ThirdOfferTitle": ThirdOffer.Title,
        "ThirdOfferPrice": ThirdOffer.Price,
        "ThirdOfferContent1": ThirdOffer.Content1,
        "ThirdOfferContent2": ThirdOffer.Content2,
        "ThirdOfferContent3": ThirdOffer.Content3,
        "ThirdOfferContent4": ThirdOffer.Content4,
        "ThirdOfferContent5": ThirdOffer.Content5,
        "ThirdOfferContent6": ThirdOffer.Content6,
        "ThirdOfferContent7": ThirdOffer.Content7,
        "ThirdOfferContent8": ThirdOffer.Content8,
        "FourthOfferTitle": FourthOffer.Title,
        "FourthOfferPrice": FourthOffer.Price,
        "FourthOfferContent1": FourthOffer.Content1,
        "FourthOfferContent2": FourthOffer.Content2,
        "FourthOfferContent3": FourthOffer.Content3,
        "FourthOfferContent4": FourthOffer.Content4,
        "FourthOfferContent5": FourthOffer.Content5,
        "FourthOfferContent6": FourthOffer.Content6,
        "FourthOfferContent7": FourthOffer.Content7,
        "FourthOfferContent8": FourthOffer.Content8,
        "FifthOfferTitle": FifthOffer.Title,
        "FifthOfferPrice": FifthOffer.Price,
        "FifthOfferContent1": FifthOffer.Content1,
        "FifthOfferContent2": FifthOffer.Content2,
        "FifthOfferContent3": FifthOffer.Content3,
        "FifthOfferContent4": FifthOffer.Content4,
        "FifthOfferContent5": FifthOffer.Content5,
        "FifthOfferContent6": FifthOffer.Content6,
        "FifthOfferContent7": FifthOffer.Content7,
        "FifthOfferContent8": FifthOffer.Content8,
        "FooterTitle": FooterSection.Title,
        "FooterContent": FooterSection.Content,
        "PhoneDigits": Phone.number,
        
        })

def rafting(request): 
    GalleryRafting = RaftingGallery.objects.get()
    return render(request, 'rafting.html', {
    "GalleryRafting": GalleryRafting,
    })
def quad(request):
    GalleryQuad = QuadGallery.objects.get()
    return render(request, 'quad.html', {
    "GalleryQuad": GalleryQuad,
    })
def pansion(request):
    GalleryPansion = PansionGallery.objects.get()
    return render(request, 'pansion.html', {
    "GalleryPansion": GalleryPansion,
    })

