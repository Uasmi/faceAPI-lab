# faceAPI-lab: Персонализированный рекламный контент

Перед началом лабораторной работы, вам нужно склонировать этот репозиторий себе на компьютер. Для этого нажмите кнопку **Clone or Download** и скачайте zip файл.
Распакуйте файл в удобное вам место.

## Установка Python 3.7 и подготовка virtual environment
##### Скачиваем miniconda:

Для установки Python и нужных нам модулей удобно использовать package manager. Самый популярный среди них - Anaconda.
Мы будем использовать упрощенную и бесплатную версию - Miniconda.
Нам нужно скачать его под Python 3.7, по этой ссылке: 

https://docs.conda.io/en/latest/miniconda.html

Далее следуем по пути установки и **не забываем добавить Minconda в PATH**:
![alt text](https://cdn-images-1.medium.com/max/1412/1*7a9zVyGP3iMXu9aB4e_Vhw.png)

После завершения установки, находим папку **Anaconda3** через пуск и запускаем **Anaconda Promt** в режиме администратора.

Первое, что нам нужно сделать это создать virtual environment (виртуальную среду). В эту среду мы будем устанавливать все необходимые библиотеки.

> Для удобной работы с модулями Python, всегда рекомендуется создавать отдельные virtual environmet-ы. Они могут содержать разные версии модулей, или самого Python

Для этого запускаем в консоли команду:

```conda create -n testvirtualenv Python=3.7```

<br/>

##### Скачиваем Visual Studio Code:
Теперь нам надо скачать нашу IDE. В этой лабораторной будем использовать бесплатную VS Code:

https://code.visualstudio.com/

После установки, нам нужно добавить Extension для работы с Python:

https://marketplace.visualstudio.com/items?itemName=ms-python.python

<br/>

##### Добавляем проект в Visual Studio Code:

Для этого нам нужно добавить папку. Жмем File и Add Folder to Workspace, затем выбираем папку, где вы сохранили репозиторий

![alt text](https://recruitlab.blob.core.windows.net/recruitlabblob/add%20folder.jpg)
<br/>

##### Настройка проекта и подготовка библиотек:

Вернемся в Anaconda Promt и запустим следующую команду, чтобы активировать наш virtual environment:

```conda activate testvirtualenv```

Далее, нам нужно найти путь к testvirtualenv. Таким образом, мы укажем visual studio code, в какой именно среде ему стоит работать.
Запускаем в консоли Anaconda Promt следующую команду:

```where python```

После этого в консоли отобразится путь до python.exe.
Копируем его и возвращаемся в VS Code.
Находим файл ```settings.json``` внутри ```.vscode``` и заменяем его на наш путь из консоли. 
Одинарный слэш меняем везде на двойной:

![alt text](https://recruitlab.blob.core.windows.net/recruitlabblob/where_python.JPG)

Теперь нам нужно установить модули, необходимые для работы нашей программы. Названия этих модулей находятся в файле ```requirements.txt```
В терминале Visual Studio Code мы запускаем:
```conda activate testvirtualenv```

```pip install -r requirements.txt```

<br/>

##### Ключи для доступа к ресурсам:
В этой лабораторной мы будем использовать эти ключи:

```subscription_key ```
```blobAccountKey ```


![alt text](https://recruitlab.blob.core.windows.net/recruitlabblob/keys%20correct.JPG)

Переходим в файл key.py и изменяем поля на значения выше, **оставляя кавычки** 


##### Первый запуск приложения:
Для того чтобы запустить приложение, нужно удостовериться, что ваша вебкамера не заклеена.
Для запуска приложения достаточно нажать F5 в VS Code.

Вам будет предложено добавить свое лицо в библиотеку лиц. Для этого нужно нажать *y*

![alt text](https://recruitlab.blob.core.windows.net/recruitlabblob/question_1.JPG)


Далее для правильной работы приложения, необходимо добавить картинку продукта, который вы хотите купить. Находим его в google, жмем copy link location и вставляем в терминал. 
**Убедитесь, что ссылка заканчивается на .jpg или другое разрешение изображений**
Если вы не хотите решать мы подготовили для вас ссылку:

При удачном добавлении лица, вы увидите ID вашего лица.



