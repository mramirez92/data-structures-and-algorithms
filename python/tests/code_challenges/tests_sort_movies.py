import pytest
from code_challenges.sort_movies import sort_movies_by_title, sort_movies_by_year

movies = [
    {
        "title": "Beetlejuice",
        "year": 1988,
        "genres": ["Comedy", "Fantasy"],
    },
    {
        "title": "The Cotton Club",
        "year": 1984,
        "genres": ["Crime", "Drama", "Music"],
    },
    {
        "title": "The Shawshank Redemption",
        "year": 1994,
        "genres": ["Crime", "Drama"],
    },
    {
        "title": "Crocodile Dundee",
        "year": 1986,

        "genres": ["Adventure", "Comedy"],
    },
    {
        "title": "Valkyrie",
        "year": 2008,
        "genres": ["Drama", "History", "Thriller"],
    },
    {
        "title": "Ratatouille",
        "year": 2007,
        "genres": ["Animation", "Comedy", "Family"],
    },
    {
        "title": "City of God",
        "year": 2002,

        "genres": ["Crime", "Drama"],
    },
    {
        "title": "Memento",
        "year": 2000,

        "genres": ["Mystery", "Thriller"],
    },
    {
        "title": "The Intouchables",
        "year": 2011,

        "genres": ["Biography", "Comedy", "Drama"],
    },
    {
        "title": "Stardust",
        "year": 2007,
        "genres": ["Adventure", "Family", "Fantasy"],
    },
]


def test_sort_year():
    m = sort_movies_by_year(movies)
    expected = ['The Intouchables', 'Valkyrie', 'Ratatouille', 'Stardust', 'City of God', 'Memento',
                'The Shawshank Redemption', 'Beetlejuice', 'Crocodile Dundee', 'The Cotton Club']
    assert m == expected


def test_sort_title():
    m = sort_movies_by_title(movies)
    expected = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento",
                "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"];
    assert m == expected


def test_sort_alph():
    list = [
        {
            "title": "Beetlejuice",
            "year": 1988,
            "genres": ["Comedy", "Fantasy"],
        },
        {
            "title": "The Cotton Club",
            "year": 1984,
            "genres": ["Crime", "Drama", "Music"],
        },
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "genres": ["Crime", "Drama"],
        },
        {
            "title": "Crocodile Dundee",
            "year": 1986,
            "genres": ["Adventure", "Comedy"],
        },
    ]

    sorts = sort_movies_by_title(list)
    expected = ['Beetlejuice', 'The Cotton Club', 'Crocodile Dundee', 'The Shawshank Redemption']
    assert sorts == expected

