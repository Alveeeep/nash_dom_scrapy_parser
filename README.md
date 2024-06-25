## Парсер сайта [наш.дом.рф](https://наш.дом.рф/сервисы/каталог-новостроек/список-объектов/список?place=0-1&objStatus=0) на фреймворке [Scrapy](https://scrapy.org) и библиотеке [Scrapy-Impersonate](https://github.com/jxlil/scrapy-impersonate)


## Использование

Установите необходимые зависимости:
```sh
pip install -r requirements.txt
```

Запустите парсер:
```sh
cd testnashdom/testnashdom
scrapy crawl parse -o result.json
```
