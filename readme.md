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


