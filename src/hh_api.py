from abc import ABC, abstractmethod

import requests


class BaseAPI(ABC):

    @abstractmethod
    def get_vacancies(self, query, area, pages):
        pass


class HeadHunterApi(BaseAPI):
    def __init__(self, query, area):
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {
            'text': query,
            'area': area,
            'per_page': 100
        }

    def __connect(self, headers):
        response = requests.get(self.__url, params=self.__params, headers=headers)
        response.raise_for_status()
        return response

    def get_vacancies(self, query, area, pages):
        vacancies = []
        for page in range(pages):
            self.__params["page"] = page

            headers = {
                'User-Agent': 'MyHHScanner/1.0 (email@example.com)'
            }

            response = self.__connect(headers)
            if response.status_code == 200:
                data = response.json()
                vacancies.extend(data.get('items', []))
                if page >= data.get('pages', 1) - 1:
                    break
            else:
                print(f"Ошибка: {response.status_code}")
                break
        return vacancies


vacancy_api = HeadHunterApi()
query = "Python"
area = 1
pages = 1
hh_vacancies = vacancy_api.get_vacancies(query, area, pages)
