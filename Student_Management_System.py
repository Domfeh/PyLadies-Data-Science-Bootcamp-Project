'Building a mini project about student management system using Tkinter as the GUI'
'Áuthor: DOMFEH ADWOA MARY'

from PIL import Image,ImageTk # imports the pillow library 
import tkinter as tk
from tkinter import Canvas, Frame, Label,Button,Tk, Entry,messagebox



window = tk.Tk()
window.title("Student Management Portal")

count=0

Faculty_info={}
Student_info={}

Faculty_Passwords=[]
Student_Passwords=[]


Faculty_IDs=[]
Student_IDs=[]

' Adding a homepage image'

n=1.5

home_image = Image.open("Ashesi.jpg")
[image_Size_Width, image_Size_Height] = home_image.size

New_Image_Size_Width = int(image_Size_Width*n)
if True:
    New_Image_Size_Height = int(image_Size_Height*n) 
else:
   New_Image_Size_Height = int(image_Size_Height/n) 
    
home_image = home_image.resize((New_Image_Size_Width,New_Image_Size_Height))
img = ImageTk.PhotoImage(home_image)


# Faculty & Student Home Page 
def Faculty_Student_homePage():
    
    global head_Frame1,head_Frame2,head_Label,btn1,btn2,Canvas1
    head_Frame1.destroy()
    head_Frame2.destroy()
    head_Label.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    
    Canvas1 = Canvas(window)

    Canvas1.config(bg="#ffa710",width = New_Image_Size_Width, height = New_Image_Size_Height)
    Canvas1.pack(expand=True,fill='both')

    
    head_Frame1 = Frame(window,bg="#333945",bd=5)
    head_Frame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    head_Frame2 = Frame(head_Frame1,bg="#EAF0F1")
    head_Frame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
     
    btn2 = Button(window,text="Login",bg='black', fg='black',command=Login)
    btn2.place(relx=0.53,rely=0.3, relwidth=0.2,relheight=0.1)
    
    


# Faculty Home Page 
def Faculty():
     Faculty_Student_homePage()
        
     head_Label = Label(head_Frame2, text="Welcome Faculty!", fg='black')
     head_Label.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)


     btn1 = Button(window,text="Register",bg='black', fg='black',command=Faculty_Registeration)
     btn1.place(relx=0.28,rely=0.3, relwidth=0.2,relheight=0.1)

     btn3 = Button(window,text="<  BACK",bg='black', fg='black',command=Student)
     btn3.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)


# Student Home Page 
def Student():
     Faculty_Student_homePage()

     head_Label = Label(head_Frame2, text="Welcome Student!", fg='black')
     head_Label.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)


     btn1 = Button(window,text="Register",bg='black', fg='black',command=Student_Registeration)
     btn1.place(relx=0.28,rely=0.3, relwidth=0.2,relheight=0.1)

     btn3 = Button(window,text="<  BACK",bg='black', fg='black',command=Faculty)
     btn3.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

'''
Database administration
'''
def get_Faculty_Info():
 
    
    ID =entry1.get()
    NAME = entry2.get()
    password = entry3.get()
    DEPARTMENT = entry4.get()
    DEPARTMENT.lower()
   
    
    try:
        if (type(int(ID)) == int):
            
            a=str(ID)
            Faculty_info[a]={}
            
            Faculty_info[a]['Name']= NAME
            Faculty_info[a]['Password']= password
            Faculty_info[a]['Department']=DEPARTMENT
            
            messagebox.showinfo ("Faculty Registration successful!!")      
        
        else:   
            messagebox.showinfo("Faculty ID should be an integer")
            return
    except:
        messagebox.showinfo("Invalid Value","Faculty ID should be an integer")
        return
    
 # automatically deletes the inputs after submission 
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')  
    print("Faculty Information: ",Faculty_info)


def get_Student_Info():


    global entry1,entry2,entry3,entry4

    ID = entry1.get()
    NAME = entry2.get()
    password = entry3.get()
    DEPARTMENT = entry4.get()
    
    
    
    try:
        if (type(int(ID)) == int):

            a=str(ID)
            Student_info[a]={}
            
            Student_info[a]['Name']= NAME
            Student_info[a]['Password']= password
            Student_info[a]['Department']=DEPARTMENT            
            messagebox.showinfo ("Student Registration successful!!")      
            
            
        else:
            messagebox.showinfo("Invalid Value","Student ID should be an integer")
            return
    except:
        messagebox.showinfo("Invalid Value","Student ID should be an integer")
        return
        
    # automatically deletes the inputs after submission
    
    
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    print("Student Information: ",Student_info)


def Faculty_Registeration():

    
      
    global label_Frame,entry1,entry2,entry3,entry4
     
    
    global count
    count =count + 1

    if(count>=2):
        label_Frame.destroy()
   
    label_Frame = Frame(window,bg='black')
    label_Frame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.42)
     # Employee/ Student  ID
    label1 = Label(label_Frame,text="ID : ", bg='black', fg='white')
    label1.place(relx=0.05,rely=0.05)
    
    entry1 = Entry(label_Frame)
    entry1.place(relx=0.3,rely=0.05, relwidth=0.62)
    
    #Employee/Student Name
    label2 = Label(label_Frame,text="Full Name : ", bg='black', fg='white')
    label2.place(relx=0.05,rely=0.2)
    
    entry2 = Entry(label_Frame)
    entry2.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    #Employee/Student Paswword
    label3 = Label(label_Frame,text="Password : ", bg='black', fg='white')
    label3.place(relx=0.05,rely=0.35)
    
    entry3 = Entry(label_Frame)
    entry3.place(relx=0.3,rely=0.35, relwidth=0.62)
    
    #Employee/Student Department
    label4 = Label(label_Frame,text="Department : ", bg='black', fg='white')
    label4.place(relx=0.05,rely=0.5)
    
    entry4 = Entry(label_Frame)
    entry4.place(relx=0.3,rely=0.5, relwidth=0.62)

    
    
    Submit_Button = Button(window,text="SUBMIT",bg='#264348', fg='black',command=get_Faculty_Info)
    Submit_Button.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)



def Student_Registeration():
    
    global label_Frame,entry1,entry2,entry3,entry4
    
    global count
    count += 1

    if(count>=2):
        label_Frame.destroy()


   
    label_Frame = Frame(window,bg='black')
    label_Frame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.42)

     # Student  ID
    label1 = Label(label_Frame,text="ID : ", bg='black', fg='white')
    label1.place(relx=0.05,rely=0.05)
    
    entry1 = Entry(label_Frame)
    entry1.place(relx=0.3,rely=0.05, relwidth=0.62)
    
    #Student Name
    label2 = Label(label_Frame,text="Full Name : ", bg='black', fg='white')
    label2.place(relx=0.05,rely=0.2)
    
    entry2 = Entry(label_Frame)
    entry2.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    #Student Paswword
    label3 = Label(label_Frame,text="Password : ", bg='black', fg='white')
    label3.place(relx=0.05,rely=0.35)
    
    entry3 = Entry(label_Frame)
    entry3.place(relx=0.3,rely=0.35, relwidth=0.62)
    
    #Student Department
    label4 = Label(label_Frame,text="Department : ", bg='black', fg='white')
    label4.place(relx=0.05,rely=0.5)
    
    entry4 = Entry(label_Frame)
    entry4.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    
  
    Submit_Button = Button(window,text="SUBMIT",bg='#264348', fg='black',command=get_Student_Info)
    Submit_Button.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)



def Login_Ids_Faculty():
    
   
    Faculty_Ids= list(Faculty_info.keys())
    for i in Faculty_Ids:
        
        a=str(i)
       
        x=Faculty_info[a]['Password']
        Faculty_Passwords.append(x)
        b=int(a)
        Faculty_IDs.append(b)
        
       
##    print('Faculty_Password: ', Faculty_Passwords)
##    print('Login_Ids_Faculty: ', Faculty_IDs)
##    
    
        
def Login_Ids_Student():
    
    Student_Ids= list(Student_info.keys())
    for i in Student_Ids:
    
        
        a=str(i)
       
        x=Student_info[a]['Password']
        Student_Passwords.append(x)
        b=int(a)
        Student_IDs.append(b)

##    print('Student_Pasword: ', Student_Passwords)    
##    print('Login_Ids_Student: ', Student_IDs)


        



def Faculty_Menu():
    
 
    global head_Frame1,head_Frame2,head_Label,Submit_Button,Canvas1,labelFrame,backBtn
    head_Frame1.destroy()
    head_Frame2.destroy()
    head_Label.destroy()
    Canvas1.destroy()
    Submit_Button.destroy()
      
    Canvas1 = Canvas(window)

    Canvas1.config(bg="#ffa710",width = New_Image_Size_Width, height = New_Image_Size_Height)
    Canvas1.pack(expand=True,fill='both')
    
    head_Frame1 = Frame(window,bg="#333945",bd=5)
    head_Frame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    head_Frame2 = Frame(head_Frame1,bg="#EAF0F1")
    head_Frame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    head_Label = Label(head_Frame2, text="Faculty MENU", fg='black')
    head_Label.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(window,text="Update Student Details",bg='black', fg='black',command=UpdateStudentInfo)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(window,text="Delete Student",bg='black', fg='black',command=deleteStudent)
    btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(window,text="View All Students",bg='black', fg='black',command =Display_All_Student_Info)
    btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn4 = Button(window,text="Search Student",bg='black', fg='black',command= SearchStudent)
    btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    

    backBtn = Button(window,text="<  BACK",bg='#455A64', fg='black',command=Faculty)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)

def Student_Menu():
    
 
    global head_Frame1,head_Frame2,head_Label,Submit_Button,Canvas1,labelFrame,backBtn
    head_Frame1.destroy()
    head_Frame2.destroy()
    head_Label.destroy()
    Canvas1.destroy()
    Submit_Button.destroy()
    
    Canvas1 = Canvas(window)

    Canvas1.config(bg="#ffa710",width = New_Image_Size_Width, height = New_Image_Size_Height)
    Canvas1.pack(expand=True,fill='both')
    
    head_Frame1 = Frame(window,bg="#333945",bd=5)
    head_Frame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    head_Frame2 = Frame(head_Frame1,bg="#EAF0F1")
    head_Frame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    head_Label = Label(head_Frame2, text="Student MENU", fg='black')
    head_Label.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn3 = Button(window,text="View GPA",bg='black', fg='black', command=Get_GPA)
    btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn4 = Button(window,text="Display Courses Grade",bg='black', fg='black',command=Display_Courses_Grade)
    btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
    
    backBtn = Button(window,text="<  BACK",bg='#455A64', fg='black',command=Student)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)


 
def get_Login_Info():
    


    global entry1,entry2,entry3,entry4
    
    login = entry1.get()
    name = entry2.get()
    password = entry3.get()
    role = entry4.get()
    role.lower()
    
    
    if (role == 'faculty'):

         Login_Ids_Faculty()
         
         
         
        
         try:
            
            for i,c in zip(Faculty_IDs,Faculty_Passwords):
                
                getLoginID = i
                getPassword = c                
                login=int(login)                
            
            if(getLoginID == login and getPassword == password):               
               messagebox.showinfo("SUCCESS","You have successfully logged in")
               Faculty_Menu()       
                
            else:                             
                messagebox.showerror("Failure","Can't log in, check your credentials")
         except:                         
             messagebox.showinfo("FAILED","Please check your credentials")            
    elif (role == 'student'):
        
        Login_Ids_Student()        
        try:
           
            for (i,c) in zip( Student_IDs,Student_Passwords) :
                getLoginID = i
                getPassword = c
                login=int(login)
            
            if(getLoginID == login and getPassword == password):
                
                messagebox.showinfo("SUCCESS","You have successfully logged in")
                Student_Menu()
            else:
                messagebox.showerror("Failure","Can't log in, check your credentials")
        except:
            messagebox.showinfo("FAILED","Please check your credentials")        
    else:
        messagebox.showinfo("EXCEPTION","Role can only be faculty or student")
        return
    
   
     # automatically deletes the inputs after submission 
    
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')


# Login for Faculty and Student
def Login():
    
    global label_Frame
    
    global count
    count += 1

    if(count>=2):
        label_Frame.destroy()
    
    global entry1,entry2,entry3,entry4,Submit_Button,btn1,btn2,btn3
    
    label_Frame = Frame(window,bg='black')
    label_Frame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.3)
    
    # Login ID
    label1 = Label(label_Frame,text="Login ID : ", bg='black', fg='white')
    label1.place(relx=0.05,rely=0.1)
    
    entry1 = Entry(label_Frame)
    entry1.place(relx=0.3,rely=0.1, relwidth=0.62)
    
    # Name
    label2 = Label(label_Frame,text="Name : ", bg='black', fg='white')
    label2.place(relx=0.05,rely=0.3)
    
    entry2 = Entry(label_Frame)
    entry2.place(relx=0.3,rely=0.3, relwidth=0.62)
    
    # Paswword
    label3 = Label(label_Frame,text="Password : ", bg='black', fg='white')
    label3.place(relx=0.05,rely=0.5)
    
    entry3 = Entry(label_Frame)
    entry3.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    # Role
    label4 = Label(label_Frame,text="Role : ", bg='black', fg='white')
    label4.place(relx=0.05,rely=0.7)
    
    entry4 = Entry(label_Frame)
    entry4.place(relx=0.3,rely=0.7, relwidth=0.62)
    
    #Submit Button
    Submit_Button = Button(window,text="SUBMIT",bg='#264348', fg='black',command=get_Login_Info)
    Submit_Button.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    

def Display_All_Student_Info():
    
    for (i,c) in zip(Student_IDs, Student_Passwords):
        a=str(i)

        try:
                                   
            x=i
            y=Student_info[a]['Name']
            z=Student_info[a]['Department']
            messagebox.showinfo("Displaying All available student Inforamtion")


        except:
            messagebox.showinfo("Invalid ID")
            
        

        print("ID   : ", x) 
        print("Name : ", y)  
        print("Department: ", z) 
        print("\n")
        return
        
        
def Search_For_Student():
    global entry1
    Stud_Id= entry1.get()
    
    for i in Student_IDs:
        a=str(i)


        try:
            if (Stud_Id==a):
                x=Stud_Id
                y=Student_info[a]['Name']
                z=Student_info[a]['Department']
                
                messagebox.showinfo(" Student Found ")
              
                
            else:
                
                messagebox.showinfo(" Student ID not found  ")
                return
               
        except:
                        
            messagebox.showinfo("Invalid ID")
            return
            
        
                
        entry1.delete(0, 'end')
        print("ID   : ", x)
        print("Name : ", y)
        print("Department: ", z)
        print("\n")
        return


def SearchStudent():
    
    global head_Frame1,head_Frame2,head_Label,Canvas1,Submit_Button,entry1
    head_Frame1.destroy()
    head_Frame2.destroy()
    head_Label.destroy()
    Canvas1.destroy()
    Submit_Button.destroy()

   
    Canvas1 = Canvas(window)
    label_Frame = Frame(window,bg='black')
    label_Frame.place(relx=0.35,rely=0.44,relwidth=0.3,relheight=0.42)

    Canvas1.config(bg="#ffa710",width = New_Image_Size_Width, height = New_Image_Size_Height)
    Canvas1.pack(expand=True,fill='both')
    
    head_Frame1 = Frame(window,bg="#333945",bd=5)
    head_Frame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    head_Frame2 = Frame(head_Frame1,bg="#EAF0F1")
    head_Frame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    head_Label = Label(head_Frame2, text="Search For a Student", fg='black')
    head_Label.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
     # Student  ID
    label1 = Label(label_Frame,text="ID : ", bg='black', fg='white')
    label1.place(relx=0.05,rely=0.05)
    
    entry1 = Entry(label_Frame)
    entry1.place(relx=0.3,rely=0.05, relwidth=0.62)
    
    
    Submit_Button = Button(window,text="SUBMIT",bg='#264348', fg='black',command=Search_For_Student)
    Submit_Button.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    
    backBtn = Button(window,text="<  BACK",bg='#455A64', fg='black',command=Faculty_Menu)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)
    


def Update_Student_Info():
    global entry1,entry2,entry3,entry4,entry5
    Stud_Id= entry1.get()
    Physics_Marks=entry2.get()
    Maths_Marks=entry3.get()
    Biology_Marks=entry4.get()
    GPA=entry5.get()
    
    
    for i in  (Student_IDs):
        a=str(i)


        try:
            if (Stud_Id==a):
                
                
                
                Student_info[a]['Physics_Marks']=Physics_Marks
                Student_info[a]['Maths_Marks']=Maths_Marks
                Student_info[a]['Biology_Marks']=Biology_Marks
                Student_info[a]['GPA']=GPA
                
                messagebox.showinfo(" Student info Updated ")
                
                
            else:
                
                
                messagebox.showinfo(" Student ID not found  ")
                return
               
        except:
            
                        
            messagebox.showinfo("Invalid ID")
            return
        
        entry1.delete(0, 'end')   
        entry2.delete(0, 'end')
        entry3.delete(0, 'end')
        entry4.delete(0, 'end')      
        entry5.delete(0, 'end')
        print(Student_info)
        return


def UpdateStudentInfo ():
    
    global head_Frame1,head_Frame2,head_Label,Canvas1,Submit_Button,entry1,entry2,entry3,entry4,entry5
    head_Frame1.destroy()
    head_Frame2.destroy()
    head_Label.destroy()
    Canvas1.destroy()
    Submit_Button.destroy()

   
    Canvas1 = Canvas(window)
    label_Frame = Frame(window,bg='black')
    label_Frame.place(relx=0.35,rely=0.44,relwidth=0.3,relheight=0.42)

    Canvas1.config(bg="#ffa710",width = New_Image_Size_Width, height = New_Image_Size_Height)
    Canvas1.pack(expand=True,fill='both')
    
    head_Frame1 = Frame(window,bg="#333945",bd=5)
    head_Frame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    head_Frame2 = Frame(head_Frame1,bg="#EAF0F1")
    head_Frame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    head_Label = Label(head_Frame2, text="Update Student Info", fg='black')
    head_Label.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
     # Student  ID
    label1 = Label(label_Frame,text="ID : ", bg='black', fg='white')
    label1.place(relx=0.05,rely=0.05)
    
    entry1 = Entry(label_Frame)
    entry1.place(relx=0.3,rely=0.05, relwidth=0.62)


    # Physiscs Marks
    label2 = Label(label_Frame,text="Physiscs Marks : ", bg='black', fg='white')
    label2.place(relx=0.05,rely=0.3)
    
    entry2 = Entry(label_Frame)
    entry2.place(relx=0.3,rely=0.3, relwidth=0.62)
    
    # Maths Marks
    label3 = Label(label_Frame,text="Maths Marks : ", bg='black', fg='white')
    label3.place(relx=0.05,rely=0.5)
    
    entry3 = Entry(label_Frame)
    entry3.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    # Biology Marks
    label4 = Label(label_Frame,text="Biology Marks : ", bg='black', fg='white')
    label4.place(relx=0.05,rely=0.7)
    
    entry4 = Entry(label_Frame)
    entry4.place(relx=0.3,rely=0.7, relwidth=0.62)



    # GPA
    label5 = Label(label_Frame,text="GPA : ", bg='black', fg='white')
    label5.place(relx=0.05,rely=0.9)
    
    entry5 = Entry(label_Frame)
    entry5.place(relx=0.3,rely=0.9, relwidth=0.62)
    
        
    Submit_Button = Button(window,text="SUBMIT",bg='#264348', fg='black',command=Update_Student_Info)
    Submit_Button.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    
    backBtn = Button(window,text="<  BACK",bg='#455A64', fg='black',command=Faculty_Menu)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)



def Student_GPA():
    
    global entry1
    Id= entry1.get()
   
    
    for i in (Student_IDs):
        
        z=str(i)


        try:
            if (Id==z):
                
                n=Student_info[z]['GPA']
                
                
                
                messagebox.showinfo(" Get GPA successful")
                
                
                
            else:
                
                messagebox.showinfo(" Invalid Student ID  ")
                return
               
        except:
                        
            messagebox.showinfo("Invalid ID")
            return
            
       
        entry1.delete(0, 'end')
       
        print("The GPA is : ",n)
        return
                
        


def Get_GPA():
    
    global head_Frame1,head_Frame2,head_Label,Canvas1,Submit_Button,entry1
    head_Frame1.destroy()
    head_Frame2.destroy()
    head_Label.destroy()
    Canvas1.destroy()
    Submit_Button.destroy()

   
    Canvas1 = Canvas(window)
    label_Frame = Frame(window,bg='black')
    label_Frame.place(relx=0.35,rely=0.44,relwidth=0.3,relheight=0.42)

    Canvas1.config(bg="#ffa710",width = New_Image_Size_Width, height = New_Image_Size_Height)
    Canvas1.pack(expand=True,fill='both')
    
    head_Frame1 = Frame(window,bg="#333945",bd=5)
    head_Frame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    head_Frame2 = Frame(head_Frame1,bg="#EAF0F1")
    head_Frame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    head_Label = Label(head_Frame2, text="Student GPA", fg='black')
    head_Label.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
     # Student  ID
    label1 = Label(label_Frame,text="ID : ", bg='black', fg='white')
    label1.place(relx=0.05,rely=0.05)
    
    entry1 = Entry(label_Frame)
    entry1.place(relx=0.3,rely=0.05, relwidth=0.62)
    
    
    Submit_Button = Button(window,text="SUBMIT",bg='#264348', fg='black',command=Student_GPA)
    Submit_Button.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    
    backBtn = Button(window,text="<  BACK",bg='#455A64', fg='black',command=Student_Menu)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)
    


def Display_Courses():
    global entry1
    Stud_Id= entry1.get()
    
    for i in  (Student_IDs):
        a=str(i)


        try:
            if (Stud_Id==a):
                x=Stud_Id
                y=Student_info[a]['Physics_Marks']
                z=Student_info[a]['Maths_Marks']
                s=Student_info[a]['Biology_Marks']
                
                messagebox.showinfo(" Course Grades Available!! ")
                
                
            else:
                
                messagebox.showinfo(" Invalid Student ID ")
                return
               
        except:
                        
            messagebox.showinfo("Invalid ID")
            return
            
        
                
        entry1.delete(0, 'end')
        print("Physics Marks  : ", y)
        print("Maths Marks : ", z)
        print("Biology Marks: ", s)
        print("\n")
        return


def Display_Courses_Grade():
    
    global head_Frame1,head_Frame2,head_Label,Canvas1,Submit_Button,entry1
    head_Frame1.destroy()
    head_Frame2.destroy()
    head_Label.destroy()
    Canvas1.destroy()
    Submit_Button.destroy()

   
    Canvas1 = Canvas(window)
    label_Frame = Frame(window,bg='black')
    label_Frame.place(relx=0.35,rely=0.44,relwidth=0.3,relheight=0.42)

    Canvas1.config(bg="#ffa710",width = New_Image_Size_Width, height = New_Image_Size_Height)
    Canvas1.pack(expand=True,fill='both')
    
    head_Frame1 = Frame(window,bg="#333945",bd=5)
    head_Frame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    head_Frame2 = Frame(head_Frame1,bg="#EAF0F1")
    head_Frame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    head_Label = Label(head_Frame2, text="Display Student Courses", fg='black')
    head_Label.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
     # Student  ID
    label1 = Label(label_Frame,text="ID : ", bg='black', fg='white')
    label1.place(relx=0.05,rely=0.05)
    
    entry1 = Entry(label_Frame)
    entry1.place(relx=0.3,rely=0.05, relwidth=0.62)
    
    
    Submit_Button = Button(window,text="SUBMIT",bg='#264348', fg='black',command=Display_Courses)
    Submit_Button.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    
    backBtn = Button(window,text="<  BACK",bg='#455A64', fg='black',command=Student_Menu)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)
    


def delete_Stu():
    global entry1
    stu_delete_id= entry1.get()
    delete_id=int(stu_delete_id)
    
    

    for (i,c) in zip(Student_IDs, Student_Passwords):
        a=str(i)
       
        x=Student_info[a]['Password']
        b=int(a)
        

        try:
            if(delete_id==b  and x== c):
                   del(Student_info[stu_delete_id])
                   messagebox.showinfo(" Student Details Deleted ")
                   
                                      
            else:               
               messagebox.showinfo(" Please Enter The Correct ID ")
               return
               
        except KeyError:
            
            
            messagebox.showinfo("Invalid ID")
            return
            

        #print(Student_Passwords)
        #print(Student_IDs)
        
        
        entry1.delete(0, 'end')
        print("The new list of Students :", Student_info)
        return
            
def deleteStudent():
    
    global head_Frame1,head_Frame2,head_Label,Canvas1,Submit_Button,entry1
    head_Frame1.destroy()
    head_Frame2.destroy()
    head_Label.destroy()
    Canvas1.destroy()
    Submit_Button.destroy()

   
    Canvas1 = Canvas(window)
    label_Frame = Frame(window,bg='black')
    label_Frame.place(relx=0.35,rely=0.44,relwidth=0.3,relheight=0.42)

    Canvas1.config(bg="#ffa710",width = New_Image_Size_Width, height = New_Image_Size_Height)
    Canvas1.pack(expand=True,fill='both')
    
    head_Frame1 = Frame(window,bg="#333945",bd=5)
    head_Frame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    head_Frame2 = Frame(head_Frame1,bg="#EAF0F1")
    head_Frame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    head_Label = Label(head_Frame2, text="Delete Student Info", fg='black')
    head_Label.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
     # Student  ID
    label1 = Label(label_Frame,text="ID : ", bg='black', fg='white')
    label1.place(relx=0.05,rely=0.05)
    
    entry1 = Entry(label_Frame)
    entry1.place(relx=0.3,rely=0.05, relwidth=0.62)
    
    
    Submit_Button = Button(window,text="SUBMIT",bg='#264348', fg='black',command=delete_Stu)
    Submit_Button.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    
    backBtn = Button(window,text="<  BACK",bg='#455A64', fg='black',command=Faculty_Menu)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)
   

Canvas1 = Canvas(window)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(width = New_Image_Size_Width, height = New_Image_Size_Height)
Canvas1.pack(expand=True, fill='both')

head_Frame1 = Frame(window,bg="#ffa710",bd=5)
head_Frame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

head_Frame2 = Frame(head_Frame1,bg="#EAF0F1")
head_Frame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

head_Label = Label(head_Frame2, text="Faculty and Student Portal", fg='black')
head_Label.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.5)

btn1 =Button(window,text="Faculty",command=Faculty)
btn1.place(relx=0.25,rely=0.3, relwidth=0.2,relheight=0.1)

btn2 = Button(window,text="Student", command=Student)
btn2.place(relx=0.55,rely=0.3, relwidth=0.2,relheight=0.1)
window.mainloop()


