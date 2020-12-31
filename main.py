import sqlite3
from manager import Manager

conn = sqlite3.connect('password_manager.db')

c = conn.cursor()

#c.execute('''CREATE TABLE passcode_manager(
#			 identity text primary key,
#			 passcode text)''')
			 
#conn.commit()


def create_passcode(identity , password):
	passcode = Manager(identity , password)
	c.execute('INSERT INTO passcode_manager VALUES (? , ?)',(passcode.identity , passcode.password))
	conn.commit()
	
def check_exist(identity):
	c.execute('SELECT * FROM passcode_manager WHERE identity=?',(identity,))
	if(c.fetchone()):
		return True
	else:
		return False


print('\t\tWELCOME TO RAMAN PASSCODE MANAGER\n')
password = input('Enter the passcode to see and add passcode    - ')
while( password != 'raman'):
	password = input('\nWrong passcode enter again to see and add passcode - ')
	
#user has already enter the write passcode
print()
print('press 1 to see all passcodes \npress 2 to add new passcode \npress 3 to search \npress 4 to delete a passcode \npress 5 to update a passcode \npress 0 to exit \n')
opt = int(input())

while(opt != 0):
	if(opt == 1):
		c.execute('SELECT * FROM passcode_manager')
		print()
		print('Passcodes are -')
		print()
		for passcode in c.fetchall():
			print(f'\t\tIdentity - {passcode[0]}')
			print(f'\t\tpassword - {passcode[1]}')
			print()
	elif (opt == 3):
		print()
		iden = input('Enter identity - ')
		c.execute('SELECT * FROM passcode_manager WHERE identity = ?',(iden,))
		result = c.fetchone()
		print()
		if(result):
			print(f'\t\tidentity -  {result[0]}')
			print(f'\t\tpassword - {result[1]}')
		else:
			print(f'No passcode found for identity {iden} please try with another identity.\n')
	
	elif (opt == 4):
		print()
		iden = input('Enter Identity - ')
		if not(check_exist(iden)):
			print(f'\nNo passcode found for identity {iden} please try again.\n')
		else:
			c.execute('DELETE FROM passcode_manager WHERE identity=?',(iden,))
			conn.commit()
			print(f'\nSuccessfully deleted passcode of identity - {iden}\n')
	
	elif (opt == 5):
		print()
		iden = input('Enter Identity - ')
		if(check_exist(iden)):
			
			new_identity = input('Enter New Identity - ')
			new_password = input('Enter New password - ')
			c.execute('UPDATE passcode_manager SET identity=? , passcode=? WHERE identity=?',(new_identity,new_password,iden))
			conn.commit()
			print(f'\nSuccessfully updated passcode of old identity - {iden}\n')
		else:
			print(f'\nNO passcode found for identity {iden}\n')
			
	else:
		print('Enter Information below to set new passcode.')
		identity = input('Identity -  ')
		password = input('password -  ')
		c.execute('SELECT * FROM passcode_manager WHERE identity=?',(identity,))
		check = c.fetchall()
		if len(check) == 0:
			create_passcode(identity , password)
		else:
			print('Identity already exists please try with different identity')
		print('\n')
		
	opt = int(input('press 1 to see all passcodes \npress 2 to add new passcode \npress 3 to search \npress 4 to delete a passcode \npress 5 to update a passcode \npress 0 to exit \n'))
	
print('exited')
conn.close()
	

		
	
	

