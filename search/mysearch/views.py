from django.shortcuts import render
from django.http import JsonResponse
import json
...

# def get_places(request):
#   if request.is_ajax():
#     q = request.GET.get('term', '')
#     places = Place.objects.filter(city__icontains=q)
#     results = []
#     for pl in places:
#       place_json = {}
#       place_json = pl.city + "," + pl.state
#       results.append(place_json)
#     data = json.dumps(results)
#   else:
#     data = 'fail'
#   mimetype = 'application/json'
#   return HttpResponse(data, mimetype)

def autocomplete(request):
    max_items = 5
    q = request.GET.get('q')
    if q:
        sqs = SearchQuerySet().autocomplete(text_auto=q)
        results = [str(result.object) for result in sqs[:max_items]]
    else:
        results = []

    return JsonResponse({'results': results})
