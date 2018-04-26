from constraint import *
from collections import deque
import Preferences 
"""Demo of constraint program to generate schedule that aligns with preferences"""

#get Preference instance from main 
p = Preferences.main()

problem = Problem()

days = ['m','t','w','r','f']
#these are hard-coded for now
min_courses = int(p.min_courses)
max_courses = int(p.max_courses)
max_days = ['m','w','r']            # [1,1,1,1,1] # all days checked
min_days = ['m','t','w']  # what the user wants

# These are the times the user requested
hour_time_to = p.time_to[0]
hour_time_from = p.time_from[0]
minute_time_to = p.time_to[1]
minute_time_from = p.time_from[1]


max_time = int((str(hour_time_to).strip() + str(minute_time_to).strip()).strip()) #11 pm
min_time = int((str(hour_time_from).strip() + str(minute_time_from).strip()).strip())  #8 am

print(max_time)
print(min_time)
#sg = problem.getSolutions()
#
times = list(range(80,2400))
num_courses = list(range(min_courses,max_courses+1))

categories = p.cat
locations = p.loc
subjects = p.subjects
professors = p.prof



problem.addVariable("day", days)
problem.addVariable("time", times)
problem.addVariable("num_course",num_courses)
problem.addVariable("location",locations)
problem.addVariable("professor",professors)
problem.addVariable("category",categories)
problem.addVariable("subject",subjects)



problem.addConstraint(lambda day,time,num_course,professor,subject,location:
                      day in max_days
                      and time <= max_time
                      and any(x in day for x in min_days)
                      and time >= min_time
                      and num_course <= max_courses
                      and num_course >= min_courses
                      and professor in professors
                      and subject in subjects
                      and location in locations
                      ,
                          ("day", "time","num_course","professor","subject","location"))
 

""" DESIGN CHOICES """
# Eagerly obtain all possible schedule possibilities --rejected in favor of lazily generating
# sg = problem.getSolutions()


# Lazy generation of solutions: file should be called multiple times, when user needs to obtain another schedule
sg = problem.getSolutionIter()


# store in deque
global schedule_deque = deque()
#append one by one
deque.append(sg)


#alternative: appending to variable sized array (Python "list")
#schedule_list = []
#schedule_list.append(sg) -- rejected due to inefficiency when compared to the deque (which has constant time append)



"""END DESIGN CHOICES"""








def main():
   print(next(sg))


    
if __name__ == "__main__": main()










