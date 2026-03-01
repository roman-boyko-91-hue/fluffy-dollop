import psycopg2


class DBManager:
    def __init__(self, db_config):
        """Инициализация менеджера с подключением"""
        self.db_config = db_config

    def _execute_query(self, query, params=None):
        """Приватный метод для выполнения запросов"""
        conn = psycopg2.connect(**self.db_config)
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(query, params)
                    return cur.fetchall()
        finally:
            conn.close()

    def get_companies_and_vacancies_count(self):
        """Получение списка всех компаний и количество вакансий у каждой компании"""
        query = """
            SELECT name, COUNT(vacancies.vacancy_id)
            FROM employers
            LEFT JOIN vacancies USING(employer_id)
            GROUP BY employers.name
        """
        return self._execute_query(query)

    def get_all_vacancies(self):
        """Получение списка вакансий (компания, название, зарплата, ссылка)"""
        query = """
            SELECT employers.name, vacancies.name, salary_from, salary_to, vacancies.url
            FROM vacancies
            JOIN employers USING(employer_id)
        """
        return self._execute_query(query)

    def get_avg_salary(self):
        """Получение средней зарплаты по вакансиям"""
        query = "SELECT AVG(salary_from) FROM vacancies WHERE salary_from IS NOT NULL"
        result = self._execute_query(query)
        return result[0][0] if result else 0

    def get_vacancies_with_higher_salary(self):
        """Получение вакансии, зарплата которых выше средней"""
        query = """
            SELECT * FROM vacancies
            WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies WHERE salary_from IS NOT NULL)
        """
        return self._execute_query(query)

    def get_vacancies_with_keyword(self, keyword):
        """Получение списка вакансий по ключевому слову в названии"""
        query = "SELECT * FROM vacancies WHERE LOWER(name) LIKE %s"
        # Используем % для поиска подстроки
        params = (f"%{keyword.lower()}%",)
        return self._execute_query(query, params)
