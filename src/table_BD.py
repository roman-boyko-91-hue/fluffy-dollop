import psycopg2

db_config = {
    "dbname": "hh_database",
    "user": "postgres",
    "password": "260980",
    "host": "localhost",
    "port": "5432"
}


def create_tables():
    """Создает таблицы для работодателей и вакансий"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS employers (
            employer_id INTEGER PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            url TEXT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS vacancies (
            vacancy_id INTEGER PRIMARY KEY,
            employer_id INTEGER REFERENCES employers(employer_id),
            name VARCHAR(255) NOT NULL,
            salary_from INTEGER,
            salary_to INTEGER,
            currency VARCHAR(10),
            url TEXT
        )
        """
    )

    conn = None
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
        print("Таблицы успешно созданы.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка БД: {error}")
    finally:
        if conn is not None:
            conn.close()


def save_to_db(employers_data, vacancies_data):
    """Сохраняет данные в базу"""
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()

    # Заполнение таблицы работодателей
    for emp in employers_data:
        cur.execute(
            "INSERT INTO employers (employer_id, name, url) VALUES (%s, %s, %s) ON CONFLICT (employer_id) DO NOTHING",
            (emp['id'], emp['name'], emp['url'])
        )

    # Заполнение таблицы вакансий
    for vac in vacancies_data:
        # Обработка зарплаты (может быть None)
        salary = vac.get('salary') or {}
        cur.execute(
            """
            INSERT INTO vacancies (vacancy_id, employer_id, name, salary_from, salary_to, currency, url)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (vacancy_id) DO NOTHING
            """,
            (
                vac['id'], vac['employer_id'], vac['name'],
                salary.get('from'), salary.get('to'), salary.get('currency'),
                vac['url']
            )
        )

    conn.commit()
    cur.close()
    conn.close()
    print("Данные успешно сохранены.")
