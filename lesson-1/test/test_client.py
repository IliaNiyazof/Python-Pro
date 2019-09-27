from client import create_presence, process_response_ans
from common.functions import *
import unittest


# Тесты
class TestClass(unittest.TestCase):
    # Корректное принятие запроса
    def test_presence(self):
        test = create_presence()
        test[TIME] = 1.0
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.0, USER: {ACCOUNT_NAME: 'User'}})

    # Проверка ответа 200
    def test_200(self):
        self.assertEqual(process_response_ans({RESPONSE: 200}), '200 : OK')

    # Тест без поля RESPONSE
    def test_no_response(self):
        self.assertRaises(ValueError, process_response_ans, {ERROR: 'Плохое соединение'})

    # Тест проверки ответа 400
    def test_400(self):
        self.assertEqual(process_response_ans({RESPONSE: 400, ERROR: 'Плохое соединение'}), '400 : Плохое соединение')


if __name__ == '__main__':
    unittest.main()
