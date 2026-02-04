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
