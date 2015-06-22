import urllib, json
from pprint import pprint

token = 'CAAG9SwJw5O4BAAxh20YiMgARnPQwiqrtcqW7PQU0MyzfXZBD1Pghv8XbO9vMONuXGnxd7EOybB5VsSq50p6pAUkSwSP9zuskOqoSFEZAvPGLiOrb6zXftXnR4hBtWBSdCJLiPBCs8d3tIAZBswqtAkyXUKonhzmfAVFA3sHmaQKwG2EKMtgPyJM3dZCKYx2NC8YtZChitFuc6vkZBpiO3E'

textos = ['OcupeEstelita','ResisteEstelita','DesocupeEstelita', 'DesisteEstelita','CaisJoseEstelita']

for texto in textos:
    url_page = 'https://graph.facebook.com/search?q=' + texto + '&type=page&access_token=' + token

    resp_page = urllib.urlopen(url_page).read()

    dados_page = json.loads(resp_page)['data']

    for page in dados_page:
        pprint(page)
