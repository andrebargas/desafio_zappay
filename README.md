# Desafio Zappay
Desafio para desenvolvedor back-end contemplando consumo do APIs externas.


Como baixar o código da aplicação:
```console
$ git clone https://github.com/andrebargas/desafio_zappay.git
```

Como instalar e rodar o código :
 Há um ambiente virtual no repositório “/venv” construido com o Venv default do Python 3. Caso já tenha o Python 3 e o Venv, os comandos a partir do diretório principal do repositório são :

```console
$ source venv/bin/activate
$ source python manage.py runserver
```

Caso não deseja rodar através do venev e instalar as dependencias :

```console
$ sudo apt-get update
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
$ sudo pip3 install django==2
$ sudo pip install requests && pip install pytest

$ python3 manage.py runserver  
```
