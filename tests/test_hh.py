import os
import json
import pytest


def test_add_vacancy(setup_saver):
    """Тестируем метод добавления вакансии"""
    saver = setup_saver
    vacancy = {'id': 1, 'title': 'Python Developer'}
    saver.add_vacancy(vacancy)

    with open(saver._JSONSaver__file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)

    assert len(data) == 1
    assert data[0]['id'] == 1
    assert data[0]['title'] == 'Python Developer'


def test_delete_vacancy(setup_saver):
    """Тестируем метод удаления вакансии"""
    saver = setup_saver
    vacancy = {'id': 1, 'title': 'Python Developer'}
    saver.add_vacancy(vacancy)
    saver.delete_vacancy(1)

    with open(saver._JSONSaver__file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)

    assert len(data) == 0
