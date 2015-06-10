SELECT COUNT(u.idUsuario)
FROM usuario u
WHERE 1=1
AND NOT EXISTS(SELECT 1 FROM comentario c WHERE c.idUsuario = u.idUsuario)
AND NOT EXISTS(SELECT 1 FROM curtidasPost cp WHERE cp.idUsuario = u.idUsuario)