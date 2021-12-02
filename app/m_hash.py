import hashlib
import hmac

def MD4(texto): #están bien
    hashObject = hashlib.new('md4', texto.encode('utf-8'))
    digest = hashObject.hexdigest()
    return(digest)

def MD5(texto): #están bien
    hashObject = hashlib.new('md5', texto.encode('utf-8'))
    digest = hashObject.hexdigest()
    return(digest)

def SHA1(texto): #están bien
    hashObject = hashlib.new('sha1', texto.encode('utf-8'))
    digest = hashObject.hexdigest()
    return(digest)

def SHA256(texto): #están bien
    hashObject = hashlib.new('sha256', texto.encode('utf-8'))
    digest = hashObject.hexdigest()
    return(digest)

def HMAC(texto, clave): #falta analizar
    hmac2 = hmac.new(key=clave.encode(), digestmod=hashlib.sha256)
    hmac2.update(bytes(texto, encoding="utf-8"))
    message_digest2 = hmac2.hexdigest()

    return(message_digest2)
