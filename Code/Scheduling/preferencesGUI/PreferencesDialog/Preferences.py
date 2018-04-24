from pprint import pprint



class Preferences(object):
    def __init__ (self,loc,cat,prof,days,time_to,time_from,time_interval,subjects,num_courses):
        
        self.loc = loc
        self.cat = cat
        self.prof = prof
        self.days = days
        self.time_to = time_to
        self.time_from = time_from
        self.time_interval = time_interval
        self.subjects = subjects
        self.num_courses = num_courses
        self.min_courses = self.num_courses[0]
        self.max_courses = self.num_courses[1]
        


<<<<<<< HEAD
=======

>>>>>>> c0c06d8965c00e4b02b96807836139f09a23e4bb
     


def main():
<<<<<<< HEAD
        in_file = open('C:\\Users\\htaleshi\\Downloads\\AdviseMe-master\\AdviseMe-master\\preferencesGUI\\PreferencesDialog\\workfile')
=======
        in_file = open('/Users/howard/PreferencesDialog/workfile')
>>>>>>> c0c06d8965c00e4b02b96807836139f09a23e4bb
        preference_string = in_file.read()

 #       self.preference_string = self.preference_string.strip('(')
#        self.preference_string = self.preference_string.strip(')')
        preference_string = preference_string.split(sep=';')

        preference_string = list(filter(None, preference_string)) # get rid of spaces

        emp = []
        for x in preference_string:
            y = x.split(sep=',')
            z = list(filter(None,y))
            emp.append(z)

        for x in emp:
            for d in x:
                if d.isdigit():
                    d = int(d)
                    
        
        p = Preferences(emp[0],emp[1],emp[2],emp[3],emp[4],emp[5],emp[6],emp[7],emp[8])
        pprint(vars(p))
        return p


if __name__ == "__main__":
    main()
<<<<<<< HEAD
=======

>>>>>>> c0c06d8965c00e4b02b96807836139f09a23e4bb
