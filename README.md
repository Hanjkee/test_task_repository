# API Тестирование комментариев

=== Запуск тестов ===

Основные команды:
pytest tests/ --html=reports/pytest/report.html --self-contained-html -v
pytest --cov=src --cov-report=html:reports/coverage tests/

Параметры:
-v - подробный вывод
--cache-clear - очистка кеша