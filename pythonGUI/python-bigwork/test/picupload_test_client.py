import paramiko

username = 'Administrator'  # 用户名为administrator
password = 'Qqhh11191911'  # 密码为远程链接时所需要的密码（云服务器实例密码）

transport = paramiko.Transport("124.222.113.8", 22)  # 获取Transport实例，其中22为端口号
transport.banner_timeout = 300 # 设置连接超时时间
transport.connect(username=username, password=password)  # 建立连接
print("ok")
# 获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(transport)
# 设置上传的本地/远程文件路径
localpath = "D:\\20212022s\\计应赛\\a copy.png"
remotepath = "C:\\python-bigwork\\a copy.png"

# 执行上传动作
sftp.put(localpath, remotepath)
transport.close()

print(transport)