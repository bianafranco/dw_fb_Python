CREATE TABLE post_comentario (
            idPost INTEGER NOT NULL,
            idComentario INTEGER NOT NULL
            );

        CREATE TABLE comentario (
            idComentario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            idUsuario INTEGER NOT NULL,
            texto TEXT NOT NULL,
            criado_em DATE NOT NULL
            );

        CREATE TABLE usuario (
            idUsuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
            );

        CREATE TABLE curtidasPost (
            idPost INTEGER NOT NULL,
            idUsuario INTEGER NOT NULL
            );

        CREATE TABLE sentimento (
            idSentimento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL
            );