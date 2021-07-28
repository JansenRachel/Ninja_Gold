from django.shortcuts import redirect, render
from time import gmtime, strftime
import random
# Create your views here.

def index(request):

    if 'current_gold' not in request.session:
        request.session['current_gold'] = 0
        request.session['activities'] = []

    return render(request, "home.html")

def process(request):
    # new_list = request.session['activities']

    time = strftime("%Y/%m/%d %I:%M%p", gmtime())
    print(request.POST['location'])
    if request.POST['location'] == 'farm':
        increase_gold = random.randint(10,20)
        activity = f"Earned {increase_gold} golds from the {request.POST['location']}! ({time})"

    elif request.POST['location'] == 'cave':
        increase_gold = random.randint(5,10)
        activity = f"Earned {increase_gold} golds from the {request.POST['location']}! ({time})"

    elif request.POST['location'] == 'house':
        increase_gold = random.randint(2,5)
        activity = f"Earned {increase_gold} golds from the {request.POST['location']}! ({time})"

    elif request.POST['location'] == 'casino':
        increase_gold = random.randint(-50,50)
        if increase_gold >= 0:
            activity = f"Winner! Winner! Entered a {request.POST['location']} and won {increase_gold} golds! ({time})"
        elif increase_gold < 0:
            activity = f"Entered a {request.POST['location']} and lost {increase_gold*-1} golds... Ouch! ({time})"
    # print (increase_gold)
    request.session['current_gold'] += increase_gold

    # if 'activities' not in request.session:
    #     request.session['activities'] = ['activity']
    # else:
    #     list = request.session['activities']
    #     request.session['activities'].append(activity)
    #     request.session['activities'] = new_list

    # request.session['activities'].append(activity)
    request.session['activities'] = [(activity)] + request.session['activities']

    return redirect("/")

def reset(request):
    request.session.flush()
    return redirect("/")