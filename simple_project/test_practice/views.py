from django.shortcuts import render

# Create your views here.
def home(req):
  person = {
    'name': 'moin khan',
    'age': 20,
    'designation': 'programmer',
    'languages': ['js', 'c', 'c++', 'py', 'html'],
    'job': ''
  }
  return render(req, "test_practice/index.html", person)