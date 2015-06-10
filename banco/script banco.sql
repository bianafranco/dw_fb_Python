BEGIN TRANSACTION;
CREATE TABLE usuario (
                idUsuario TEXT NOT NULL PRIMARY KEY,
                nome TEXT NOT NULL
                );
CREATE TABLE sentimento (
                idSentimento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL
                );
CREATE TABLE post_comentario (
                idPost TEXT NOT NULL,
                idComentario TEXT NOT NULL,
                FOREIGN KEY(idPost) REFERENCES post(idPost),
                FOREIGN KEY(idComentario) REFERENCES comentario(idComentario)
                );
CREATE TABLE post (
                idPost TEXT NOT NULL PRIMARY KEY,
                texto VARCHAR(500) NOT NULL,
                criado_em DATE NOT NULL,
                idSentimento INTEGER NOT NULL
                );
CREATE TABLE curtidasPost (
                idPost TEXT NOT NULL,
                idUsuario TEXT NOT NULL,            
                FOREIGN KEY(idPost) REFERENCES post(idPost),
                FOREIGN KEY(idUsuario) REFERENCES usuario(idUsuario)
                );
CREATE TABLE comentario (
                idComentario TEXT NOT NULL PRIMARY KEY,
                idUsuario TEXT NOT NULL,
                texto VARCHAR(500) NOT NULL,
                criado_em DATE NOT NULL,
                idSentimento INTEGER NOT NULL,
                FOREIGN KEY(idUsuario) REFERENCES usuario(idUsuario)
                );
COMMIT;
