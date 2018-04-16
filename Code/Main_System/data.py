class University():
	def __init__(self, name = "Example Uni", course_list = ['Ex101', 'Ex102', 'Ex201', 'Ex230'], major_list = ['Examples'], transfer={"Uni":{"Ex102":"Ex101"}}):
		self.name = name
		self.course_list = course_list
		self.major_list = major_list
		self.transfer = transfer

	def find_transfer_credit(self, uni):
		if not uni.name in self.transfer:
			return None
		return self.transfer[uni.name]

class major():
	def __init__(self, name = "Examples", requirements = ['Ex101', 'Ex102', 'Ex201', 'Ex230']):
		self.name = name
		self.requirements = requirements

class Student():
	def __init__(self, university = "Uni", courses_taken = [], major = "Examples", username = "abc", password = '123'):
		self.university = university
		self.courses_taken = courses_taken
		self.major = major
		self.username = username
		self.password = password

def find_transfer(student, uni_1, uni_2):
	ret = []
	val = []
	transfer = uni_2.find_transfer_credit(uni_1)
	if transfer == None:
		return False
	for itm in transfer:
		if transfer[itm] in student.major.requirements and not transfer[itm] in student.courses_taken:
			ret.append(itm)
			val.append(transfer[itm])
	return ret

def ret_vals():
	Examples = major()
	compsci = major("Computer Science", ['CSC130','CSC230','CSC330'])
	bio = major("Biology", ['BIO101','BIO102','BIO103','BIO104','BIO105'])
	major_list = [Examples, compsci, bio]
	ex = University("Example University", ['Ex101','Ex102','Ex201','Ex230','Ex330','Ex350'], [Examples], {"UNCG":{"CSC130":"Ex101","CSC230":"Ex102"},"NCAT":{"Bio101":"Ex101","BIO102":"Ex102"}})
	UNCG = University("UNCG", ['CSC130','CSC230','CSC330','CSC490','BIO101','BIO102','BIO103','BIO104','BIO105'],[compsci,bio],{"Example University":{"Ex230":"CSC130","Ex330":"BIO105"},"NCAT":{"BIO105":"CSC130"}})
	NCAT = University("NCAT", ['BIO101','BIO102','BIO103','BIO104','BIO105'],[bio],{'Example University':{"Ex101":"BIO105"}})
	uni_list = [ex, UNCG, NCAT]
	course_markers = ['WI','SI','GSB','GLT']
	ret_list = [major_list, uni_list, course_markers]
	return ret_list
