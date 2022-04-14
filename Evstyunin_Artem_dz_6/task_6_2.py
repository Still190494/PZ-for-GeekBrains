# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

file = open('nginx_logs.txt','r', encoding='utf-8')
spam = {}
for line in file:
    remote_addr = line.split()
    spam.setdefault(remote_addr[0],0) #Ключ это IP, значение "0"
    spam[remote_addr[0]] += 1 # +1 к значению если оно повторяется
spam_sort = sorted(spam.items(), key=lambda x: x[1]) #сортировка по значению
spammer = spam_sort[-1]
print(spammer)
file.close()