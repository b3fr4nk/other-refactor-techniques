# by Kami Bigdely
# Extract class

class Actor:
    """Represents an actor"""

    def __init__(self, first_name, last_name, email, birth_year, movies):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birth_year = birth_year
        self.movies = movies

    def send_hiring_email(self):
        """Print hiring email confirmation message"""
        print(f'sent email to: {self.email}')

    def __repr__(self):
        movies_string = ''
        for movie in self.movies:
            movies_string += f'{movie}\n'
        return f'{self.first_name}, {self.last_name}\n Movies Played: {movies_string}'


first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],
          ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

for i, value in enumerate(emails):
    actor = Actor(first_names[i], last_names[i],
                  value, birth_year[i], movies[i])
    if birth_year[i] > 1985:
        # print(first_names[i], last_names[i])
        # print('Movies Played: ', end='')
        # for m in movies[i]:
        #     print(m, end=', ')
        # print()
        print(actor)
        actor.send_hiring_email()
