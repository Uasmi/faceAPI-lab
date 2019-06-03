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

For access to the Face API you will need to add the subscription key to the **key.py** keeping the quotes.
```subscription_key: "#"```

And for the blob storage you need to enter the blobAccount key to the **key.py** keeping the quotes as well.
```blobAccountKey: '#'```

# First run 
For the first run you need to make sure that your Web Cam is accessible. Jump to anaconda and run 
``python main.py``







