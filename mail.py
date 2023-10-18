import random
import smtplib

otp = ''.join([str(random.randint(0,9))for i in range(6)])


server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('nikhilbaghele11@gmail.com','wivoawqvmcgbophp')
msg='your otp is '+str(otp)
server.sendmail('nikhilbaghele11@gmail.com','ommhatre2003@gmail.com',msg)
server.quit()