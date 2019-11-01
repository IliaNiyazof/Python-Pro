import sys
import os
from common.variables import *
from common.functions import *
import unittest


class TestSocket:
    def __init__(self, test):
        self.test = test

    # отправка
    def send(self, message_send):
        json_test = json.dumps(self.test)
        self.encoded_message = json_test.encode(ENCODING)
        self.receved_message = message_send

    # получение
    def recv(self, max):
        json_test = json.dumps(self.test)
        return json_test.encode(ENCODING)


class Tests(unittest.TestCase):
    test_send = {
        ACTION: PRESENCE,
        TIME: 1.0,
        USER: {
            ACCOUNT_NAME: 'test'
        }
    }
    test_recv_ok = {RESPONSE: 200}
    test_recv_err = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    # тестируем корректность работы фукции отправки
    def test_send_message(self):
        test_socket = TestSocket(self.test_send)
        # вызов тестируемой функции
        send_message(test_socket, self.test_send)
        # проверка корретности кодирования словаря.
        self.assertEqual(test_socket.encoded_message, test_socket.receved_message)

    # тест функции приёма сообщения
    def test_get_message(self):
        test_socket_ok = TestSocket(self.test_recv_ok)
        test_socket_err = TestSocket(self.test_recv_err)
        # тест расшифровки хорошего словаря
        self.assertEqual(get_message(test_socket_ok), self.test_recv_ok)
        # тест расшифровки плохого словаря
        self.assertEqual(get_message(test_socket_err), self.test_recv_err)


if __name__ == '__main__':
    unittest.main()
