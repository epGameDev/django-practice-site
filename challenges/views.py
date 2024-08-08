from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
"january": "Learn Design, HTML, and CSS",
"february": "Learn Javascript",
"march": "Learn TypeScript",
"april": "Learn React and Redux",
"may": "Learn SQL and PostgreSQL",
"june": "Learn Docker and Kubernetes",
"july": "Learn Algorithms and Data Structures",
"august": "Learn Python and Automation",
"september": "Learn Linux Administration",
"october": "Learn Golang",
"november": "Learn Django",
"december": "Learn Rust",
}


# Create your views here.
def index(request):
  return HttpResponse("Hello World!")


def monthly_challenge_index(request, month):

  try:
    months = list(monthly_challenges.keys())
    month_redirect = months[month - 1]
    return HttpResponseRedirect(redirect_to="/" + month_redirect)
  except:
    return HttpResponseNotFound("This page you are looking for is not found. Check your spelling or contact the site support.")


def monthly_challenge(request, month):

  try:
    challenge_text = monthly_challenges[month]
    return HttpResponse(f'Your challenge for the money: {challenge_text}')
  except:
    return HttpResponseNotFound("This page you are looking for is not found. Check your spelling or contact the site support.")
