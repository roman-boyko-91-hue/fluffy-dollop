class Vacancy():
    __slots__ = ('name', 'salary', 'url', 'description')

    def __init__(self, name, salary, url, description):
        self.name = name
        self.salary = self.validate_salary(salary)
        self.url = url
        self.description = description

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def validate_salary(self, value):
        salary_to = value.get("to")
        salary_from = value.get("from")
        if salary_to:
            return salary_to
        elif salary_from:
            return salary_from
        else:
            return 0
