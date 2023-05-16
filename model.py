import json

class Recept:
    def __init__(self, name, author, type, description, link, ingredients, cuisine):
        self.name = name
        self.author = author
        self.type = type
        self.description = description
        self.link = link
        self.ingredients = ingredients
        self.cuisine = cuisine

    def __str__(self):
        return f'{self.name} - {self.type}'

class DecodeError(Exception):
    print('Error')

class Model:
    def __init__(self):
        self.filepath = 'db.txt'
        self.__recepts = {}
        try:
            self.data = json.load(open(self.filepath, 'r', encoding='utf-8'))
            for recept in self.data.values():
                self.__recepts[f'{recept["name"]} {recept["type"]}'] = Recept(*recept.values())
        except json.JSONDecodeError:
            raise DecodeError
        except FileNotFoundError:
            with open(self.filepath, 'w') as f:
                f.write('{}')

    @property
    def recepts(self):
        return self.__recepts

    def save_recepts(self):
        dict_recepts = {rec.name: rec.__dict__ for rec in self.__recepts.values()}
        json.dump(dict_recepts, open(self.filepath, 'w', encoding='utf-8'))

    def add_new_recept(self, recept_data):
        new_recept = Recept(*recept_data.values())
        self.__recepts[f'{new_recept.name} {new_recept.type}'] = new_recept
        self.save_recepts()

    def find_recepts(self, criteria):
        recepts = []
        for recept in self.__recepts.values():
            for crit in criteria:
                if recept in recepts:
                    break
                for prop in recept.__dict__.values():
                    if crit.lower() in prop.lower():
                        recepts.append(recept)
                        break

        return recepts

    def delete_recept(self, recepts):
        if len(recepts) == 0:
            return "Такой рецепт не был найден!"
        elif len(recepts) == 1:
            recept = recepts[0]
            key = f'{recept.name} {recept.type}'
            self.__recepts.pop(key)
            self.save_recepts()
            return 'Рецепт был удалён!'
        else:
            return 'Слишком много рецептов'
        