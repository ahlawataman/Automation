import requests

url = 'https://clashofcodes.herokuapp.com/user/signin'
myobj = '{"email":"ahlawataman3@gmail.com","password":"----"}'
head = {'_ga_Q0L0V6P641':'GS1.1.1641448746.2.1.1641449499.0', '_ga':'GA1.1.984749176.1641392013', 'express:sess':'eyJwYXNzcG9ydCI6e319', 'express:sess.sig':'5rsqTabounLZ_yYBTYpBYv2moWk'}

x = requests.post(url, data = myobj, cookies=head)

print(x.status_code)
