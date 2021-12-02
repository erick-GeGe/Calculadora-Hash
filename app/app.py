from flask import Flask, render_template, request
import m_hash
import json


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/MD4', methods=["POST"])
def MD4_result():
   
    tex_claro = request.form["data"]
    clave_md4 = m_hash.MD4(tex_claro)
    return clave_md4
        

@app.route('/MD5', methods = ["POST"])
def MD5_result():
    tex_claro = request.form["data"]
    clave_md5 = m_hash.MD5(tex_claro)
    return clave_md5
    

@app.route('/SHA1', methods = ["POST"])
def Sha1_result():
    tex_claro = request.form["data"]
    hash_sha1 = m_hash.SHA1(tex_claro)
    return hash_sha1
    

@app.route('/SHA256', methods = ["POST"])
def Sha256_result():
    tex_claro = request.form["data"]
    hash_sha256 = m_hash.SHA256(tex_claro)
    return hash_sha256
    

@app.route('/HMAC', methods = ["POST"])
def Hmac_result():
    tex_claro = request.form["data"]
    clave = request.form["clave"]
    hash_hmac = m_hash.HMAC(tex_claro, clave)
    return hash_hmac

if __name__ == '__main__':
    app.run(debug=True)
