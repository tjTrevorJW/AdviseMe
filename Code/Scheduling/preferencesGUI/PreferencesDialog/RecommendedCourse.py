import pandas as pd





class Recommended_Course(object):
    def __init__(self,course,title,sh,course_type,instructor,meeting_dates,days,time,
                             location,categories,seats,limit,enroll,campus,subject):
    
        self.course = course
        self.title = title
        self.sh = sh
        self.instructor = instructor
        self.meeting_dates = meeting_dates
        self.time = time
        self.location = location
        self.categories = categories
        self.seats = seats
        self.limit = limit
        self.enroll = enroll
        self.campus = campus
        self.subject = subject



def main():
    filepath = 'C:\\Users\\htaleshi\\Downloads\\AdviseMe-master\\AdviseMe-master\\Code\\Suggested_Classes\\recommendedData.csv'
    #'C:\\Users\\\htaleshi\\Downloads\\tempFull.csv\\AdviseMe-master\\AdviseMe-master\\preferencesGUI\\PreferencesDialog'

    df = pd.read_csv(filepath)

    df = df.drop(columns=['CRN','**Notes','Prerequisites','Score','Unnamed: 0'])
    df.rename(columns={'*Campus': 'Campus','Course Type':'Course_Type','Meeting Dates':'Meeting_Dates'}, inplace=True)


    recommended_course_list = []

    for row in df.itertuples(index=True,name='Pandas'):
        r = Recommended_Course(getattr(row,'Course'),
        getattr(row,'Title'),
        getattr(row,'SH'),
        getattr(row,'Course_Type'),
        getattr(row,'Instructor'),
        getattr(row,'Meeting_Dates'),
        getattr(row,'Days'),
        getattr(row,'Time'),
        getattr(row,'Location'),
        getattr(row,'Categories'),
        getattr(row,'Seats'),
        getattr(row,'Limit'),
        getattr(row,'Enroll'),
        getattr(row,'Campus'),
        getattr(row,'Subject'))
        recommended_course_list.append(r)
    return recommended_course_list
    
    
if __name__ == '__main__': main()

    