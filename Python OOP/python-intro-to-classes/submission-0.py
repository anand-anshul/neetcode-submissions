class Pet:
    def __init__(self, name, species):
        self.name=name
        self.species=species
cat=Pet("Fluffy", "cat")
print(f"My pet is a {cat.species} named {cat.name}")