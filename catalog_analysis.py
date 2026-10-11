import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },  # noqa: E501
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    if not movies:
        return 0
    ratings = [m["rating"] for m in movies]
    return round(sum(ratings) / len(ratings), 1)


def catalog_age_stats(movies, current_year=2026):
    if not movies:
        return (0, 0, 0)
    ages = [current_year - m["year"] for m in movies]
    max_age = max(ages)
    min_age = min(ages)
    avg_age = math.ceil(sum(ages) / len(ages))
    return (max_age, min_age, avg_age)


def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо" if rating < 9 else "шедевр"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо"


def decade_label(year):
    match year:
        case y if y > 2020:
            return "новые"
        case y if y >= 2015:
            return "недавние"
        case _:
            return "старые"

def count_long_movies(movies, threshold=120):
    count = 0
    for m in movies:
        if m["duration_min"] > threshold:
            count += 1
    return count

def normalize_title(title):
    words = title.split()
    result = []
    for word in words:
        fixed = word[0].upper() + word[1:]
        result.append(fixed)
    return " ".join(result)

def make_slug(title):
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    genres = ", ".join(sorted(movie["genres"])) 
    return f"'{movie['title']}' ({movie['year']}) — {movie['rating']}/10, {duration_in_hours(movie['duration_min'])}, жанры: {genres}"   # noqa: E501

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key = lambda m: m["rating"], reverse= True)
    return [m["title"] for m in sorted_movies] 

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key = lambda m: m["rating"], reverse= True)
    top = sorted_movies[: n]
    return [(m["title"], m["rating"]) for m in top]

def count_by_genre(movies):
    counts = {}
    for m in movies:
        for genre in m["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
        return counts

def actor_filmography(movies):
    filmography = {}
    for m in movies:
        for actor in m["actors"]:
            filmography.setdefault(actor, []).append(m["title"])
    return filmography

def dict_comp_movies(movies):
    avg = average_rating(movies)
    return {m["title"]: m["rating"] for m in movies if m["rating"] > avg}

def all_genres(movies):
    result = set()
    for m in movies:
        result = result | m["genres"]
    return result

def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])

def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)    

def iter_high_rated(movies, min_rating=8.0):
    for m in movies:
        if m["rating"] >= min_rating:
            yield m
      



def main():
    print("Hello from catalog_analysis.py!")

    for m in movies:
        if "comedy" in m["genres"]:
            continue
        print(m["title"])

    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print("Первый шедевр:", movies[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")

    print("Длинных фильмов (>120 мин):", count_long_movies(movies)) 
    
    print("Нормализация")
    print(normalize_title("silent hours"))
    
    print("Слаги")
    print(make_slug("Silent Hours")) 
    
    print("Отчёт")
    print(format_report_line(movies[7])) 

    print("Сортировка по рейтингу") 
    print(titles_sorted_by_rating(movies))

    print("Топ-3")
    print(top_n_by_rating(movies, 3))

    print("По жанрам")
    print(count_by_genre(movies))

    print("Фильмография")
    print(actor_filmography(movies))

    print("Выше среднего")
    print(dict_comp_movies(movies))

    print("Все жанры")
    print(all_genres(movies))

    print("Общие актёры")
    print(common_actors(movies[0], movies[3]))

    print("Жанры в одном")
    print((genres_only_in_one(movies[5:6], movies[:5])))

    print("Фильмы с рейтингом ≥ 8.0")
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))

    print("Суммарная длительность (>7)")    
    total = sum(m["duration_min"] for m in movies if m["rating"] > 7)
    print(total)

if __name__ == "__main__":
    main()
