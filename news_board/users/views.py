import requests
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from rest_framework.response import Response


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            if username and password:
                data = {'username': username, 'password': password}
                response = requests.post('http://localhost:8000/api-token-auth/', data=data)
                if response.status_code == 200:
                    token = response.json().get('token')

                    # Сохранение токена в Local Storage
                    storage = request.COOKIES  # Или другой способ доступа к Local Storage
                    storage['token'] = token
                    response = Response(token, status=200)

                    return response
    else:
        form = AuthenticationForm(request)
        return render(request, 'login.html', {'form': form})

    return JsonResponse({'error': 'Invalid credentials'}, status=400)
