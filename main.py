from src.classes import DBManager
from src.database import create_db, execute_sql_script, insert_data
from src.employers import get_data_employers, get_vacancies
from src.utils import config


def main():
    url = 'https://api.hh.ru/employers'
    area = '113'  # регион
    db_name = 'head_hunter_db'
    script_file = 'src/queries.sql'
    params = config()

    employers = get_data_employers(url, area)  # получение списка компаний
    vacancies = get_vacancies(employers)  # получение списка вакансий по компаниям

    create_db(params, db_name)  # создание базы данных
    execute_sql_script(params, db_name, script_file)  # создание таблиц в базе данных
    insert_data(params, db_name, employers, vacancies)  # добавление данных в таблицы

    db = DBManager(params, db_name)

    #  Методы для работы с БД
    db.get_companies_and_vacancies_count()  # Показывает все компании и количество вакансий у каждой компании
    # db.get_all_vacancies()  # Показывает все вакансии (назв комп, назв вак, ЗП, ссылки на вакансию)
    # db.get_avg_salary()  # Показывает среднюю зарплату по вакансиям
    # db.get_vacancies_with_higher_salary()  # Показывает все вакансии, у которых зарплата выше средней

    # keyword = 'Менеджер'
    # db.get_vacancies_with_keyword(keyword)  # Показывает все вакансии, в названии которого содержится переданное слово


if __name__ == '__main__':
    main()