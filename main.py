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



password = input('Enter the MASTER password to get access  :  ')
while( password != 'raman'):
	password = input('\nWrong MASTER password enter again to get access : ')

#user has enter successfully to the app
print('WELCOME TO RAMAN PASSCODE MANAGER')
print('_________________________________\n')
print('---------Menu---------')
print('1. See all passcodes \n2. Add new passcode \n3. To search a passcode \n4. Delete a passcode \n5. Update a passcode \n0. Exit or Quit')
print('__________________________________________')
opt = int(input('\n   :  '))

while(opt != 0):
	if(opt == 1):
		c.execute('SELECT * FROM passcode_manager')
		print('\nPasscodes are :\n')
		for passcode in c.fetchall():
			print('\t*****************************')
			print(f'\t Identity - {passcode[0]}')
			print(f'\t password - {passcode[1]}')
			print('\t*****************************\n')
	elif (opt == 3):
		iden = input('\nEnter identity - ')
		c.execute('SELECT * FROM passcode_manager WHERE identity = ?',(iden,))
		result = c.fetchone()
		print()
		if(result):
			print('\t*****************************')
			print(f'\t Identity - {result[0]}')
			print(f'\t password - {result[1]}')
			print('\t*****************************\n')
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
		print('Enter Information below to set new passcode : \n')
		identity = input('Identity :  ')
		password = input('password :  ')
		c.execute('SELECT * FROM passcode_manager WHERE identity=?',(identity,))
		check = c.fetchall()
		if len(check) == 0:
			create_passcode(identity , password)
			print(f'Successfully Added passcode with Identity - {identity}')
		else:
			print('Identity already exists please try with different identity')
		print('\n')
		
	print('-------------------Menu-----------------------------------')
	print('1. See all passcodes \n2. Add new passcode \n3. To search a passcode \n4. Delete a passcode \n5. Update a passcode \n0. Exit or Quit \n')
	print('__________________________________________')
	opt = int(input('\n   :  '))
	
print('See you Again! ')
conn.close()
	

		
	
	

