import json
import os


def print_with_indent(value, indent=0):
    indentation = " " * indent
    print(indentation + str(value))


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = list()
        self.entries = entries
        self.parent = parent
        self.title = title

    def __str__(self):
        return self.title

    @classmethod # это разъеб использование; создание объектов класса особым образом
    def from_json(cls, value: dict):
        new_entry = cls(value['title'])
        for item in value.get('entries', []):
            new_entry.add_entry(cls.from_json(item))
        return new_entry

    def add_entry(self, entry):
        entry.parent = self
        self.entries.append(entry)

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)

    def json(self):
        res = {'title': self.title, 'entries': [entry.json() for entry in self.entries]}
        return res

    def save(self, path):
        file_dir = os.path.join(path, f'{self.title}.json')
        with open(file_dir, 'w') as f:
            json.dump(self.json(), f, indent=2, ensure_ascii=False)

    @classmethod
    def load(cls, path):
        with open(path, 'r') as f:
            return cls.from_json(json.load(f))





def main():
    grocery_entry = Entry('Продукты')
    meat = Entry('Мясное')
    grocery_entry.add_entry(meat)

    sosiki = Entry('Сосиски')
    kolbasa = Entry('Колбаса')
    meat.add_entry(sosiki)
    meat.add_entry(kolbasa)

    with_cheese = Entry('С сыром')
    sosiki.add_entry(with_cheese)

    salami = Entry('Салями')
    kolbasa.add_entry(salami)

    chiken = Entry('Курица')
    salami.add_entry(chiken)


    new_entry = Entry.load('Продукты.json')
    new_entry.print_entries()

if __name__ == '__main__':
    main()
# grocery_entry.save('C:\\Users\\vital\\PycharmProjects\\Todo_list')
# dict_to_json = json.dumps(res, ensure_ascii=False, indent=2) # Не надо преобразовывать в ascii иначе бурда



