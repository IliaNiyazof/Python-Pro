# import sys
# import os
# from server import process_message
# import unittest
# from common.variables import *
#
#
# class TestServer(unittest.TestCase):
#     no_data = {
#         RESPONSE: 400,
#         ERROR: 'Плохое соединение'
#     }
#     yes_data = {RESPONSE: 200}
#
#     #  корректный запрос
#     def test_ok_check(self):
#         self.assertEqual(process_message({ACTION: PRESENCE, TIME: 1.0, USER: {ACCOUNT_NAME: 'User'}}), self.yes_data)
#
#     # Ошибка - нет пользователя
#     def test_no_user(self):
#         self.assertEqual(process_message({ACTION: PRESENCE, TIME: '1.0'}), self.no_data)
#
#     # Ошибка - не User
#     def test_unknown_user(self):
#         self.assertEqual(process_message({ACTION: PRESENCE, TIME: '1.0', USER: {ACCOUNT_NAME: 'Guest'}}), self.no_data)
#
#     # Если нету действий
#     def test_no_actions(self):
#         self.assertEqual(process_message({TIME: 1.0, USER: {ACCOUNT_NAME: 'User'}}), self.no_data)
#
#     # Ошибка, не содержит времени
#     def test_no_time(self):
#         self.assertEqual(process_message({ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'User'}}), self.no_data)
#
#     # Ошибка, неизвестное действие
#     def test_wrong_action(self):
#         self.assertEqual(process_message({ACTION: '', TIME: '1.0', USER: {ACCOUNT_NAME: 'User'}}), self.no_data)
#
#
# if __name__ == '__main__':
#     unittest.main()
