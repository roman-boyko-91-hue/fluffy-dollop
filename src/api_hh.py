from datetime import time

import requests


def get_employer_id(company_name):
    """Получение данных о работодателях и их вакансиях с сайта hh.ru."""
    url = "https://api.hh.ru/employers"
    params = {
        'text': company_name,
        'only_with_vacancies': True  # Искать только компании с вакансиями
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Проверка на успешность запроса
        results = response.json().get('items', [])

        if results:
            return results[0]['id'], results[0]['name']
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
    return None, None


def get_vacancies_by_employer(employer_id):
    url = "https://api.hh.ru/vacancies"
    params = {
        'employer_id': employer_id,
        'per_page': 20  # Количество результатов на страницу
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Проверка на успешность запроса
        data = response.json()

        vacancies = []
        for item in data.get('items', []):
            vacancies.append({
                'title': item['name'],
                'salary': item.get('salary'),
                'url': item['alternate_url']
            })
        return vacancies
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return []


employer_id, name = get_employer_id("Yandex")

if employer_id:
    vacancies = get_vacancies_by_employer(employer_id)
    for v in vacancies:
        print(f"{v['title']} - {v['url']}")
else:
    print("Работодатель не найден.")

# Список интересующих компаний
COMPANY_NAMES = [
    "Яндекс", "Сбер", "Т-Банк", "VK", "Ozon",
    "Авито", "Kaspersky", "МТС", "Альфа-Банк", "X5 Group"
]


def get_employer_ids(names):
    """Находит ID компаний по их названиям"""
    employer_ids = {}
    url = "https://api.hh.ru"

    for name in names:
        params = {'text': name, 'only_with_vacancies': True}
        # Указываем User-Agent (требование API hh.ru)
        headers = {'User-Agent': 'MyVacancyApp/1.0 (contact@example.com)'}

        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            items = response.json().get('items', [])
            if items:
                # Берем первый результат поиска (самый релевантный)
                employer_ids[items[0]['name']] = items[0]['id']
        time.sleep(0.1)  # Небольшая задержка, чтобы не превышать лимиты
    return employer_ids


def get_vacancies(employer_id):
    """Получает до 5 последних вакансий для конкретного ID работодателя"""
    url = "https://api.hh.ru"
    params = {
        'employer_id': employer_id,
        'per_page': 5,  # Ограничимся 5 вакансиями для примера
        'order_by': 'publication_time'
    }
    headers = {'User-Agent': 'MyVacancyApp/1.0'}

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json().get('items', [])
    return []
