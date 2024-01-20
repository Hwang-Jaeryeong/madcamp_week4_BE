from django.http import JsonResponse
import requests
import aiohttp
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

def get_fixtures(request):
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

    params = {
        'league': '39',
        'season': request.GET.get('season', '2020'),
        'date': request.GET.get('date', '2021-01-28')
    }
    headers = {
        'X-RapidAPI-Key': '24d52a531dmsh693cfe90d613d38p1a8e61jsn6a752b08adf5',
        'X-RapidAPI-Host': 'api-football-v1.p.rapidapi.com'
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

        # fixture_id 리스트를 추가
        fixture_ids = []
        for fixture in data.get('response', []):
            fixture_id = fixture.get('fixture', {}).get('id', None)
            if fixture_id:
                fixture_ids.append(fixture_id)

        data['fixture_ids'] = fixture_ids

        return JsonResponse(data)
    except requests.exceptions.HTTPError as errh:
        return JsonResponse({"error": f"HTTP Error: {errh}"}, status=500)
    except requests.exceptions.ConnectionError as errc:
        return JsonResponse({"error": f"Error Connecting: {errc}"}, status=500)
    except requests.exceptions.Timeout as errt:
        return JsonResponse({"error": f"Timeout Error: {errt}"}, status=500)
    except requests.exceptions.RequestException as err:
        return JsonResponse({"error": f"Error: {err}"}, status=500)


def get_predictions(request, fixture_id):
    url = 'https://api-football-v1.p.rapidapi.com/v3/predictions'
    params = {'fixture': fixture_id}
    headers = {
        'X-RapidAPI-Key': '24d52a531dmsh693cfe90d613d38p1a8e61jsn6a752b08adf5',
        'X-RapidAPI-Host': 'api-football-v1.p.rapidapi.com'
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        return JsonResponse(data)
    except requests.exceptions.HTTPError as errh:
        return JsonResponse({"error": f"HTTP Error: {errh}"}, status=500)
    except requests.exceptions.ConnectionError as errc:
        return JsonResponse({"error": f"Error Connecting: {errc}"}, status=500)
    except requests.exceptions.Timeout as errt:
        return JsonResponse({"error": f"Timeout Error: {errt}"}, status=500)
    except requests.exceptions.RequestException as err:
        return JsonResponse({"error": f"Error: {err}"}, status=500)