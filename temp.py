from tkinter import*
root =Tk()
root.title("Fever_Report")
root.geometry("600x600")

question1_radiobutton=StringVar(value="0")

Question1=Label(root,text="Do you have headache and sore throat ? ")
Question1.pack()
Question1_r1=Radiobutton(root,text="yes",varialbe=question1_radiobutton,value="yes")
Question1_r1.pack()
question1_r2=Radiobutton(root,text="no",varialbe=question1_radiobutton,value="no")
Question_1r2.pack()

question2_radiobutton=StringVar(value="0")

Question2=Label(root,text="Is your body temperature high ? ")
Question2.pack()
Question2_r1=Radiobutton(root,text="yes",varialbe=question1_radiobutton,value="yes")
Question2_r1.pack()
question2_r2=Radiobutton(root,text="no",varialbe=question1_radiobutton,value="no")
Question2_r2.pack()

question3_radiobutton=StringVar(value="0")

Question3=Label(root,text="Are there any symptoms of eye redness ? ")
Question3.pack()
Question3_r1=Radiobutton(root,text="yes",varialbe=question1_radiobutton,value="yes")
Question3_r1.pack()
question3_r2=Radiobutton(root,text="no",varialbe=question1_radiobutton,value="no")
Question3_r2.pack()

def fever_score():
    score=0
    if question1_radiobutton.get()=="yes":
        score=score+20
        print(score)
    if question2_radiobutton.get()=="yes":
        score=score+20
        print(score)
    if question3_radiobutton.get()=="yes":
        score=score+20
        print(score)
        
    if   score <= 20:
        messagebox.showinfo("Report","Yod don't need to visit a doctor.")
    elif score > 20 and score<=40:
        messagebox.showinfo("Report","You might prehaps to visit a doctor.")
    else:
        messagebox.showinfo("Report","I strongly advise you to visit a doctor.")
        
btn=Button(root,text="click me",command=fever_score)
btn.pack()
root.mainloop()        