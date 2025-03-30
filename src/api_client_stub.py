"""
Заглушка для корректного анализа покрытия тестов.
Реальный клиент API находится в tests/helpers/api_client.py
"""

class StubClient:
    @staticmethod
    def get_example():
        return True

def dummy_function():
    return 42