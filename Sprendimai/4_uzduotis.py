# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget
    def was_expensive(self):
        if self.budget > 1000000:
            return True
        else:
            return False
    def __str__(self):
        return self.title



everything_everywhere = Movie('Everything Everywhere All at Once', 'Kwan, Scheinert', 25000000)
print(everything_everywhere.was_expensive())

niekas_nenorejo = Movie('Niekas nenorėjo mirti', 'V. Žalakevicius', 50000)
print(niekas_nenorejo.was_expensive())
