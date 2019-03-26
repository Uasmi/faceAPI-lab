# Personal Marketing build on Azure Face API

Before start, you need to clone this repo either by downloading zip file or cloning with git.

You will also need **Python 3.7**, **Anaconda** and **Azure Subscription** to run this example.

## Installing Python 3.7 and setting up virtual environment 
##### Downloading miniconda:

To download miniconda go here and grab 3.7 installation package:

https://docs.conda.io/en/latest/miniconda.html

After the installation is completed run Anaconda Promt as administrator.
First, we need to setup virtual environment, which we will use to install packages for python required for this app to work.

To do that, run:

```conda create -n testvirtualenv Python=3.7```

Press *y* to install required packages. 
<br/>

##### (Optional) Installing Visual Studio Code:
You will also need andIDE or code editor (like Sublime) to change variable values.
In this example we use VS Code (it's free), which you can grab here:

https://code.visualstudio.com/

Then, install Python Extension:

https://marketplace.visualstudio.com/items?itemName=ms-python.python

<br/>

##### Setting up the environment:

Lets get back to Anaconda Promt to activate virtual environment:

```conda activate testvirtualenv```

To install the required modules, we need to ```cd``` to the path of repository (which you either cloned or downloaded). Run 

```cd``` + your path to folder

Then run:

```pip install -r requirements.txt```

This will install required modules.

<br/>

##### Setting up Face API and Blob Storage:
Now we will need to setup our Services in Azure.
Face API will handle the matching between users and adverts, and blob storage will store advertising data.

```subscription_key: "#"```

```blobAccountKey: '#'```


Переходим в файл key.py и изменяем поля на значения выше, **оставляя кавычки** 


##### Первый запуск приложения:
Для того чтобы запустить приложение, нужно удостовериться, что ваша вебкамера не заклеена.
Для запуска приложения достаточно нажать F5 в VS Code.

Вам будет предложено добавить свое лицо в библиотеку лиц. Для этого нужно нажать *y*

![alt text](https://recruitlab.blob.core.windows.net/recruitlabblob/question_1.JPG)


Далее для правильной работы приложения, необходимо добавить картинку продукта, который вы хотите купить. Находим его в google, жмем copy link location и вставляем в терминал. 
**Убедитесь, что ссылка заканчивается на .jpg или другое разрешение изображений**
Если вы не хотите решать мы подготовили для вас ссылку:

```https://i.livelib.ru/boocover/1000117421/200/a0de/Vladimir_Levi__Lekarstvo_ot_leni.jpg```

При удачном добавлении лица, вы увидите ID вашего лица.



