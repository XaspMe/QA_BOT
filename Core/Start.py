import Core.Controller.DB_Handle as db_handler


"""
Реализовать проверку наличия файла базы данных, если нет вызывать следующий код:
"""
#var = db_handler.Handler()
#var.create_db_and_tables() # создание бд

var = db_handler.Handler()
for x in range(10):
    print(var.add_chatid(107+x, 'Ssutsul'))

"""
Реализовать запуск pool Telegram
"""

"""
Все запросы адресовать в Command handler, 
он должен сам обрабатывать запрос и присылать экземпляр View сюда через (Return).
Возможно требуется создать класс хранящий данные ответа.
"""

"""
Реалазиовать логгирование всех действий этого файла с ротацией логов, путь к логу хранится в файле конфига
"""

