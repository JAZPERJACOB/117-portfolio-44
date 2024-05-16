from django.shortcuts import render

# Function-based view
def test_view(request):
    return render(request, 'pages/test.html')

def about_view(request):
    return render(request, 'pages/about.html')

