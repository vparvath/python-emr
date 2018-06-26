import datetime
import os
import operator

print ("Current working directory is: ", os.getcwd())

from pathlib import Path
Path('children_directory.txt').touch()
Path('pediatrician_directory.txt').touch()
Path('children_visit_directory.txt').touch()
Path('children_appointment_directory.txt').touch()

children_directory={}
gender_directory={'M':'Male','F':'Female'}
pediatrician_directory ={}
children_visit_directory ={}
children_appointment_directory ={}


def cls(): print ("\n" * 5)

######################################################
#           write & retrieve filenames section
######################################################
            
def write_children_directory(children_directory, filename):
    with open(filename, 'w') as outfile:
        for name in children_directory.keys():            
            outfile.writelines(name + ';' + ';'.join([str(value) for value in children_directory[name]])+ '\n')

def retreive_children_directory(children_directory, filename):
    with open(filename, 'r') as infile:
        for rec in infile:
            items=rec.split(';')
            children_directory[items[0]] = [x for x in items[1:len(items)]]
            children_directory[items[0]][7]=(children_directory[items[0]][7][0:len(children_directory[items[0]][7])-1])

def write_pediatrician_directory(pediatrician_directory, filename):
    with open(filename, 'w') as outfile:
        for name in pediatrician_directory.keys():            
            outfile.writelines(name + ';' + ';'.join([str(value) for value in pediatrician_directory[name]]) + '\n')

def retreive_pediatrician_directory(pediatrician_directory, filename):
    with open(filename, 'r') as infile:
        for rec in infile:
            items=rec.split(';')
            pediatrician_directory[items[0]] = [x for x in items[1:len(items)]]
            pediatrician_directory[items[0]][2]=(pediatrician_directory[items[0]][2][0:len(pediatrician_directory[items[0]][2])-1])
            

def write_children_visit_directory(children_visit_directory, filename):
    with open(filename, 'w') as outfile:
        for name in children_visit_directory.keys():            
            outfile.writelines(name + ';' + ';'.join([str(value) for value in children_visit_directory[name]]) + '\n')

def retreive_children_visit_directory(children_visit_directory, filename):
    with open(filename, 'r') as infile:
        for rec in infile:
            items=rec.split(';')
            children_visit_directory[items[0]] = [x for x in items[1:len(items)]]
            children_visit_directory[items[0]][2]=(children_visit_directory[items[0]][2][0:len(children_visit_directory[items[0]][2])-1])


def write_children_appointment_directory(children_appointment_directory, filename):
    with open(filename, 'w') as outfile:
        for name in children_appointment_directory.keys():            
            outfile.writelines(name + ';' + ';'.join([str(value) for value in children_appointment_directory[name]]) + '\n')

def retreive_children_appointment_directory(children_appointment_directory, filename):
    with open(filename, 'r') as infile:
        for rec in infile:
            items=rec.split(';')
            children_appointment_directory[items[0]] = [x for x in items[1:len(items)]]
            children_appointment_directory[items[0]][2]=(children_appointment_directory[items[0]][2][0:len(children_appointment_directory[items[0]][2])-1])            

            
######################################################
#           validation section
######################################################

def validate_date(date_text):
    valid=1
    try:
        datetime.datetime.strptime(date_text, '%m-%d-%Y')
    except ValueError:

        print ("*** Invalid date format...must be in format of MM-DD-YYYY, Please try again")
        valid=0
    if (len(date_text) < 10):
        print ("*** Invalid date format...must be 10 characters long, Please try again")
        valid=0
    return valid

def validate_gender(gender_rec,gender):
     status=1
     if gender not in gender_rec:
        print ('Entered gender: ', gender, ' is invalid, Please try again')
        status=0
        
     return status

def validate_pediatrician(pediatrician_record,pediatrician):
     status=1
     if pediatrician not in pediatrician_record:
        status=0
     return status


def validate_time(time_text):
    valid=1
    try:
        datetime.datetime.strptime(time_text, '%H:%M')
    except ValueError:

        print ("*** Invalid Time format...must be in format of HH(0-23):MM(0-59), Please try again")
        valid=0
    return valid    

def validate_phone_number(phone_number):
    if len(phone_number) != 12:
        print ('Entered phone number: ', phone_number, ' is invalid, Please enter the phone number in the format XXX-XXX-XXXX')
        return False
    for i in range(12):
        if i in [3,7]:
            if phone_number[i] != '-':
                print ('Entered phone number: ', phone_number, ' is invalid, Please enter the phone number in the format XXX-XXX-XXXX')
                return False
        elif not phone_number[i].isalnum():
            print ('Entered phone number: ', phone_number, ' is invalid, Please enter the phone number in the format XXX-XXX-XXXX')
            return False
    return True


######################################################
#           Add Child/Pediatrician section
######################################################

def add_child(child_record, name):
  ''' Enter Child demographic info
      Dictionary key:  Child name
      Value:  1. BirthDate (age)
              2. Gender
              3. Address
              4. Pediatrician
  '''

  
 
  if name in child_record.keys():
        print ("Child\'s Name: ",name," is already in our Database !!!")
  else:
     valid=0
     while not valid:
        birthdate=input('Enter child\'s birthdate (MM-DD-YYYY): ')
        valid=validate_date(birthdate)

        if valid:
    
          D1=datetime.datetime(int(birthdate[6:]),int(birthdate[0:2]), int(birthdate[3:5]),0,0,0)
          D2=datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month,datetime.datetime.today().day)
          days=int((D2-D1).days)
          age = int(days / 365)
          print("Current age =", age) #print age

          if (days < 0):
             print ('Invalid birthdate...must be older than current date, please try again')
             valid=0

     valid=0
     while not valid:
        gender=input('Enter child gender (M/F): ')
        valid=validate_gender(gender_directory, gender)
        
     address=input('Enter child\'s Address: ')
     
     valid=0
     while not valid:
        pediatrician=input('Enter child Pediatrician: ')
        retreive_pediatrician_directory(pediatrician_directory,'pediatrician_directory.txt')
        valid=validate_pediatrician(pediatrician_directory,pediatrician)
        if not valid:
               add_or_ignore= input ('Entered Pediatrician is not in our database, would you like to add this pediatrician into our system?\
\nPress \'Y\' for Yes, \'N\' for No: ')
               if add_or_ignore.upper() == 'Y' :
                   add_pediatrician(pediatrician_directory, pediatrician )
                   valid=1
                   
               elif add_or_ignore.upper() == 'N' :
                   pediatrician='NOT_IN_SYSTEM'
                   valid=1

               elif add_or_ignore.upper() != ('Y' and 'N'):
                   print ('Incorrect option entered. Please choose from the available options from the Pediatric EMR menu.')
                   valid=0 

     valid=0
     while not valid:
        phone_number=input('Please enter Parent\'s phone number in the format XXX-XXX-XXXX: ')
        valid=validate_phone_number(phone_number)

     insurance=input('Enter child\'s Insurance Details: ')
     
     pharmacy=input('Enter child\'s Pharmacy Details: ')
   
        
     child_record[name] = [age,birthdate,gender,address,pediatrician, phone_number, insurance, pharmacy  ]

     write_children_directory(children_directory,'children_directory.txt')

     print ('New Child: \'',name, '\' added to the database successfully')   
  

def add_child_visit(child_record,child_visit_record,name):
  ''' Enter child visit  info
      Dictionary key:  Child\'s name
      Value:  1. Date visited
              2. see by - Pediatrician 
              3. Diagnostic
              
  '''
   
  if name not in child_record.keys():
     print ("Child\'s Name: ",name," must be in our Database first !!!")
  else:
     valid=0
     while not valid:
        visit_date=input('Enter child visit Date (MM-DD-YYYY): ')
        valid=validate_date(visit_date)

        if valid:
   
          D1=datetime.datetime(int(visit_date[6:]),int(visit_date[0:2]), int(visit_date[3:5]),0,0,0)
          D2=datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month,datetime.datetime.today().day)
          days=int((D2-D1).days)
          age = int(days / 365)
          if (days < 0):
            print ('Invalid child visit Date ...must be later than current date, please try again') #later instead of older
            valid=0
        
     valid=0
     while not valid:
        pediatrician=input('Enter child Pediatrician: ')
        retreive_pediatrician_directory(pediatrician_directory,'pediatrician_directory.txt')
        valid=validate_pediatrician(pediatrician_directory,pediatrician)
        if not valid:
               add_or_ignore= input ('Entered Pediatrician is not in our database, would you like to add this pediatrician into our system?\
\nPress \'Y\' for Yes, \'N\' for No: ')
               if add_or_ignore.upper() == 'Y' :
                   add_pediatrician(pediatrician_directory, pediatrician )
                   valid=1
                   
               elif add_or_ignore.upper() == 'N' :
                   pediatrician='NOT_IN_SYSTEM'
                   valid=1

               elif add_or_ignore.upper() != ('Y' and 'N'):
                   print ('Incorrect option entered. Please choose from the available options from the menu.')
                   valid=0 

        
     diagnostic=input('Enter Diagnostic: ')
	 
     visit_key=name + '*' + visit_date

     if visit_key in child_visit_record.keys():
       print ('Child :',name,'and visit-date: ',visit_date,' is already in the Database ...')
     else:   
       child_visit_record[visit_key] = [visit_date,pediatrician,diagnostic]

       write_children_visit_directory(children_visit_directory,'children_visit_directory.txt')

       print ('New Visit Info for: \'',name, '\' has been added to the database successfully')
       

def add_child_appointment(child_record,child_appointment_record,name):
 
  if name not in child_record.keys():
        print ("Child Name: ",name," must be in our patient Database first before you can add!!!")
  else:
        valid=0
        while not valid:
          app_date=input('Enter Date of Appointment(MM-DD-YYYY): ')
          valid=validate_date(app_date)
          if valid:
     
            D1=datetime.datetime(int(app_date[6:]),int(app_date[0:2]), int(app_date[3:5]),0,0,0)
            D2=datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month,datetime.datetime.today().day)
            days=int((D2-D1).days)
            age = int(days / 365)
            if (days > 0):
              print ('Invalid patient appointment Date ...must be in the future, please try again')
              valid=0
        
        valid=0
        while not valid:
          time_of_appointment=input('Enter patient Time of Appointment HH(0-23):MM(0-59): ')
          valid=validate_time(time_of_appointment)
          

        valid=0
        while not valid:
           pediatrician=input('Enter child Pediatrician: ')
           retreive_pediatrician_directory(pediatrician_directory,'pediatrician_directory.txt')
           valid=validate_pediatrician(pediatrician_directory,pediatrician)
           if not valid:
                  add_or_ignore= input ('Entered Pediatrician is not in our database, would you like to add this pediatrician into our system?\
\nPress \'Y\' for Yes, \'N\' for No: ')
                  if add_or_ignore.upper() == 'Y' :
                      add_pediatrician(pediatrician_directory, pediatrician )
                      valid=1
                      
                  elif add_or_ignore.upper() == 'N' :
                      pediatrician='NOT_IN_SYSTEM'
                      valid=1
   
                  elif add_or_ignore.upper() != ('Y' and 'N'):
                      print ('Incorrect option entered. Please choose from the available options from the menu.')
                      valid=0 
			   
			   
        app_rec=name + '*' + app_date
        child_appointment_record[app_rec] = [app_date, time_of_appointment, pediatrician]

        write_children_appointment_directory(children_appointment_directory,'children_appointment_directory.txt')

        print ('New Appointment for: \'',name, '\' has been added to the database successfully')
		


def add_pediatrician(pediatrician_record, name):
  ''' Enter Pediatrician info
      Dictionary key:  Pediatrician name
      Value:  1. Gender
              2. Speciality
              3. Phonenumber
  '''
  
 
  if name in pediatrician_record.keys():
        print ("Pediatrician\'s Name: ",name," is already in our Database !!!")
  else:

     valid=0
     while not valid:
        gender=input('Enter Pediatrician\'s gender (M/F): ')
        valid=validate_gender(gender_directory, gender)
        
     speciality=input('Enter Pediatrician\'s speciality: ')


     valid=0
     while not valid:
        phone_number=input('Please enter Pediatrician\'s phone number in the format XXX-XXX-XXXX: ')
        valid=validate_phone_number(phone_number)
        
     pediatrician_record[name] = [gender,speciality,phone_number]

     write_pediatrician_directory(pediatrician_directory,'pediatrician_directory.txt')

     print ('New Pediatrician: \'',name, '\' added to the database successfully')   
  

######################################################
#           View Child/Pediatrician section
######################################################

def view_child(child_record,Name):
  if Name in child_record.keys():
     cls()
     print ('**** Child information ****')
     print ('Name:',Name)
     print ('0. Age:',child_record[Name][0])
     print ('1. Birthdate:',child_record[Name][1])
     print ('2. Gender:',child_record[Name][2],'-', gender_directory[child_record[Name][2]])
     print ('3. Address:',child_record[Name][3])
     print ('4. Pediatrician:',child_record[Name][4])
     print ('5. Phone Number:',child_record[Name][5])
     print ('6. Insurance:',child_record[Name][6])
     print ('7. Pharmacy:',child_record[Name][7])
     
  else:
     cls() 
     print ('Child:',Name,' is not in our database, please try again')      



def view_child_visit(child_record,child_visit_record,name):
 
  if name not in child_record.keys():
        print ("Child\'s Name: ",name," must be in our Database first !!!")
  else:

    print ('Name'.ljust(15),'Visit-Date'.ljust(15),'Pediatrician'.ljust(12),'Diagnostic'.ljust(35))
    print (100*'-')
    
    for key in sorted(child_visit_record):        
        visit_key=key.split('*')
        if visit_key[0]== name:
           print (name.ljust(15), child_visit_record[key][0].ljust(15),child_visit_record[key][1].ljust(12),\
           child_visit_record[key][2].ljust(35))


def view_child_appointment (child_record,child_appointment_record,name):
 
  if name not in child_record.keys():
        print ("Child Name: ",name," must be in our Database first.")
  else:

        print ('Name'.ljust(15),'Appointment-Date'.ljust(25),'Appointment-Time'.ljust(20),'Pediatrician'.ljust(20))
        print (100*'-')
        for key in sorted(child_appointment_record):        
           visit_key=key.split('*')
           if visit_key[0]== name:
            print (name.ljust(15), child_appointment_record[key][0].ljust(25),child_appointment_record[key][1].ljust(20),\
            child_appointment_record[key][2].ljust(20))
       


def view_pediatrician(pediatrician_record,Name):
  if Name in pediatrician_record.keys():
     cls()
     print ('**** pediatrician information ****')
     print ('Name:',Name)
     print ('0. Gender:',pediatrician_record[Name][0],'-', gender_directory[pediatrician_record[Name][0]])
     print ('1. Speciality:',pediatrician_record[Name][1])
     print ('2. Phonenumber:',pediatrician_record[Name][2])
  else:
     cls() 
     print ('pediatrician:',Name,' is not in our database, please try again')


######################################################
#           Edit Child/Pediatrician section
######################################################

def edit_child(child_record,Name):
  if Name in child_record.keys():
     view_child(child_record,Name)
     edit_field=-1 

     while edit_field <0 or edit_field > 7:
       edit_field=int(input('Enter Field to be edit: '))

       if edit_field == 0:
            print ('You cannot edit age directly. In order to change the age, please selection option \'1\' to change the birthdate')
            edit_field=-1
        

       if edit_field == 1:
            valid=0
            while not valid:
              birthdate=input('Enter child birthdate (MM-DD-YYYY): ')
              valid=validate_date(birthdate)

              if valid:
  
                D1=datetime.datetime(int(birthdate[6:]),int(birthdate[0:2]), int(birthdate[3:5]),0,0,0)
                D2=datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month,datetime.datetime.today().day)
                days=int((D2-D1).days)
                age = int(days / 365)

                if (days < 0):
                   print ('Invalid birthdate...must be older than current date, please try again')
                   valid=0
          
            child_record[Name][0]=age
            child_record[Name][1]=birthdate        
            print ('Child: ', Name, '-> birthdate information updated to: ', birthdate)
        
  
       elif edit_field == 2:
            valid=0
            while not valid:
               gender=input('Enter child gender (M/F): ')
               valid=validate_gender(gender_directory, gender)

            child_record[Name][2]=gender
            print ('child: ', Name, '-> gender information updated to: ', gender)
        
       elif  edit_field == 3:
            address=input('Enter child Address: ') 
            child_record[Name][3]=address
            print ('Child: ', Name, '-> Address information updated to: ', address )
        
       elif  edit_field == 4:
            valid=0
            while not valid:

               pediatrician=input('Enter Pediatrician\'s name: ')
               retreive_pediatrician_directory(pediatrician_directory,'pediatrician_directory.txt')
               valid=validate_pediatrician(pediatrician_directory,pediatrician)
           
               if not valid:
                   add_or_ignore= input ('Entered Pediatrician is not in our database, would you like to add this pediatrician into our system?  \
\nPress \'Y\' for Yes, \'N\' for No: ')
                   if add_or_ignore.upper() == 'Y' :
                       add_pediatrician(pediatrician_directory, pediatrician )
                       valid=1
                   
                   elif add_or_ignore.upper() == 'N' :
                       pediatrician='NOT_IN_SYSTEM'
                       valid=1

                   elif add_or_ignore.upper() != ('Y' and 'N'):
                       print ('Incorrect option entered. Please choose from the available options from the Pediatric EMR menu.')
                       valid=0 
                      
            child_record[Name][4]=pediatrician

            print ('Child: ', Name, '-> Pediatrician information updated to: ', pediatrician )

       elif edit_field == 5:
            valid=0
            while not valid:
             phone_number=input('Enter Parent\'s Phone Number: ')
             valid=validate_phone_number(phone_number)

            child_record[Name][5]=phone_number
            print ('Child: ', Name, '-> Phone Number information updated to: ', phone_number)

           
       elif  edit_field == 6:
            insurance=input('Enter child\'s Insurance Details: ') 
            child_record[Name][6]=insurance
            print ('Child: ', Name, '-> Insurance Details updated to: ', insurance )


       elif  edit_field == 7:
            pharmacy=input('Enter child\'s Pharmacy Details: ') 
            child_record[Name][7]=pharmacy
            print ('Child: ', Name, '-> Pharmacy Details updated to: ', pharmacy )            

 
  
  else:
     print ('Child:',Name,' is not in our database, please try again')

  write_children_directory(children_directory,'children_directory.txt')
     
def edit_pediatrician(pediatrician_record,Name):
  if Name in pediatrician_record.keys():
     view_pediatrician(pediatrician_record,Name)
     edit_field=-1 

     while edit_field <0 or edit_field > 2:
       edit_field=int(input('Enter Field to be edit: '))
       

     if edit_field == 0:
          valid=0
          while not valid:
           gender=input('Enter child gender (B/G): ')
           valid=validate_gender(gender_directory, gender)

          pediatrician_record[Name][0]=gender
          print ('pediatrician: ', Name, '-> gender information updated to: ', gender)
        
     elif  edit_field == 1:
        speciality=input('Enter Pediatrician Speciality: ') 
        pediatrician_record[Name][1]=speciality
        print ('Pediatrician: ', Name, '-> Speciality information updated to: ', speciality )

     elif edit_field == 2:
          valid=0
          while not valid:
           phone_number=input('Enter Pediatrician\'s Phone Number: ')
           valid=validate_phone_number(phone_number)

          pediatrician_record[Name][2]=phone_number
          print ('pediatrician: ', Name, '-> Phone Number information updated to: ', phone_number)
        
        
  
  else:
     print ('Pediatrician:',Name,' is not in our database, please try again')

  write_pediatrician_directory(pediatrician_directory,'pediatrician_directory.txt')


######################################################
#      List All Children/Pediatrician section
######################################################


def list_all_child(child_record,sortby):
  sort1={}


  print ('Child\'s Name'.ljust(20),'Age'.ljust(6),'DOB'.ljust(12),'Gender'.ljust(8),'Address'.ljust(45),\
  'Pediatrician'.ljust(16), 'Parent\'s Contact'.ljust(18), 'Insurance'.ljust(18), 'Pharmacy'.ljust(10) )
  print (160*'-')
  

  if sortby=='by_name':
     sort1=sorted(child_record.keys())
     for name in sort1:
      print (name.ljust(20),child_record[name][0].ljust(6), child_record[name][1].ljust(12),child_record[name][2].ljust(8)\
      ,child_record[name][3].ljust(45),child_record[name][4].ljust(16), child_record[name][5].ljust(18),\
             child_record[name][6].ljust(18), child_record[name][7].ljust(10))
  else:
     sort1 = sorted(children_directory.items(), key=operator.itemgetter(1))
     for rec in sort1:
      name=rec[0]
      print (rec[0].ljust(20),rec[1][0].ljust(6), rec[1][1].ljust(12),rec[1][2].ljust(8),\
      rec[1][3].ljust(45),rec[1][4].ljust(16), rec[1][5].ljust(18), rec[1][6].ljust(18), rec[1][7].ljust(10))

def list_all_pediatrician(pediatrician_record,sortby):
  sort1={}


  print ('Name'.ljust(12),'Gender'.ljust(8),'Speciality'.ljust(12),'Phonenumber'.ljust(16))
  print (80*'-')

  sort1=sorted(pediatrician_record.keys())
  for name in sort1:
      print (name.ljust(12),pediatrician_record[name][0].ljust(8),pediatrician_record[name][1].ljust(12)\
      ,pediatrician_record[name][2].ljust(16))


#################################################
#selection
#################################################


main_selection='0'
while main_selection.upper() != 'Q':
   cls()
   print ('\t\t *****  Pediatric EMR Menu  *****\n')

   print ('Press the button \'C\' for Accessing Child Info Database')
   print ('Press the button \'P\' for Accessing Pediatrician Info Database')
   print ('')

   main_selection=input ('Enter one of the selections as listed above (Press the button \'Q\' to quit): ')
   if main_selection.upper() == 'C' :

       print ('')
       print ('You have selected the option to access Child database')
       print ('Press the button \'A\' for Adding Child\'s Profile')
       print ('Press the button \'V\' for Viewing Child\'s Profile')
       print ('Press the button \'L\' for Listing All Child Profiles (Sorted by name or age)')
       print ('Press the button \'E\' for Editing Child Profile \n')
       print ('Press the button \'ACV\' for Adding Child\'s Visit Info')
       print ('Press the button \'VCV\' for Viewing Child\'s Visit Info')
       print ('Press the button \'ACA\' for Adding Child\'s Appointment Info')
       print ('Press the button \'VCA\' for Viewing Child\'s Appointment Info \n') #Viewing instead of Adding

       while True:
                      
           child_selection=input ('Enter one of the selections as listed above: ')
           print('')

           if child_selection.upper() ==  'A' :
              retreive_children_directory(children_directory,'children_directory.txt')

              name=input('Enter Child\'s Name to Add: ')
              add_child(children_directory, name)
              break

           elif child_selection.upper() == 'V' :
              retreive_children_directory(children_directory,'children_directory.txt')
              name=input('Enter Child\'s Name to View: ')
              view_child(children_directory,name)
              break


           elif child_selection.upper() == 'L' :
              retreive_children_directory(children_directory,'children_directory.txt')
              while True:
       

                  list_by_input=input ('How would you like to list the information? \
\nPress the button \'N\' to sort by Name or \'A\' to sort by Age: ')

          
                  if list_by_input.upper() == 'N' :
                      print ('You have selected the option to sort by Name. Here is the list that you requested.\n')
                      list_by='by_name'
                      break
       
                  elif list_by_input.upper() == 'A' :
                      print ('You have selected the option to sort by Age. Here is the list that you requested.\n')
                      list_by='by_age'
                      break

                  elif list_by_input.upper() != ('N' and 'A') :
                      print ('Incorrect option entered. Press enter the correct option from the menu.')
                      continue
          
              list_all_child(children_directory, list_by)
              break

           elif child_selection.upper() == 'E' :
              retreive_children_directory(children_directory,'children_directory.txt')
              name=input('Enter Child\'s Name to be edited: ')
              edit_child(children_directory,name)
              break

           elif child_selection.upper() == 'ACV':
              retreive_children_directory(children_directory,'children_directory.txt')
              retreive_children_visit_directory(children_visit_directory,'children_visit_directory.txt')
              name=input('Enter Child Name for the visit (add):')
              add_child_visit(children_directory, children_visit_directory,name)
              break
            
           elif child_selection.upper() == 'VCV':
              retreive_children_directory(children_directory,'children_directory.txt')
              retreive_children_visit_directory(children_visit_directory,'children_visit_directory.txt')
              name=input('Enter Child Name for the visit history (view):')
              view_child_visit(children_directory, children_visit_directory,name)
              break
              
           elif child_selection.upper() == 'ACA':
              retreive_children_directory(children_directory,'children_directory.txt')
              retreive_children_appointment_directory(children_appointment_directory,'children_appointment_directory.txt')
              name=input('Enter Child Name to have appointment to be added:')
              add_child_appointment(children_directory,children_appointment_directory,name)
              break

              
           elif child_selection.upper() == 'VCA':
              retreive_children_directory(children_directory,'children_directory.txt')
              retreive_children_appointment_directory(children_appointment_directory,'children_appointment_directory.txt')
              name=input('Enter Child Name for the appointment history (view):')
              view_child_appointment(children_directory,children_appointment_directory,name)
              break
      
           elif child_selection.upper() != ('A' and 'V' and 'L' and 'E' and 'ACV' and 'VCV' and 'ACA' and 'VCA'):
              print('')
              print ('Incorrect option entered. Please choose from the available options.')
              continue

   elif main_selection.upper() == 'P' :

       print ('')
       print ('You have selected the option to access Pediatrician database')
       print ('Press the button \'A\' for Adding Pediatrician\'s Info')
       print ('Press the button \'V\' for Viewing Pediatrician\'s Info')
       print ('Press the button \'L\' for Listing All Profiles (Sorted by name)')
       print ('Press the button \'E\' for Editing Pediatrician\'s Info \n')

       while True:
           ped_selection=input ('Enter one of the selections as listed above: ')
           print('')

           if ped_selection.upper() == 'A' :
              retreive_pediatrician_directory(pediatrician_directory,'pediatrician_directory.txt')

              name=input('Enter Pediatrician\'s Name to be added: ')
              add_pediatrician(pediatrician_directory, name)
              break

           elif ped_selection.upper() == 'V' :
              retreive_pediatrician_directory(pediatrician_directory,'pediatrician_directory.txt')
              name=input('Enter Pediatrician\'s Name to be viewed: ')
              view_pediatrician(pediatrician_directory,name)
              break


           elif ped_selection.upper() == 'L' :
              retreive_pediatrician_directory(pediatrician_directory,'pediatrician_directory.txt')     
              list_all_pediatrician(pediatrician_directory, 'by_name')
              break

           elif ped_selection.upper() == 'E' :
              retreive_pediatrician_directory(pediatrician_directory,'pediatrician_directory.txt')
              name=input('Enter Pediatrician\'s Name to be edited: ')
              edit_pediatrician(pediatrician_directory,name)
              break
      
           elif ped_selection.upper() != ('A' and 'V' and 'L' and 'E'):
              print('')
              print ('Incorrect option entered. Please choose from the available options.')
              continue

   elif main_selection.upper() != ('C' and 'P' and 'Q' ):

       print ('Incorrect option entered. Please choose from the available options from the Pediatric EMR menu.')



