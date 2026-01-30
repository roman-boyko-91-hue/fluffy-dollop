from abc import ABC, abstractmethod

import requests


class HeadHunterAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class Vacancy(HeadHunterAPI):
    def get_vacancies(self, query, area, pages):
        url = "https://api.hh.ru/vacancies"
        vacancies = []
        for page in range(pages):
            params = {
                'text': query,
                'area': area,
                'page': page,
                'per_page': 100
            }

            headers = {
                'User-Agent': 'MyHHScanner/1.0 (email@example.com)'
            }

            response = requests.get(url, params=params, headers=headers)
            if response.status_code == 200:
                data = response.json()
                vacancies.extend(data.get('items', []))
                if page >= data.get('pages', 1) - 1:
                    break
            else:
                print(f"Ошибка: {response.status_code}")
                break
        return vacancies

    @staticmethod
    def cast_to_object_list(hh_vacancies):
        return hh_vacancies


vacancy_api = Vacancy()
query = "Python"
area = 1
pages = 1
hh_vacancies = vacancy_api.get_vacancies(query, area, pages)
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)


class JSONSaver:
    def add_vacancy(self, vacancy):
        # Логика для добавления вакансии в JSON-файл
        pass

    def delete_vacancy(self, vacancy):
        # Логика для удаления вакансии из JSON-файла
        pass


json_saver = JSONSaver()
json_saver.add_vacancy()
json_saver.delete_vacancy()


def filter_vacancies(vacancies, filter_words):
    """Фильтрует вакансии по списку ключевых слов."""
    filtered = []
    for vacancy in vacancies:
        if any(word.lower() in vacancy['description'].lower() for word in filter_words):
            filtered.append(vacancy)
            return filtered


def get_vacancies_by_salary(vacancies, salary_range):
    """Возвращает вакансии, зарплата которых входит в заданный диапазон."""
    min_salary, max_salary = map(int, salary_range.split('-'))
    return [vacancy for vacancy in vacancies if min_salary <= vacancy['salary'] <= max_salary]


def sort_vacancies(vacancies, key='salary'):
    """Сортирует вакансии по указанному ключу (например, по зарплате)"""
    return sorted(vacancies, key=lambda x: x[key], reverse=True)


def get_top_vacancies(vacancies, top_n):
    """Возвращает топ N вакансий."""
    return vacancies[:top_n]


def print_vacancies(vacancies):
    """Выводит информацию о вакансиях."""
    for vacancy in vacancies:
        print(f"Название: {vacancy['title']}, Зарплата: {vacancy['salary']}, Описание: {vacancy['description']}")


def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")


ranged_vacancies = get_vacancies_by_salary(sort_vacancies, salary_range)
sorted_vacancies = sort_vacancies(ranged_vacancies)
top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
print_vacancies(top_vacancies)

if __name__ == "__main__":
    user_interaction()
