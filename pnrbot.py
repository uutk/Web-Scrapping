def pnrStatus(last_chat_id,last_update_id):
	url="https://www.railyatri.in/pnr-status/"
	current_update_id=last_update_id
	greet_bot.send_message(last_chat_id,"Enter PNR Number")
	while last_update_id==current_update_id:
		current_update= greet_bot.get_last_update()
		current_update_id = current_update['update_id']
	greet_bot.send_message(last_chat_id,"Fetching Status....")	
	pnr=current_update['message']['text']
	if len(pnr)!=10:
		greet_bot.send_message(last_chat_id,"Enter a valid PNR Number:")
	else	
		url=url+pnr
		r=requests.get(url)
		train_booking='Booking Status:'
		train_name='Train Name:'
		train_from='From:'
		train_to='To:'
		train_date='Journey Date:'
		train_class='Class:'
		train_status='Current Status:'
		soup = BeautifulSoup(r.content, 'html5lib')
		table=soup.find('div', attrs = {'class':'pnr-search-result-info'})
		t=1					
		flag=0
		for row in table.findAll('p',attrs={'class':'pnr-bold-txt'}):
			name=row.text
			if t==1:
				flag=1
				train_name=train_name+name
			elif t==2:
				train_from=train_from+name
			elif t==3:
				train_to=train_to+name
			elif t==4:
				train_date=train_date+name
			elif t==5:
				train_class=train_class+name
			t=t+1
		t=1	
		temp=0
		table=soup.find('div', attrs = {'id':'status'})	
		for row in table.findAll('p',attrs={'class':'pnr-bold-txt'}):
			if t==2:
				temp=1
				train_status=train_status+row.text
			elif t==1:
				train_booking=train_status+row.text	
			t=t+1	
		if flag!=0 and temp!=0:	
			pnr_info=train_booking+'\n'+train_status+'\n'+train_name+'\n'+train_from+'\n'+train_to+'\n'+train_date+'\n'+train_class
			greet_bot.send_message(last_chat_id,pnr_info)
		else:
			greet_bot.send_message(last_chat_id,"Verify your PNR number!")