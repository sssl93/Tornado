from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
from base64 import b64encode
from base64 import b64decode


def rsa_sign(message):
    private_key_file = open('./myPrivateKey.pem', 'r')
    private_key = RSA.importKey(private_key_file)
    hash_obj = SHA.new(message)
    signer = PKCS1_v1_5.new(private_key)
    d = b64encode(signer.sign(hash_obj))
    file = open('./signThing.txt', 'wb')
    file.write(d)
    file.close()


def rsa_verify(message):
    public_key_file = open('./myPublicKey.pem', 'r')
    public_key = RSA.importKey(public_key_file)
    sign_file = open('./signThing.txt', 'r')
    sign = b64decode(sign_file.read())
    h = SHA.new(message)
    verifier = PKCS1_v1_5.new(public_key)
    return verifier.verify(h, sign)


if '__main__' == __name__:
    rsa_sign('zhangshibo')
