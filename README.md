# miniProject

## Project Introduction
This is a mini Django project in preparation for the 2022/23 Honours Project, presenting (1) an Intraday Candlestick Graph for S&P 500 Index at 5-min interval (2) Spider-web graph/ Radar map (3) Daily Close prices for S&P 500 stocks in information technology and financials sector Graph. 

## Authors

Hailey, Sami, Yong

## Project directory structure
```text
MiniProject
  |-- MiniProject
        |-- MiniProject (Django project settings)
              |-- asgi.py
              |-- settings.py
              |-- urls.py
              |-- wsgi.py
        |-- static (Data Collection files)
              
        |-- visual (Django app)
              |-- apps.py
              |-- views.py (website views)
  |-- .env
  |-- manage.py
```
## Package choices and justification


**Yong**:  Responsible for Django set-up, Intraday Candlestick Graphs.
I initiated the website with django-echarts, a web scaffolding tool that integrates Pyechart to new Django projects. I then created the Intraday Candlestick Graph for S&P 500 Index with Pyechart, I chose Pyechart over other packages because it's quick to write and it supports dynamic, interactive graphs with creative theme palate. I wish to create 3D visuals and discover more possibilities for better data visualisation in the actual project. 

**Hailey**: Responsible for live web scraping and data collection.
```txt
Collecting data: I intend to capture the investment and loan data from Yahoo Finance websites as a data source, basically every dimension and every format of data is available to facilitate the later operation. Yahoo has gone to a Reactjs front end which means if you analyze the request headers from the client to the backend you can get the actual JSON they use to populate the client side stores.
Formatting data: Here I will divide the acquired data into xls, csv, sql, and pandas DataFrame format data, and operate them separately to cope with various data source formats
Cleaning and organizing data: excel, sql, python, javascript will be used
Statistical Analysing data: mainly using pandas and sql in python.
Visualize data: I will use django web development for visualisation (html, css, javascript)
```

**Sami** : Responsible for the Market Capatalization Diagram, Spiderweb graph.

## Clone repo
```shell
git clone "https://github.com/YongjiangChen/miniPoroject.git"
```
## Installation
In the cloned folder, open a terminal where requirements.txt is

```shell
pip install -r requirements.txt
```

## Running
Enter the manage.py directory in the terminal, and run server

```shell
python manage.py runserver
```
Ctrl-Click on the local server link poped in the terminal to open the web page

## Repo update
```shell
git pull
```

## Commit to the project
Upload file on github webpage or using git:
```shell
git add <file to be updated>
```

```shell
git commit -m "commit message"
```

```shell
git push origin main
```
