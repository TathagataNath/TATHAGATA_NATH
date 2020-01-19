from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from PIL import ImageTk, Image

class GUI:

    def __init__(self, other):

        self._other = other
        self._isSecondRoot=False
        self._frameList=[]
        self.createRoot()

    def createRoot(self):


        if not self._isSecondRoot:

            self._root = Tk()
            self._root.title("TINDER APP")
            self._root.configure(background="#bdb76b")
            self._root.resizable(width=False, height=False)
            image = PhotoImage(file="appIcon.png")
            self._root.iconphoto(False,image)
            self._root.protocol("WM_DELETE_WINDOW",self._other.quitHandler)

        else:
            self._root1 = Toplevel()

            '''PhotoImage can not work with two or more instances of Tk simultaneously hence Toplevel is used in the
            second root '''

            self._root1.configure(background="#bdb76b")
            self._root1.resizable(width=False, height=False)
            image = PhotoImage(file=r"F:\appIcon.png")
            self._root1.iconphoto(False,image)
            self._root1.protocol("WM_DELETE_WINDOW",self._other.quitHandler)


    def displayMessage(self, title, message):

        messagebox.showinfo(title, message)

    def displayYesNo(self, title, message):

        return messagebox.askyesno(title,message)

    def setUpFrame(self,root):

        self._frame1 = Frame(root, bg="#bdb76b")
        self._frame1.grid(row=0, column=0)

        self._frame2 = Frame(root, bg="#bdb76b")
        self._frame2.grid(row=2, column=0)

        self._frame3 = Frame(root, bg="#bdb76b")
        self._frame3.grid(row=2, column=30)

        self._frame4 = Frame(root, bg="#bdb76b")
        self._frame4.grid(row=10, column=0)

    def viewProfile(self, data,message, mode=""):

        self.destroyRoot(mode)

        self.clearGrid(self._root)
        self._root.minsize(900, 700)

        self.setUpFrame(self._root)

        self.createMenu()

        headinglabel=Label(self._frame1,text=message,bg="#bdb76b",fg="#000")
        headinglabel.configure(font=("Times New Roman",30,"bold"))
        headinglabel.grid(row=0,column=10,columnspan=25,sticky=W,padx=(10,10),pady=(10,10))

        nameLabel = Label(self._frame2, text="NAME", bg="#bdb76b", fg="#000")
        nameLabel.configure(font=("Times New Roman", 18, "bold"))
        nameLabel.grid(row=2, column=0, columnspan=5, sticky=W, padx=10, pady=(10, 5))

        nameValue = Label(self._frame2, text=data[1], bg="#bdb76b", fg="#000",anchor=W)
        nameValue.configure(font=("Times New Roman", 18, "italic"))
        nameValue.grid(row=2, column=11, columnspan=5, sticky=W, ipadx=20, ipady=7, pady=(10, 5))

        emailLabel = Label(self._frame2, text="EMAIL", bg="#bdb76b", fg="#000")
        emailLabel.configure(font=("Times New Roman", 18, "bold"))
        emailLabel.grid(row=3, column=0, columnspan=5, sticky=W, padx=10, pady=(10, 5))

        emailValue = Label(self._frame2, text=data[2], bg="#bdb76b", fg="#000",anchor=W)
        emailValue.configure(font=("Times New Roman", 18, "italic"))
        emailValue.grid(row=3, column=11, columnspan=5, sticky=W, ipadx=20, ipady=7, pady=(10, 5))

        ageLabel = Label(self._frame2, text="AGE", bg="#bdb76b", fg="#000")
        ageLabel.configure(font=("Times New Roman", 18, "bold"))
        ageLabel.grid(row=4, column=0, columnspan=5, sticky=W, padx=10, pady=(10, 5))

        ageValue = Label(self._frame2, text=data[4], bg="#bdb76b", fg="#000",anchor=W)
        ageValue.configure(font=("Times New Roman", 18, "italic"))
        ageValue.grid(row=4, column=11, columnspan=5, sticky=W, ipadx=20, ipady=7, pady=(10, 5))

        self.viewImage(data[6])

        genderLabel = Label(self._frame2, text="GENDER", bg="#bdb76b", fg="#000")
        genderLabel.configure(font=("Times New Roman", 18, "bold"))
        genderLabel.grid(row=5, column=0, columnspan=5, sticky=W, padx=10, pady=(10, 5))

        genderValue = Label(self._frame2, text=data[5], bg="#bdb76b", fg="#000",anchor=W)
        genderValue.configure(font=("Times New Roman", 18, "italic"))
        genderValue.grid(row=5, column=11, columnspan=5, sticky=W, ipadx=20, ipady=7, pady=(10, 5))

        cityLabel = Label(self._frame2, text="CITY", bg="#bdb76b", fg="#000")
        cityLabel.configure(font=("Times New Roman", 18, "bold"))
        cityLabel.grid(row=6, column=0, columnspan=5, sticky=W, ipadx=10, pady=(10, 5))

        cityValue = Label(self._frame2, text=data[7], bg="#bdb76b", fg="#000",anchor=W)
        cityValue.configure(font=("Times New Roman", 18, "italic"))
        cityValue.grid(row=6, column=11, columnspan=5, sticky=W, ipadx=20, ipady=7, pady=(10, 5))

        bioLabel = Label(self._frame2, text="DETAILS", bg="#bdb76b", fg="#000")
        bioLabel.configure(font=("Times New Roman", 18, "bold"))
        bioLabel.grid(row=7, column=0, columnspan=5, sticky=W, ipadx=10,pady=(10,5))

        bioValue = Label(self._frame2,text=data[8],bg="#bdb76b", fg="#000",justify=LEFT)
        bioValue.configure(font=("Times New Roman", 18,"italic"))
        bioValue.grid(row=7, column=11, columnspan=5, sticky=W, padx=(5,0),pady=(10,5))

    def clearGrid(self,root):

        for i in root.grid_slaves():
            i.destroy()

    def viewAllProfiles(self, collection, i,mode):

        self.clearGrid(self._root)

        self.destroyRoot(mode)

        self.viewProfile(collection[i], mode, mode)

        if mode == "ALL PROFILES" :
            previousButton = Button(self._frame4, text="PREVIOUS", bg="#008000", fg="#fff",
                                command=lambda: self._other.viewHandler(mode="PREVIOUS",other="other"))
        elif mode == "MY PROPOSALS" :
            previousButton = Button(self._frame4, text="PREVIOUS", bg="#008000", fg="#fff",
                                    command=lambda: self._other.proposalHandler(mode="PREVIOUS"))
        elif mode == "MY REQUESTS" :
            previousButton = Button(self._frame4, text="PREVIOUS", bg="#008000", fg="#fff",
                                    command=lambda: self._other.requestHandler(mode="PREVIOUS"))
        elif mode == "SEARCH RESULT" :
            previousButton = Button(self._frame4, text="PREVIOUS", bg="#008000", fg="#fff",
                                    command=lambda: self._other.searchHandler(self._nameEntry,mode="PREVIOUS"))
        else :
            previousButton = Button(self._frame4, text="PREVIOUS", bg="#008000", fg="#fff",
                                    command=lambda: self._other.matchesHandler(mode="PREVIOUS"))

        previousButton.configure(font=("Times New Roman", 10))
        previousButton.grid(row=10, column=5, padx=3, ipadx=3, columnspan=2,pady=(7,0))

        if mode in ["ALL PROFILES", "MY REQUESTS", "SEARCH RESULT"]:
            proposeButton = Button(self._frame4, text="PROPOSE", bg="#008000", fg="#fff",
                                   command=lambda: self._other.proposeHandler(collection[i]))
            proposeButton.configure(font=("Times New Roman", 10))
            proposeButton.grid(row=10, column=11, padx=3, ipadx=3, columnspan=2,pady=(7,0))

        if mode == "ALL PROFILES" :
            nextButton = Button(self._frame4, text="NEXT", bg="#008000", fg="#fff",
                            command=lambda: self._other.viewHandler(mode="NEXT",other="other"))
        elif mode == "MY PROPOSALS" :
            nextButton = Button(self._frame4, text="NEXT", bg="#008000", fg="#fff",
                                    command=lambda: self._other.proposalHandler(mode="NEXT"))
        elif mode == "MY REQUESTS" :
            nextButton = Button(self._frame4, text="NEXT", bg="#008000", fg="#fff",
                                command=lambda: self._other.requestHandler(mode="NEXT"))
        elif mode == "SEARCH RESULT" :
            nextButton = Button(self._frame4, text="NEXT", bg="#008000", fg="#fff",
                                command=lambda: self._other.searchHandler(self._nameEntry,mode="NEXT"))
        else :
            nextButton = Button(self._frame4, text="NEXT", bg="#008000", fg="#fff",
                                command=lambda: self._other.matchesHandler(mode="NEXT"))

        nextButton.configure(font=("Times New Roman", 10))
        nextButton.grid(row=10, column=15, padx=3, ipadx=3, columnspan=2,pady=(7,0))

    def firstPage(self):

        self.clearGrid(self._root)

        self.destroyRoot()

        self._root.minsize(500,400)
        emptyMenuBar = Menu(self._root)
        self._root.config(menu=emptyMenuBar)

        items=self.showWidgets(self._root)

        loginButton = Button(self._root, text="LOGIN", bg="#008000", fg="#fff",
                             command=lambda: self._other.loginHandler(items))
        loginButton.configure(font=("Times New Roman", 18, "bold"))
        loginButton.grid(row=10, column=4, columnspan=5, sticky=W, ipadx=20, pady=(10, 5))

        newUserLabel = Label(self._root, text="NEW USER ?", bg="#bdb76b", fg="#000")
        newUserLabel.configure(font=("Times New Roman", 14, "bold"))
        newUserLabel.grid(row=14, column=12, columnspan=5, padx=10, sticky=W, pady=(10, 5))

        registerButton = Button(self._root, text="REGISTER HERE", bg="#008000", fg="#fff",
                                command=lambda: self.registrationPage())
        registerButton.configure(font=("Times New Roman", 12, "bold"))
        registerButton.grid(row=15, column=12, columnspan=10, ipadx=10, pady=(10, 5))

        self._root.mainloop()

    def createMenu(self):

        menu = Menu(self._root)
        self._root.config(menu=menu)

        filemenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.configure(font=("Times New Roman", 10))
        filemenu.add_cascade(label="View My Profile", command=lambda: self._other.viewHandler())
        filemenu.add_command(label="Edit My Profile", command=lambda: self.editingPage(self._other.getUser()))
        filemenu.add_command(label="View Other Profiles", command=lambda: self._other.viewHandler(other="other"))
        filemenu.add_command(label="Search Other Profiles",command=lambda: self.searchPage())
        filemenu.add_command(label="LogOut", command=lambda: self._other.logOutHandler())
        filemenu.add_command(label="Delete My Profile",command=lambda : self._other.deleteHandler())


        helpmenu = Menu(menu, tearoff=0, font=("Times New Roman", 20, "bold"))
        menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.configure(font=("Times New Roman", 10))
        helpmenu.add_command(label="My Proposals", command=lambda: self._other.proposalHandler())
        helpmenu.add_command(label="My Requests", command=lambda: self._other.requestHandler())
        helpmenu.add_command(label="My Matches", command=lambda: self._other.matchesHandler())

    def chooseImage(self,root,l,flag=0):


        self._path=filedialog.askopenfilename(
            parent=root,
            title='Choose Image',
            filetypes=[      ('jpg images','.jpg'),
                             ('jpeg images','.jpeg'),
                             ('gif images (.gif)', '.gif'),
                             ('png images (.png)', '.png'),
                             ('tiff images (.tiff)','.tiff'),
                       ]
            )

        if self._path not in ["",tuple()]:

            self.viewImage(self._path)
            l[flag+4]=self._path

    def showWidgets(self, root,frame=False, flag=False, data=()):

        l=[]

        if not flag and data == () :
            headingLabel = Label(root, text="TINDER", bg="#bdb76b", fg="#000")
        elif flag:
            headingLabel = Label(self._frame1, text="NEW REGISTRATION", bg="#bdb76b", fg="#000")
        else:
            headingLabel = Label(self._frame1, text="EDIT PROFILE", bg="#bdb76b", fg="#000")

        headingLabel.configure(font=("Times New Roman", 30, "bold"))
        headingLabel.grid(row=0, column=10, columnspan=25,padx=(10, 0), pady=(10, 10))

        if flag or data != ():
            nameLabel = Label(self._frame2, text="NAME", bg="#bdb76b", fg="#000")
            nameLabel.configure(font=("Times New Roman", 18, "bold"))
            nameLabel.grid(row=1, column=0, columnspan=5, sticky=W, padx=10, pady=(10, 5))

            nameEntry = Entry(self._frame2)
            nameEntry.configure(font=("Times New Roman", 14))
            if not flag:
                nameEntry.insert(0, data[1])
            nameEntry.grid(row=1, column=11, columnspan=5, sticky=W, ipadx=20, ipady=7, pady=(10, 5))

            l.append(nameEntry)
        if frame:
            emailLabel = Label(self._frame2, text="EMAIL", bg="#bdb76b", fg="#000")
        else :
            emailLabel = Label(root, text="EMAIL", bg="#bdb76b", fg="#000")
        emailLabel.configure(font=("Times New Roman", 18, "bold"))
        if not flag and data == ():
            emailLabel.grid(row=1, column=0, columnspan=5, sticky=W, padx=10, pady=(10, 5))
        else:
            emailLabel.grid(row=2, column=0, columnspan=5, sticky=W, padx=10, pady=(10, 5))
        if frame:
            emailEntry = Entry(self._frame2)
        else:
            emailEntry = Entry(root)
        emailEntry.configure(font=("Times New Roman", 14))
        if not flag and data != ():
            emailEntry.insert(0, data[2])
        if not flag and data == ():
            emailEntry.grid(row=1, column=11, columnspan=5, sticky=W, ipadx=20, ipady=7, pady=(10, 5))
        else:
            emailEntry.grid(row=2, column=11, columnspan=5, sticky=W, ipadx=20, ipady=7, pady=(10, 5))
        l.append(emailEntry)
        if frame:
            passwordLabel = Label(self._frame2, text="PASSWORD", bg="#bdb76b", fg="#000")
        else:
            passwordLabel = Label(root, text="PASSWORD", bg="#bdb76b", fg="#000")
        passwordLabel.configure(font=("Times New Roman", 18, "bold"))
        if not flag and data == ():
            passwordLabel.grid(row=2, column=0, columnspan=5, sticky=W, padx=10, pady=(10, 5))
        else:
            passwordLabel.grid(row=3, column=0, columnspan=5, sticky=W, padx=10, pady=(10, 5))
        if frame:
            passwordEntry=Entry(self._frame2)
        else:
            passwordEntry = Entry(root)
        passwordEntry.configure(font=("Times New Roman", 14))
        if not flag and data != ():
            passwordEntry.insert(0, data[3])

        if not flag and data == ():
            passwordEntry.grid(row=2, column=11, columnspan=5, sticky=W, ipadx=20, ipady=7, pady=(10, 5))
        else:
            passwordEntry.grid(row=3, column=11, columnspan=5, sticky=W, ipadx=20, ipady=7, pady=(10, 5))

        l.append(passwordEntry)

        if flag or data != ():
            ageLabel = Label(self._frame2, text="AGE", bg="#bdb76b", fg="#000")
            ageLabel.configure(font=("Times New Roman", 18, "bold"))
            ageLabel.grid(row=4, column=0, columnspan=5, sticky=W, padx=10, pady=(10, 5))

            ageEntry = Entry(self._frame2)
            ageEntry.configure(font=("Times New Roman", 14))
            if not flag:
                ageEntry.insert(0, data[4])
            ageEntry.grid(row=4, column=11, columnspan=5, sticky=W, ipadx=20, ipady=7, pady=(10, 5))

            l.append(ageEntry)

            if flag:
                genderLabel = Label(self._frame2, text="GENDER", bg="#bdb76b", fg="#000")
                genderLabel.configure(font=("Times New Roman", 18, "bold"))
                genderLabel.grid(row=5, column=0, columnspan=5, sticky=W, padx=10, pady=(10, 5))

                var = StringVar(self._frame2)
                var.set("Choose")
                genderOptionMenu = OptionMenu(self._frame2, var, "Male", "Female", "Other")
                genderOptionMenu.configure(font=("Times New Roman", 14))
                genderOptionMenu.grid(row=5, column=11, columnspan=5, sticky=W, padx=10, pady=(10, 5))

                l.append(var)

            imageLabel = Label(self._frame2, text="IMAGE", bg="#bdb76b", fg="#000")
            imageLabel.configure(font=("Times New Roman", 18, "bold"), justify=LEFT)
            imageLabel.grid(row=6, column=0, columnspan=5, sticky=W, padx=10, pady=(10, 5))

            if flag :
                imageChoose=Button(self._frame2, text="CHOOSE IMAGE", bg="#008000", fg="#fff",
                   command=lambda: self.chooseImage(root,l,1))
            else :
                imageChoose = Button(self._frame2, text="CHOOSE IMAGE", bg="#008000", fg="#fff",
                                     command=lambda: self.chooseImage(root, l))
            imageChoose.configure(font=("Times New Roman",14,"bold"))
            imageChoose.grid(row=6, column=11, columnspan=2, padx=5, ipadx=10, pady=(10, 5))

            if data == () :
                l.append("")
            else :
                l.append(data[6])

            if not flag and data !=() :
                self.viewImage(data[6])

            cityLabel = Label(self._frame2, text="CITY", bg="#bdb76b", fg="#000")
            cityLabel.configure(font=("Times New Roman", 18, "bold"))
            cityLabel.grid(row=8, column=0, columnspan=5, sticky=W, padx=10, pady=(10, 5))

            cityEntry = Entry(self._frame2)
            cityEntry.configure(font=("Times New Roman", 14))
            if not flag:
                cityEntry.insert(0, data[7])
            cityEntry.grid(row=8, column=11, columnspan=5, sticky=W, ipadx=20, ipady=7, pady=(10, 5))

            l.append(cityEntry)

            bioLabel = Label(self._frame2, text="ABOUT", bg="#bdb76b", fg="#000")
            bioLabel.configure(font=("Times New Roman", 18, "bold"))
            bioLabel.grid(row=9, column=0, columnspan=5, sticky=W, padx=10, pady=(10, 0))

            bioEntry = Text(self._frame2, height=8, width=24,wrap=WORD)
            bioEntry.configure(font=("Times New Roman", 14))
            if not flag:
                bioEntry.insert(END, data[8])
            bioEntry.grid(row=9, column=11, columnspan=5, sticky=W, padx=2, pady=(10, 0))

            l.append(bioEntry)

        return l

    def registrationPage(self):

        self._isSecondRoot=True
        self.createRoot()
        self.setUpFrame(self._root1)
        items = self.showWidgets(self._root1,frame=True,flag=True)
        self._root1.minsize(850, 725)
        self._root1.title("NEW REGISTRATION")

        registrationButton = Button(self._frame4, text="REGISTER", bg="#008000", fg="#fff",
                                    command=lambda: self._other.regHandler(items))
        registrationButton.configure(font=("Times New Roman", 18, "bold"))
        registrationButton.grid(row=16, column=10, columnspan=5, sticky=W, ipadx=20, pady=(30, 0))

    def destroyRoot(self,mode="",command=""):

        if self._isSecondRoot  and ( mode != "SEARCH RESULT" or command == "CLOSE" ):
            self._root1.destroy()
            self._isSecondRoot=False
        elif command == "CLOSE":
            self._root.destroy()

    def editingPage(self, data):

        self.destroyRoot()

        self.clearGrid(self._root)

        self.setUpFrame(self._root)

        self._root.minsize(800, 700)

        items = self.showWidgets(self._root,frame=True, data=data)

        updateButton = Button(self._frame4, text="UPDATE", bg="#008000", fg="#fff",
                              command=lambda: self._other.updateHandler(items))
        updateButton.configure(font=("Times New Roman", 18, "bold"))
        updateButton.grid(row=16, column=10, columnspan=5, sticky=W, ipadx=20, pady=(30, 0))

    def searchPage(self) :

        self._isSecondRoot=True
        self.createRoot()

        self._root1.minsize(500, 200)
        self._root1.title("SEARCH PROFILE")

        headingLabel = Label(self._root1, text="SEARCH PROFILE", bg="#bdb76b", fg="#000")
        headingLabel.configure(font=("Times New Roman", 18, "bold","underline"))
        headingLabel.grid(row=0, column=5, columnspan=5, pady=(10, 10))

        nameLabel = Label(self._root1, text="Enter Name", bg="#bdb76b", fg="#000")
        nameLabel.configure(font=("Times New Roman", 18, "bold"))
        nameLabel.grid(row=1, column=0, columnspan=5, sticky=W, padx=10, pady=(10, 10))

        self._nameEntry=Entry(self._root1)
        self._nameEntry.configure(font=("Times New Roman", 14))
        self._nameEntry.grid(row=1, column=6, columnspan=5, sticky=W, ipady=7, ipadx=10, pady=(10, 10))


        nameButton = Button(self._root1, text="SEARCH", bg="#bdb76b", fg="#000",
                               command=lambda: self.test())
        nameButton.configure(font=("Times New Roman", 14,"bold"))
        nameButton.grid(row=4, column=5, padx=3, ipadx=3, columnspan=2, pady=(10, 0))

    def test(self):
        self._other.resetSearchIndex()
        self._other.searchHandler(self._nameEntry,"")

    def viewImage(self,path) :
        load = Image.open(path)
        load = load.resize((300, 400), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        imageViewLabel = Label(self._frame3, image=render)
        imageViewLabel.image = render
        imageViewLabel.grid(row=7, column=25, columnspan=5,padx=(40,0), pady=(10, 5))
