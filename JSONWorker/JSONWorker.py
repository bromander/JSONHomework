import json

class JSONWorker:
    def __init__(self, data):
        # Проверим
        if isinstance(data, list) and len(data) == 3 and all(isinstance(d, dict) and len(d) == 2 for d in data):
            self.data = data
        else:
            raise ValueError("Data must be a list of 3 dictionaries, each with 2 key-value pairs.")

    def write_to_file(self, filename):
        """Записывает данные JSON."""
        with open(filename, 'w') as file:
            json.dump(self.data, file, indent=4)
        print(f"Data successfully written to {filename}")

    def read_from_file(self, filename):
        """Читает данные из файла"""
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"Data successfully read from {filename}")
        return data

# Пример использования:
data = [
    {"key1": "value1", "key2": "value2"},
    {"key3": "value3", "key4": "value4"},
    {"key5": "value5", "key6": "value6"}
]

worker = JSONWorker(data)

# Записываем
worker.write_to_file('data.json')

# Читаем
read_data = worker.read_from_file('data.json')
print(read_data)
