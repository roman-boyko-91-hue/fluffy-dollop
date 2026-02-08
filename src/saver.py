from abc import ABC, abstractmethod
import json
import os


class BaseSaver(ABC):
    @abstractmethod
    def add_vacancy(self, new_vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id):
        pass


class JSONSaver:
    def add_vacancy(self, new_vacancy):
        file_path = 'data/vacancies.json'
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        data.append(new_vacancy)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def delete_vacancy(self, vacancy_id):
        file_path = 'data/vacancies.json'
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = []

        updated_data = [v for v in data if v['id'] != vacancy_id]

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(updated_data, f, indent=4, ensure_ascii=False)


json_saver = JSONSaver()
json_saver.add_vacancy({'id': 1, 'title': 'Python Developer'})
json_saver.delete_vacancy()
