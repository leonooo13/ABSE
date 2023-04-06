# 如何设计一个基于属性的可搜索加密方案
1. 属性加密
2. 可搜索加密
Q:如何存储用户属性
Q:属性和加密如何结合
Q:我使用属性作为密钥将用户的信息加密后，存储到云端，是这样吗？
Q:hash函数如何与加密后的消息进行结合
## 属性加密
1. 将属性转成字符串，进行hash值生成attr_key
2. 使用`cipher=AES.new(attr_key, AES.MODE_CBC)`,`cipher = cipher.encrypt(pad(plaintext.encode(), AES.block_size))`进行加密，也可以返回iv初始向量
3. 解密与上面一样
# 安装Charm后
Q:如何使用abe
charm\schemes\abenc中有多种abe算法
abenc后面的nc,应该是encryption的前三个字母
[在该连接中提供了多种样例](https://jhuisi.github.io/charm/schemes.html)
```
abenc_bsw07
abenc_dacmacs_yj14
abenc_lsw08
abenc_maabe_rw15
abenc_maabe_yj14
abenc_tbpre_lww14
abenc_unmcpabe_yahk14
abenc_waters09
abenc_yct14
```
其中选择第一中算法bsw07来介绍如何使用CPABE
## author
John Bethencourt, Brent Waters (Pairing-based)
From: “Ciphertext-Policy Attribute-Based Encryption”.
Published in: 2007
Available from:
Notes:
Security Assumption:
type: ciphertext-policy attribute-based encryption (public key)
setting: Pairing
# 算法流程
1. 生成群
2. 生成cpabe对象
3. 定义属性
4. 设置访问树
5. setup->pk,mk
6. 生成私钥 keygen(pk,mk,属性)
6. e(mk,msg,访问树)
7. d(mk,sk,cipher)
