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
