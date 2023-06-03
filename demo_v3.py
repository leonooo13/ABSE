from charm.toolbox.pairinggroup import PairingGroup, ss512
from charm.toolbox.secretutil import SecretUtil
from charm.toolbox.ABEnc import CPabe09


# 初始化PairingGroup
group = PairingGroup(ss512)

# 生成主密钥和公钥
cpabe = CPabe09(group)
master_key, public_key = cpabe.setup()

# 定义属性和策略
attributes = ['student', 'math', 'good_score']
policy = '((math and good_score) or (student and good_score))'

# 生成秘钥
secret_key = cpabe.keygen(public_key, master_key, attributes)

# 明文加密
plaintext = b'This is a secret message.'
ciphertext = cpabe.encrypt(public_key, plaintext, policy)

# 密文解密
decrypt_text = cpabe.decrypt(public_key, secret_key, ciphertext)

# 输出结果
print('Plaintext:', plaintext)
print('Decrypt text:', decrypt_text)
