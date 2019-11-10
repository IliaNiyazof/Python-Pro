import subprocess
import asyncio

process = []


async def function1():
    await asyncio.sleep(3)
    print('Загрузка данных')


async def function2():
    print('Происходит запуск функции')
    await asyncio.sleep(5)
    print('Поехали')
    while True:
        action = input('Выберите действие: q - выход , s - запустить сервер, k - запустить клиенты:')
        if action == 'q':
            break
        elif action == 's':
            # Запускаем сервер!
            process.append(subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))
        elif action == 'k':
            clients_count = int(input('Введите количество тестовых клиентов для запуска: '))
            # Запускаем клиентов:
            for i in range(clients_count):
                process.append(
                    subprocess.call(f'python client.py -n test{i + 1}', shell=True))
                process.append(
                    subprocess.Popen(f'python OpenFile.py -n test{i + 1}', creationflags=subprocess.CREATE_NO_WINDOW))


def mainLoop():
    eloop = asyncio.get_event_loop()
    tasks = [eloop.create_task(function2()), eloop.create_task(function1())]
    wait_tasks = asyncio.wait(tasks)
    eloop.run_until_complete(wait_tasks)
    eloop.close()


mainLoop()
