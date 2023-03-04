from sqlalchemy import desc
from sqlalchemy.sql import func

from db import db_session
from models import Salary


def top_salary(num_rows: int = 10) -> print:
    top_salary = Salary.query.order_by(Salary.salary.desc()).limit(num_rows)

    for s in top_salary:
        print(f"З/п: {s.salary}")


def salary_by_city(city_name: str) -> print:
    top_salary = Salary.query.filter(Salary.city == city_name).order_by(
        Salary.salary.desc()
    )

    print(city_name)
    for s in top_salary:
        print(f"З/п: {s.salary}")


def top_salary_by_domain(domain: str, num_rows: int = 5) -> print:
    top_salary = (
        Salary.query.filter(Salary.email.like(f"%{domain}"))
        .order_by(Salary.salary.desc())
        .limit(num_rows)
    )
    print(domain)
    for s in top_salary:
        print(f"З/п: {s.salary}")


def average_salary() -> print:
    avg_salary = db_session.query(func.avg(Salary.salary)).scalar()
    print(f"Средняя зарплата {avg_salary:.2f}")


def count_distinct_cities() -> print:
    count_cities = db_session.query(Salary.city).group_by(Salary.city).count()
    print(f"Количество городов: {count_cities}")


def top_avg_salary_by_city(num_rows: int = 5) -> print:
    top_salary = (
        db_session.query(Salary.city, func.avg(Salary.salary).label("avg_salary"))
        .group_by(Salary.city)
        .order_by(desc("avg_salary"))
        .limit(num_rows)
    )

    for city, salary in top_salary:
        print(f"Город {city} - з/п {salary:.2f}")


if __name__ == "__main__":
    top_avg_salary_by_city(10)
