# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
import os
main_folder = 'my_project'                                        #Основная папка
folders = ['settings','mainapp','adminapp','authapp']             #Вложенные папки
starter = [os.makedirs(os.path.join(main_folder,folder))          #Создание папок
for folder in folders if not os.path.exists(os.path.join(main_folder,folder))] #Создавать если нету
