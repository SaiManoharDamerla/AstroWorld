from django.contrib import messages, auth
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
import random
import json
import requests  # Add this line
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from .models import Register

from .models import Register, Contact, Userdetails, Feedback


# home page
def navbar(request):
    return render(request, "navbar.html")


def signup(request):
    return render(request, "signup.html")


def contactus(request):
    return render(request, "contactus.html")


def feedback(request):
    return render(request, "feedback.html")


def home(request):
    return render(request, "home.html")


def aboutus(request):
    return render(request, "aboutus.html")


def loader(request):
    return render(request, "loader.html")


def services(request):
    return render(request, "services.html")


def forgotpass(request):
    return render(request, "forgotpass.html")


def rashichart(request):
    return render(request, "rashichart.html")


def horoscope(request):
    return render(request, "horoscope.html")


def zodiacsign(request):
    return render(request, "zodiacsign.html")


def profile(request):
    email = request.session.get('email')
    data = Userdetails.objects.filter(email=email).first()
    print(data)
    return render(request, "profile.html", {'data': data})


def userdetails(request):
    return render(request, "userdetails.html")


def checksignup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        reg = Register(name=name, password=password, email=email)
        reg.save()
        messages.info(request, "Email registered Successfully")
        return render(request, "signup.html")


def checksignin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        login = Register.objects.filter(Q(email=email) & Q(password=password)).first()
        # login = authenticate(request, email=email, password=password)

        if login:
            request.session['email'] = email
            if login.details:
                return redirect('home')
            else:
                return render(request, "userdetails.html", {'email': email})
        else:
            messages.info(request, "Email not registered")
            return render(request, "signup.html")


def generate_otp():
    otp = ""
    for _ in range(4):
        otp += str(random.randint(0, 9))
    return otp


def checkforgot(request):
    if request.method == "POST":
        email = request.POST.get('email')
        print(email)
        try:
            value = Register.objects.get(email=email)
            # print(value)
            if value:
                otp = generate_otp()
                request.session["otp"] = otp
                subject = 'Your OTP for the change Password'
                message = "otp:" + otp
                request.session['femail'] = email
                send_mail(subject, message, 'damerla.vsrs.manohar@gmail.com', [email], fail_silently=False)
                return render(request, "otpverify.html")
        except Register.DoesNotExist:
            messages.info(request, "Email not registered")
            return render(request, "signup.html")
        except Exception as e:
            print(e)  # Print the actual exception for debugging purposes
            return HttpResponse("An error occurred")


def checkotp(request):
    if request.method == "POST":
        userotp = request.POST["userotp"]
        otp = request.session["otp"]

        print(otp, userotp)
        if userotp == otp:
            return render(request, 'changepass.html')
        else:
            messages.info(request, "Otp MisMatch")
            return render(request, "otpverify.html")


def changepass(request):
    if request.method == "POST":
        newpassword = request.POST.get('newPassword')
        confirmPassword = request.POST.get('confirmPassword')
        femail = request.session['femail']
        print(newpassword, confirmPassword)
        if newpassword == confirmPassword:
            user = Register.objects.get(email=femail)
            user.password = newpassword
            user.save()
            return render(request, 'signup.html')
        else:
            messages.info(request, "Password MisMatch")
            return render(request, "changepass.html")


def checkcontact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages.info(request, "We Will Contact you soon !!")
        return redirect('contactus')


def checkuserdetails(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        postalcode = request.POST.get('postalcode')
        try:
            user = Userdetails(
                username=username,
                email=email,
                fname=fname,
                lname=lname,
                address=address,
                city=city,
                country=country,
                postalcode=postalcode
            )
            user.save()
            check = Register.objects.get(email=email)
            check.details = True
            check.save()
        except:
            pass

        return redirect('home')


Rasi = None  # Declare Rasi as a global variable


def rasi(request):
    global Rasi
    if request.method == "POST":
        year = int(request.POST.get('year'))
        month = int(request.POST.get('month'))
        date = int(request.POST.get('date'))
        hours = int(request.POST.get('hours'))
        minutes = int(request.POST.get('minutes'))

        url = "https://json.freeastrologyapi.com/horoscope-chart-svg-code"
        url1 = "https://json.freeastrologyapi.com/planets"

        payload = json.dumps({
            "year": year,
            "month": month,
            "date": date,
            "hours": hours,
            "minutes": minutes,
            "seconds": 0,
            "latitude": 17.38333,
            "longitude": 78.4666,
            "timezone": 5.5,
            "config": {
                "observation_point": "topocentric",
                "ayanamsha": "lahiri"
            },
            "settings": {
                "observation_point": "topocentric",
                "ayanamsha": "lahiri"
            }
        })

        headers = {
            'Content-Type': 'application/json',
            'x-api-key': 'sVhJNyXEho1paRvj6HgqK61jX3Xfef1xaGkD982m'
        }

        response = requests.post(url, headers=headers, data=payload)
        response1 = requests.post(url1, headers=headers, data=payload)

        if response1.status_code == 200:
            planets_data = response1.json()
            moon_data = [entry.get('Moon', None) for entry in planets_data['output']]
            moon_data = [moon for moon in moon_data if moon is not None]

            if moon_data:
                latest_moon_data = moon_data[-1]
                current_sign = latest_moon_data.get('current_sign')

                if current_sign == 1:
                    Rasi = "Mesha"
                elif current_sign == 2:
                    Rasi = "Vrishabha"
                elif current_sign == 3:
                    Rasi = "Mithuna"
                elif current_sign == 4:
                    Rasi = "Karka"
                elif current_sign == 5:
                    Rasi = "Simha"
                elif current_sign == 6:
                    Rasi = "Kanya"
                elif current_sign == 7:
                    Rasi = "Tula"
                elif current_sign == 8:
                    Rasi = "Vrishchika"
                elif current_sign == 9:
                    Rasi = "Dhanu"
                elif current_sign == 10:
                    Rasi = "Makara"
                elif current_sign == 11:
                    Rasi = "Kumbha"
                elif current_sign == 12:
                    Rasi = "Meena"
            else:
                print("No Moon data available.")

        if response.status_code == 200:
            response_json = response.json()
            svg_data = response_json.get("output", "")
            # print(Rasi)
            if svg_data:
                return render(request, "userinput.html", {"svg_data": svg_data, "planets_data": Rasi})

        return render(request, "rasichart.html", {"svg_data": None, "planets_data": None})


def input(request):
    return render(request, "userinput.html")


def submit_feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        rating = request.POST.get('rating')
        feedback_form = Feedback(name=name, email=email, feedback=feedback, rating=rating)
        feedback_form.save()
        messages.info(request, "FeedBack Submitted Successfully")
        return redirect('feedback')