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


class GetLineupPredictions(View):
    def get(self, request, fixture_id):
        url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups'
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

class GetFixtureEvents(View):
    def get(self, request, fixture_id):
        # Get team information
        team_info_url = 'https://api-football-v1.p.rapidapi.com/v3/teams'
        params = {}
        headers = {
            'X-RapidAPI-Key': '24d52a531dmsh693cfe90d613d38p1a8e61jsn6a752b08adf5',
            'X-RapidAPI-Host': 'api-football-v1.p.rapidapi.com'
        }

        try:
            response = requests.get(team_info_url, params=params, headers=headers)
            response.raise_for_status()
            team_data = response.json()

            # Create a dictionary to store yellow and red card counts for each team
            yellow_red_count = {}

            # Get fixture events
            events_url = 'https://api-football-v1.p.rapidapi.com/v3/fixtures/events'
            params = {'fixture': fixture_id}
            response = requests.get(events_url, params=params, headers=headers)
            response.raise_for_status()
            data = response.json()

            # Count yellow and red cards for each team
            for event in data.get('response', []):
                team_name = event.get('team', {}).get('name', '')
                if team_name:
                    if team_name not in yellow_red_count:
                        yellow_red_count[team_name] = {'yellow': 0, 'red': 0}
                    if event.get('type', '') == 'Card':
                        if event.get('detail', '') == 'Yellow Card':
                            yellow_red_count[team_name]['yellow'] += 1
                        elif event.get('detail', '') == 'Red Card':
                            yellow_red_count[team_name]['red'] += 1

            # Convert counts to integers
            for team_name, card_counts in yellow_red_count.items():
                card_counts['yellow'] = int(card_counts['yellow'])
                card_counts['red'] = int(card_counts['red'])

            # Add yellow and red card counts to the response
            data['yellow_red_count'] = yellow_red_count

            return JsonResponse(data)

        except Exception as e:
            return JsonResponse({'error': str(e)})

class GetStandings(View):
    def get(self, request):
        options = {
            'method': 'GET',
            'url': 'https://api-football-v1.p.rapidapi.com/v3/standings',
            'params': {
                'season': request.GET.get('season', '2023'),
                'league': '39'
            },
            'headers': {
                'X-RapidAPI-Key': '24d52a531dmsh693cfe90d613d38p1a8e61jsn6a752b08adf5',
                'X-RapidAPI-Host': 'api-football-v1.p.rapidapi.com'
            }
        }

        try:
            response = requests.request(**options)
            response.raise_for_status()
            data = response.json()
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({'error': str(e)})

def get_top_scorers(request):
    api_url = 'https://api-football-v1.p.rapidapi.com/v3/players/topscorers'
    headers = {
        'X-RapidAPI-Key': '24d52a531dmsh693cfe90d613d38p1a8e61jsn6a752b08adf5',
        'X-RapidAPI-Host': 'api-football-v1.p.rapidapi.com'
    }
    params = {
        'league': '39',
        'season': request.GET.get('season', '2023'),
    }

    try:
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()  # 에러가 발생하면 예외를 일으킵니다.
        data = response.json()

        # 여기에서 API 응답을 가공하고 필요한 데이터를 추출합니다.
        top_scorers = data.get('response', [])

        # 예시: 간단하게 상위 5명의 득점자 이름과 골 수를 가져오는 코드
        top_scorers_info = [{'name': player['player']['name'], 'goals': player['statistics'][0]['goals']} for player in top_scorers[:5]]

        return JsonResponse({'top_scorers': top_scorers_info})
    except requests.exceptions.HTTPError as errh:
        return JsonResponse({'error': f'HTTP Error: {errh}'}, status=500)
    except requests.exceptions.ConnectionError as errc:
        return JsonResponse({'error': f'Error Connecting: {errc}'}, status=500)
    except requests.exceptions.Timeout as errt:
        return JsonResponse({'error': f'Timeout Error: {errt}'}, status=500)
    except requests.exceptions.RequestException as err:
        return JsonResponse({'error': f'Error: {err}'}, status=500)