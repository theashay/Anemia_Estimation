from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd
    from joblib import dump, load
    from PIL import Image ,ImageTk

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()
    w,h = root.winfo_screenwidth(),root.winfo_screenheight()
    root.title("Check Anemia Disease")
    root.geometry("%dx%d+0+0"%(w,h))
    root.configure(background="#7FFFD4")

    
    w,h = root.winfo_screenwidth(),root.winfo_screenheight()
    
    bg = Image.open(r"a.png")
    bg.resize((1366,500),Image.ANTIALIAS)
    print(w,h)
    bg_img = ImageTk.PhotoImage(bg)
    bg_lbl = tk.Label(root,image=bg_img)
    bg_lbl.place(x=600,y=93)
   
    LAB_TEST = tk.IntVar()
    RESULT = tk.DoubleVar()
    PDW = tk.DoubleVar()
    Probablity_health = tk.DoubleVar()
    GENDER = tk.IntVar()
    
    
    #===================================================================================================================



    def Detect():
        e1= LAB_TEST.get()
        print(e1)
        e2=RESULT.get()
        print(e2)
        e3= PDW.get()
        print(e3)
        e4= Probablity_health.get()
        print(e4)
        e5= GENDER.get()
        print(e5)
    
        #########################################################################################
        
        from joblib import dump , load
        a1=load('anemia_MODEL.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5]])
        print(v)
        if v[0]==1:
            print("Yes")
            yes = tk.Label(root,text="Animeai Disease \nDetected!",background="red",foreground="white",font=('times', 20, ' bold '),width=15)
            yes.place(x=280,y=600)
            # file = open(r"D:/ashwini bitmap folder 2023/23C9513 Anemia Estimation (ML)/anemia_estimation 100% code/Report.txt", 'w')
            # file.write("-----Patient Report-----\n As per input data and system model Anemia Disease Detected for Respective Paptient."
            #            "\n***Kindly Follow Medicatins***"
                    
            #         )
            # file.close()
            
        else:
            print("No")
            no = tk.Label(root, text="No Disease \nDetected", background="green", foreground="white",font=('times', 20, ' bold '),width=15)
            no.place(x=280, y=600)
            # file = open(r"D:/ashwini bitmap folder 2023/23C9513 Anemia Estimation (ML)/anemia_estimation 100% code/Report.txt", 'w')
            # file.write("-----Patient Report-----\n As per input data and system model No Anemia Disease Detected for Respective Paptient."
            #            "\n\n***Relax and Follow below mentioned Life Style to be Healthy as You Are!!!***"
                    
            #         )
            # file.close()

 
    label=tk.Label(root,text='''
               Huge doses of Vitamin B12 had profound 
               beneficial effects on my health. Iron 
               deficiency anemia is a global pandemic! 
               Anemia made the tissues and organs small and pale.
               '''
               ,font=("Calibri",12),bg="pink",
               
               fg="black")
    label.place(x=650,y=350)
    

    l1=tk.Label(root,text="LAB_TEST",background="#7FFFD4",font=('times', 20, ' bold '),width=10)
    l1.place(x=5,y=40)
    # LAB_TEST=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar= LAB_TEST)
    # LAB_TEST.place(x=200,y=1)
    R1 = Radiobutton(root, text="Hemoglobin", variable=LAB_TEST, value=1).place(x=5,y=80)
    R2 = Radiobutton(root, text="MCH", variable=LAB_TEST, value=2).place(x=5,y=120)
    R3 = Radiobutton(root, text="MCHC", variable=LAB_TEST, value=3).place(x=5,y=160)
    R4 = Radiobutton(root, text="MCV", variable=LAB_TEST, value=3).place(x=5,y=200)


    l2=tk.Label(root,text="RESULT",background="#7FFFD4",font=('times', 20, ' bold '),width=10)
    l2.place(x=5,y=250)
    RESULT=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=RESULT)
    RESULT.place(x=500,y=250)

    l3=tk.Label(root,text="PDW",background="#7FFFD4",font=('times', 20, ' bold '),width=7)
    l3.place(x=5,y=300)
    RESULT=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=RESULT)
    RESULT.place(x=500,y=300)
    
    l4=tk.Label(root,text="Probablity_health",background="#7FFFD4",font=('times', 20, ' bold '),width=16)
    l4.place(x=5,y=350)
    RESULT=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=RESULT)
    RESULT.place(x=500,y=350)
    

    l5=tk.Label(root,text="GENDER",background="#7FFFD4",font=('times', 20, ' bold '),width=10)
    l5.place(x=5,y=400)
    GENDER=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=GENDER)
    GENDER.place(x=500,y=400)

   

    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=300,y=450)
    
    # button1 = tk.Button(root,text="train",command=Detect,font=('times', 20, ' bold '),width=10)
    # button1.place(x=50,y=520)
    


    root.mainloop()

Train()