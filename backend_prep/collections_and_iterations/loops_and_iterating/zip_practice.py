first_name = ['Tim', 'Olivia', 'Louis', 'Kendrick', 'Ludwig']
last_name = ['McGraw', 'Rodrigo', 'Armstrong', 'Lamar', 'Beethoven']
genre = ['country', 'pop', 'jazz', 'rap', 'classical']

musician = zip(first_name, last_name, genre)
for first_name, last_name, genre in musician:
    print(f'{first_name} {last_name} is a {genre} musician!!')