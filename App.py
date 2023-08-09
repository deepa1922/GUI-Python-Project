from tkinter import *
from mydb import Database
from tkinter import messagebox
from myAPI import API
class NLPApp:

    def __init__(self):

        #create db object
        self.dbo = Database()
        self.apio = API()

        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#34495E')

        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)

        login_btn = Button(self.root,text='Login',width=30,height=2,bg='#34495e',command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root,text='Not a member?',width=15)
        label3.pack(pady=(20,10))

        redirect_btn = Button(self.root,text='Register Now',width=10,height=2,bg='#34495e',command=self.register_gui)
        redirect_btn.pack(pady=(10,10))

    def register_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', width=30, height=2, bg='#34495e',command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member?', width=15)
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now', width=10, height=2, bg='#34495e', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))
    def clear(self):
        #clear the existing gui
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        #fetch data from gui
        name = self.name_input.get()
        email=self.email_input.get()
        password= self.password_input.get()

        response = self.dbo.add_data(name,email,password)

        if response:
           messagebox.showinfo('Success','Registration successful,you can login now')
        else:
           messagebox.showerror('Error','Email already exists')

    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo('success','login successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect email/password ')

    def home_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4, bg='#34495e',
                              command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Named Entity Recoginition', width=30, height=4, bg='#34495e',
                               command=self.ner_gui)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=4, bg='#34495e',
                               command=self.emotion_gui)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout', width=10, height=2, bg='#34495e', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text', width=15)
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50,)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_btn = Button(self.root, text='Analyze Sentiment', bg='#34495e', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='',bg='#34495E',fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Previous', bg='#34495e', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result= self.apio.sentiment_analysis(text)

        txt = ''
        for i in result['sentiment']:
             txt = txt + i +'->'+ str(result['sentiment'][i]) + '\n'

        print(txt)
        self.sentiment_result['text'] = txt


    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Named Entity Recoginition', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text', width=15)
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        ner_btn = Button(self.root, text='Analyze ENR', bg='#34495e', command=self.do_ner_analysis)
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='', bg='#34495E', fg='white')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Previous', bg='#34495e', command=self.sentiment_gui)
        goback_btn.pack(pady=(10, 10))

    def do_ner_analysis(self):
        text = self.ner_input.get()
        result = self.apio.ner_analysis(text)

        txt = ''
        for entity in result['entities']:
            txt += f"Name: {entity['name']}\nCategory: {entity['category']}\nConfidence Score: {entity['confidence_score']:.2f}\n\n"

        print(txt)
        self.ner_result['text'] = txt

    def emotion_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Emotion Prediction', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text', width=15)
        label1.pack(pady=(10, 10))

        self.emotion_input = Entry(self.root, width=50)
        self.emotion_input.pack(pady=(5, 10), ipady=4)

        emotion_btn = Button(self.root, text='Analyze Emotion', bg='#34495e', command=self.do_emotion_analysis)
        emotion_btn.pack(pady=(10, 10))

        self.emotion_result = Label(self.root, text='', bg='#34495E', fg='white')
        self.emotion_result.pack(pady=(10, 10))
        self.emotion_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Previous', bg='#34495e', command=self.ner_gui)
        goback_btn.pack(pady=(10, 10))

    def do_emotion_analysis(self):
        text = self.emotion_input.get()
        result = self.apio.emotion_analyse(text)

        txt = ''
        for i in result['emotion']:
            txt += i + '->' + str(result['emotion'][i]) + '\n'
        print(txt)
        self.emotion_result['text'] = txt


nlp = NLPApp()