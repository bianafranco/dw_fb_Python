import json, urllib
from pprint import pprint
from criando_banco import dao

d = dao()
## pegar token no site do https://developers.facebook.com/tools/explorer/145634995501895/?method=GET&path=me&version=v2.3
token = ''

ids_pages = ['320033178143669','656041921137604','1447067488906490','1431849273799074','233680560160631','241341586064569','803005986480403','253946268141958','1464043183838725','1623122437904948','706728776102230']

print 'Iniciando...'

for page in ids_pages:
    url_post = 'https://graph.facebook.com/' + page + '/posts?access_token=' + token

    resposta_post = urllib.urlopen(url_post).read()

    dados_post = json.loads(resposta_post)

    if 'error' not in dados_post.keys():

        if len(dados_post['data']) > 0:
            nomePage = dados_post['data'][0]['from']['name']
            
            print 'Page = ' + nomePage
            for dado in dados_post['data']:        
                idPost = dado['id']
                if 'message' in dado.keys():
                    if d.postExiste(idPost) == False:
                        texto = dado['message']
                        criado_em = dado['created_time'][0:10]
                        print 'Post Novo: ' + idPost
                        d.inserirPost(idPost,texto,criado_em)
                if 'likes' in dado.keys():
                    likes = dado['likes']['data']
                    for like in likes:
                        usuarioId = like['id']
                        usuarioNome =  like['name']
                        if d.usuarioExiste(usuarioId) == False:
                            d.inserirUsuario(usuarioId, usuarioNome)
                            print 'Usuario Novo: ' + usuarioId
                            if d.curtidasPostExiste(dado['id'], usuarioId) == False:
                                d.inserirCurtidasPost(dado['id'], usuarioId)
                                print 'Curtida Novo'
                if 'comments' in dado.keys():
                    comments = dado['comments']['data']
                    for comment in comments:
                        usuarioId = comment['from']['id']
                        usuarioNome =  comment['from']['name']
                        idComentario = comment['id']
                        texto = comment['message']
                        criado_em = comment['created_time'][0:10]
                        if d.usuarioExiste(usuarioId) == False:
                            d.inserirUsuario(usuarioId, usuarioNome)
                            print 'Usuario Comentario Novo: ' + usuarioId
                        if d.comentarioExiste(idComentario) == False:
                            d.inserirComentario(idComentario, usuarioId, texto, criado_em)
                            print 'Comentario Novo: ' + idComentario
                        if d.postComentarioExiste(idPost, idComentario) == False:
                            d.inserirPostComentario(idPost, idComentario)
                            print 'post Comentario Novo: ' + idPost
    else:        
        print 'code: ' + str(dados_post['error']['code']) + '\nMessage: ' + dados_post['error']['message'] + '\nType: ' + dados_post['error']['type']
        
        break
print 'Terminado.'
