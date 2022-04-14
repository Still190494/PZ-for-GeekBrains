# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида:
# (<remote_addr>, <request_type>, <requested_resource>).
# Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

file = open('nginx_logs.txt','r', encoding='utf-8')
for line in file:
    result = []
    remote_addr = line.split()
    result.append(remote_addr[0])
    request_type = line.split()
    request_type = request_type[5].split('"')
    result.append(request_type[1])
    requested_resource = line.split()
    result.append(requested_resource[6])
    print(result)
file.close()



