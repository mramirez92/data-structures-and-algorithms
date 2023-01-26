from operator import itemgetter
import re

"""
sort movies by year:
use sort method to return sorted list by year.
key uses itemgetter helps extract key values.
return titles only
"""


def sort_movies_by_year(movies):
    movies.sort(key=itemgetter('year'), reverse=True)
    titles = [movie['title'] for movie in movies]
    return titles


"""
sort movies by title:
use sort method to return sorted list by title.
key used is a key derived from helper function get_sort_key
    - uses regex to remove leading a's, an's, the's from title
return sorted titles only
"""


def sort_movies_by_title(movies):
    def get_sort_key(movie):
        sort_key = re.sub(r'^(?:The|An?|A)\s+', '', movie['title'])
        return sort_key

    movies.sort(key=get_sort_key)
    titles = [movie["title"] for movie in movies]
    return titles
