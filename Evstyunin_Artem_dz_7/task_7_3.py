# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание,
# что html-файлы расположены в родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.
import yaml
import os
with open('config.yaml','r') as f:
    d = yaml.safe_load(f)
    def create_data(data):
        for folder, data_tmps in data.items():
            if not os.path.exists(folder):
                os.mkdir(folder)
            os.chdir(folder)
            for data_tmp in data_tmps:
                if isinstance(data_tmp,dict):
                    create_data(data_tmp)
                else:
                    if not os.path.exists(data_tmp):
                        if '.' in data_tmp:
                            with open(data_tmp,'w') as file:
                                file.write('')
        else:
            os.chdir('../')


create_data(d)
