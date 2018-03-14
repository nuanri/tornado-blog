import hashlib
import random
import string


def _hash(salt, raw_password):
    data = "{0}{1}".format(salt, raw_password)
    return hashlib.sha512(data.encode("UTF-8")).hexdigest()


def encrypt_password(plaintext):
    salt = random.sample(string.ascii_letters + string.digits, 32)
    h = _hash(salt, plaintext)
    return "%s$%s" % (salt, h)


def check_password(raw_password, enc_password):
    salt, h = enc_password.split('$')
    return h == _hash(salt, raw_password)
