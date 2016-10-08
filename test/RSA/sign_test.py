from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
from base64 import b64encode
from base64 import b64decode
import json


def rsa_sign(message):
    private_key_file = open('id_rsa', 'r')
    private_key = RSA.importKey(private_key_file)
    e_mesg = b64encode(json.dumps(message))
    hash_obj = SHA.new(e_mesg)
    signer = PKCS1_v1_5.new(private_key)
    e_sign = b64encode(signer.sign(hash_obj))
    return e_sign, e_mesg


def rsa_verify(e_sign,e_mesg):
    public_key_file = open('id_rsa.pub', 'r')
    public_key = RSA.importKey(public_key_file)
    sign = b64decode(e_sign)
    h = SHA.new(e_mesg)
    verifier = PKCS1_v1_5.new(public_key)
    if verifier.verify(h, sign):
        message = b64decode(e_mesg)
        return message


if '__main__' == __name__:
    e_sign, e_mesg = rsa_sign('zhangshibo')
    print e_sign,e_mesg
    message = rsa_verify(e_sign,e_mesg)
    print message
