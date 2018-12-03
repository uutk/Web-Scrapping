import requests
import tables
from bs4 import BeautifulSoup
import csv
import datetime
def wordMeaning(last_chat_id,last_update_id):
	i=1
	errorMsg='Meaning for the Word was not found.'+'\n'+'This may be due to one of the following reasons:'+'\n'+'  1)Misspelled Word'+'\n'+'  2)Compund Word'+'\n'+'Retry with a valid word!'
	url='http://www.dictionary.com/browse/'
	current_update_id=last_update_id
	greet_bot.send_message(last_chat_id,"Enter Word to be searched")
	while last_update_id==current_update_id:
		current_update= greet_bot.get_last_update()
		current_update_id = current_update['update_id']	
	word=current_update['message']['text']
	meaning='Meaning of '+word+':'+'\n'
	url=url+word+'?s=t'
	r=requests.get(url)
	soup = BeautifulSoup(r.content, 'html5lib')
	table=soup.find('ol', attrs = {'class':'css-zw8qdz e10vl5dg3'})
	if not table:
		greet_bot.send_message(last_chat_id,errorMsg)
	else:
		for row in table.findAll('span',attrs={'class':'css-4x41l7 e10vl5dg6'}):
			meaning=meaning+str(i)+'.'+row.text+'\n'
			i=i+1
		print(meaning)
		greet_bot.send_message(last_chat_id,meaning)	
class BotHandler:
    def __init__(self, token):
        self.token = '604449506:AAGdN1Sco2yj5hW7DM3dEmmP5IJKHP_y_lQ'
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json
    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp
    def get_last_update(self):
        get_result = self.get_updates()
        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]
        return last_update
greet_bot = BotHandler('604449506:AAGdN1Sco2yj5hW7DM3dEmmP5IJKHP_y_lQ')  
greetings = ('hello', 'hi', 'greetings', 'sup','hey','hai','hey there','dai','el','vanakam','dae','dude')
now = datetime.datetime.now()  
def main():  
	new_offset = None
	today = now.day
	hour = now.hour
	while True:
		greet_bot.get_updates(new_offset)
		last_update = greet_bot.get_last_update()
		last_update_id = last_update['update_id']
		last_chat_text = last_update['message']['text']
		last_chat_id = last_update['message']['chat']['id']
		last_chat_name = last_update['message']['chat']['first_name']
		if last_chat_text.lower() in greetings :
			if today == now.day and 6 <= hour < 12:
				greet_bot.send_message(last_chat_id, 'Good Morning  {}'.format(last_chat_name))
			elif today == now.day and 12 <= hour < 17:
				greet_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
			elif today == now.day and 17 <= hour < 23:
				greet_bot.send_message(last_chat_id, 'Good Evening  {}'.format(last_chat_name))
			today += 1
		elif last_chat_text.lower()=='bye' or last_chat_text.lower()=='tata' or last_chat_text.lower()=='cys' or last_chat_text.lower()=='see you soon':
			user_name='Bye! Have a Nice Day '+last_chat_name+'!'
			greet_bot.send_message(last_chat_id,user_name)  	
		elif last_chat_text.lower() =='score' or last_chat_text.lower() =='scores' or last_chat_text.lower() =='cricket':
			greet_bot.send_message(last_chat_id, 'Live Score Loading!')
			cricscore(last_chat_id)	
		elif last_chat_text.lower() == 'google' or last_chat_text.lower() == 'search':
			googleSearch(last_chat_id,last_update_id)
		elif last_chat_text.lower() == 'pnr':
			pnrStatus(last_chat_id,last_update_id)
		elif last_chat_text.lower() == 'meaning':
			wordMeaning(last_chat_id,last_update_id)			
		new_offset=last_update_id + 1
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()