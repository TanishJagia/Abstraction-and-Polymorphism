class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most spoken language in India.")
    def type(self):
        print("India is a developing country.")
class Australia():
    def capital(self):
        print("Canberra is the capital of Australia.")
    def language(self):
        print("English is the most spoken language in Australia.")
    def type(self):
        print("Australia is a developed country.")
obj_ind = India()
obj_aus = Australia()

for country in (obj_ind, obj_aus):
    country.capital()
    country.language()
    country.type()