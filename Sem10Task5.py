"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
from subprocess import Popen, PIPE
from chardet import detect

web_res = ['yandex.ru', 'youtube.com']
for i in web_res:
    ping = Popen(['ping', i], stdout=PIPE)
    for j in ping.stdout:
        res = detect(j)
        j = j.decode(res['encoding']).encode('utf8')
        print(j.decode('utf8'))
