class Manager:

	def __init__(self,passcode_identity , password):
		self.identity = passcode_identity
		self.password = password
	
	@property
	def show(self):
		return f'Identity - {self.identity} \n password - {self.password}'
		
	def __repr__(self):
		return f'{self.identity} - {self.password}'
		
	
		
