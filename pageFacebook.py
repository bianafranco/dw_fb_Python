import urllib, json
from pprint import pprint

token = 'CAACEdEose0cBADpiLWHa3cPzYSpZCfC5uDler6tDN12gvXAvo5M4NGgMNyvzpvTItyTLeX9ZAZAFN4qcmvmFNmIAUO8DlBhZCQXajUOSFKgvwDoouxREHRfI7BZBIgN9SzZCE697uKTWHkas578gkg05vWoXhvkZAaMbMyxs0nGT5rPj0JWvImYVXAwXnhEff6UHDDu1bd4e9gCZAjxFtwl50xqZCZBrtIDQAZD'

textos = ['OcupeEstelita','ResisteEstelita','DesocupeEstelita', 'DesisteEstelita','CaisJoseEstelita']

for texto in textos:
    url_page = 'https://graph.facebook.com/search?q=' + texto + '&type=page&access_token=' + token

    resp_page = urllib.urlopen(url_page).read()

    dados_page = json.loads(resp_page)['data']

    for page in dados_page:
        pprint(page)
