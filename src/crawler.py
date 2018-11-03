import requests, bs4, hashlib, time, sys, smtplib
from email.mime.text import MIMEText
from tqdm import trange

#ovu funkciju zamenite nekim drugim nacinom obavestavanja.
#za desktop notifikacije pogledajte biblioteku libnotify
def send_email(to, text, url):
    msg = MIMEText(text)
    msg['subject'] = f'Promena na sajtu {url}'
    msg['to'] = to
    msg['from'] = 'mr15334'
    
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

def send_request(url):
    req = requests.get(url)
    hash = hashlib.md5()
    hash.update(req.text.encode('utf-8'))
    return(hash.hexdigest(), req)

def pause():
	step = time_to_sleep/100
	for i in trange(int(100)):
		time.sleep(step)

url = input("Unesite url: ")
mail = input("Unesite mail adresu: ")
time_to_sleep = int(120) #vreme spavanja u sekundama
old_hash = send_request(url)[0]
new_hash = old_hash

while old_hash == new_hash :
	pause()
	(new_hash, new_req) = send_request(url)

new_req.encoding = "utf-8"
html = new_req.text
soup = bs4.BeautifulSoup(html, "html.parser")
text = soup.find(id='text')
send_email(to = mail, text = text, url = url)
print("Poslata poruka")


