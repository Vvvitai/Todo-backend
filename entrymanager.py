from entry import Entry
import os

class EntryManager:
    def __init__(self, data_path: str):
        self.entries = []
        self.data_path = data_path

    def save(self):
        for entry in self.entries:
            entry.save(self.data_path)

    def load(self):
        for file in os.listdir(self.data_path):
            if file.endswith('.json'):
                self.entries.append(Entry.load(os.path.join(self.data_path, file)))

    def add_entry(self, title):
        new_entry = Entry(title)
        self.entries.append(new_entry)


if __name__ == '__main__':
    e_manager = EntryManager('C:\\Users\\vital\\PycharmProjects\\Todo_list')
    e_manager.load()