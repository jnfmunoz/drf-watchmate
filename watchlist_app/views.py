# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse

# # Create your views here.
# def movie_list(request):
#     movies = Movie.objects.all()
#     #print('movies')
#     data = {
#                 'movies' : list(movies.values())
#             }
#     return JsonResponse(data)

# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name': movie.name,
#         'descripition' : movie.description,
#         'active' : movie.active,
#     }
#     #print(movie)
#     return JsonResponse(data)