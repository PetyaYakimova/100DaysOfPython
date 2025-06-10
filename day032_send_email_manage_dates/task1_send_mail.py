import smtplib

my_email = "fake_mail@gmail.com"
password = "fakepass"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="receiver_mail@gmail.com",
                        msg="Subject:Hello\n\nThis is the contents of my email")
