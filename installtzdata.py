import sys, os, string
import paramiko

update = "yum update -y tzdata"
check = "zdump -v /usr/share/zoneinfo/America/Sao_Paulo | grep 2018"
servers = ['192.168.1.1','192.168.1.2','187.52.5.3']


for server in servers:
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server, username='root', password='password')
        stdin, stdout, stderr = ssh.exec_command(update)
        stdin.write('xy\n')
        stdin.flush()
        stdin.close()
        print stdout.readlines()
        print "Instalado no servidor " + server
        stdin, stdout, stderr = ssh.exec_command(check)
        stdin.write('xy\n')
        stdin.flush()
        stdin.close()
        print "Verifique se foi atualizado para 4 de novembro"
        print stdout.readlines()

    except:
        print "Erro no servidor" + server
        pass
