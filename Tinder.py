from GUIHelper import GUI, END
from DBHelper import DBHelper


class Tinder(GUI):

    def __init__(self):
        self._viewIndex = 0
        self._proposalIndex=0
        self._requestIndex=0
        self._searchIndex=0
        self._matchesIndex=0
        self._user = None
        self._dbObject = DBHelper()
        if self._dbObject.checkConnection() :
            super().__init__(self)
            self.firstPage()

    def verifier(self, values, flag=0, edit="",search=False):
        if flag or edit != "" or search :
            if len(values[0].get()) == 0:
                self.displayMessage("INPUT ERROR", "PLEASE ENTER A VALID NAME")
                return False
        if not search :
            if not flag and edit=="":
                if len(values[0].get()) == 0 or '@' not in values[0].get() or '.com' != values[0].get()[-4:]:
                    self.displayMessage("INPUT ERROR", "PLEASE ENTER A VALID EMAIL")
                    return False
            else:
                if len(values[1].get()) == 0 or '@' not in values[1].get() or '.com' != values[1].get()[-4:]:
                    self.displayMessage("INPUT ERROR", "PLEASE ENTER A VALID EMAIL")
                    return False
            if (flag and edit == "" and len(self._dbObject.searchItem('email','users','email',values[1].get())) != 0) or (
                    not flag and edit != "" and self._dbObject.searchItem('email','users','email',values[1].get())[0][0] != self._user[2] and len(
                self._dbObject.searchItem('email','users','email',values[1].get())) != 0):
                self.displayMessage("INPUT ERROR", "EMAIL ID ALREADY REGISTERED")
                return False
            if flag or edit != "":
                if len(values[2].get()) == 0:
                    self.displayMessage("INPUT ERROR", "PLEASE ENTER A VALID PASSWORD")
                    return False
            else:
                if len(values[1].get()) == 0:
                    self.displayMessage("INPUT ERROR", "PLEASE ENTER A VALID PASSWORD")
                    return False

            if flag or edit != "":
                if len(values[3].get()) == 0 or not values[3].get().isdigit():
                    self.displayMessage("INPUT ERROR", "PLEASE ENTER A VALID AGE ( ONLY INTEGER NUMBER )")
                    return False
            if flag and edit == "":
                if values[4].get() == "Choose":
                    self.displayMessage("INPUT ERROR", "PLEASE ENTER A VALID GENDER")
                    return False
            if flag or edit != "":
                if values[flag+4]=="" and edit=="" :
                    self.displayMessage("INPUT ERROR","PLEASE CHOOSE AM IMAGE")
                    return False
                if len(values[flag + 5].get()) == 0:
                    self.displayMessage("INPUT ERROR", "PLEASE ENTER A VALID CITY")
                    return False
                if values[flag + 6].compare("end-1c", "==", "1.0"):
                    self.displayMessage("INPUT ERROR", "PLEASE GIVE YOUR DETAILS")
                    return False
        return True

    def loginHandler(self,l):

        if self.verifier(l):
            response = self._dbObject.search("users", "email", l[0].get(), "password", l[1].get())
            if len(response) == 0:
                self.displayMessage("INPUT ERROR", "USER NOT FOUND")
            else:
                self._user = response[0]
                self.viewProfile(self._user,"MY PROFILE")

    def regHandler(self, args):

        if self.verifier(args, 1):

            regDict = {
                'name': args[0].get().capitalize(),
                'email': args[1].get().lower(),
                'password': args[2].get(),
                'age': args[3].get(),
                'gender': args[4].get(),
                'bg': args[5],
                'city': args[6].get().capitalize(),
                'bio': args[7].get("1.0", END).strip()
            }

            flag = self._dbObject.insert("users", regDict)

            if flag:
                self.displayMessage("REGISTRATION", "REGISTRATION SUCCESSFUL\nPLEASE LOGIN TO CONTINUE")
                self.destroyRoot()
            else:
                self.displayMessage("REGISTRATION", "REGISTRATION FAILED")

    def viewHandler(self, mode="",other=""):

        response = self._dbObject.getAll("users", self._user[0])

        if mode == "PREVIOUS":
            self._viewIndex = (self._viewIndex + (len(response) - 1)) % len(response)
        elif mode == "NEXT":
            self._viewIndex = (self._viewIndex + 1) % len(response)

        if other == "" :
            self.viewProfile(self._user,"MY PROFILE",False)

        elif other != "" :
            self.viewAllProfiles(response, self._viewIndex,"ALL PROFILES")

    def updateHandler(self, args):

        if self.verifier(args, edit="edit"):

            updateDict = {
                'name': args[0].get().capitalize(),
                'email': args[1].get().lower(),
                'password': args[2].get(),
                'age': args[3].get(),
                'bg': args[4],
                'city': args[5].get().capitalize(),
                'bio': args[6].get("1.0", END).strip(),
            }

            flag = self._dbObject.update("users", self._user[0], updateDict)

            if flag:
                response = self._dbObject.search("users", "email", updateDict['email'], "password", updateDict['password'])
                self._user = response[0]
                self.displayMessage("UPDATE", "UPDATE SUCCESSFUL")
            else:
                self.displayMessage("UPDATE", "UPDATE FAILED")

    def proposeHandler(self, data):

        response = self._dbObject.search("proposals", "romeo_id", self._user[0], "juliet_id", data[0])

        if len(response) != 0:
            self.displayMessage("PROPOSAL", "PROPOSAL ALREADY MADE")
        else:

            proposalDict = {
                "romeo_id": self._user[0],
                "juliet_id": data[0]
            }

            flag = self._dbObject.insert("proposals", proposalDict)

            if flag:
                self.displayMessage("PROPOSAL", "PROPOSAL SENT")
            else:
                self.displayMessage("PROPOSAL", "PROPOSAL NOT SENT")

    def deleteHandler(self):

        if self.displayYesNo("DELETE PROFILE","DO YOU REALLY WANT TO DELETE YOUR PROFILE ?"):
            flag=self._dbObject.delete("users","user_id",self._user[0])
            if flag :
                self._dbObject.delete("proposals","romeo_id",self._user[0])
                self._dbObject.delete("proposals","juliet_id",self._user[0])
                self.displayMessage("DELETE PROFILE","PROFILE DELETED")
                self.firstPage()
            else :
                self.displayMessage("DELETE PROFILE","PROFILE NOT DELETED")

    def proposalHandler(self,mode=""):

        records=self._dbObject.findProposalsOrRequests('juliet_id','romeo_id',self._user[0])

        if records != [] :

            if mode == "PREVIOUS":
                    self._proposalIndex = (self._proposalIndex + (len(records) - 1)) % len(records)
            elif mode == "NEXT":
                self._proposalIndex = (self._proposalIndex + 1) % len(records)

            self.viewAllProfiles(records,self._proposalIndex,"MY PROPOSALS")

        else :
            self.displayMessage("MY PROPOSALS","NO PROPOSALS FOUND")

    def requestHandler(self,mode=""):

        records=self._dbObject.findProposalsOrRequests('romeo_id','juliet_id',self._user[0])

        if records != [] :

            if mode == "PREVIOUS":
                self._requestIndex = (self._requestIndex + (len(records) - 1)) % len(records)
            elif mode == "NEXT":
                self._requestIndex = (self._requestIndex + 1) % len(records)

            self.viewAllProfiles(records, self._requestIndex, "MY REQUESTS")

        else :
            self.displayMessage("MY REQUESTS","NO REQUESTS FOUND")

    def matchesHandler(self,mode=""):

            records=self._dbObject.findMatches(self._user[0])

            if records != [] :

                 if mode == "PREVIOUS":
                     self._matchesIndex = (self._matchesIndex + (len(records) - 1)) % len(records)
                 elif mode == "NEXT":
                     self._matchesIndex = (self._matchesIndex + 1) % len(records)

                 self.viewAllProfiles(records,self._matchesIndex,"MY MATCHES")

            else :
                self.displayMessage("MY MATCHES","NO MATCHES FOUND")


    def searchHandler(self,nameEntry,mode) :

        if self.verifier([nameEntry],search=True) :

            response=self._dbObject.searchItem('*','users','name','%'+nameEntry.get()+'%','user_id',self._user[0])

            if response == [] :
                self.displayMessage("SEARCH","NO RECORD FOUND")

            else :
                if mode == "PREVIOUS" :
                    self._searchIndex = (self._searchIndex + (len(response) - 1)) % len(response)
                elif mode == "NEXT" :
                    self._searchIndex = (self._searchIndex + 1) % len(response)

                self.viewAllProfiles(response,self._searchIndex,"SEARCH RESULT")

    def logOutHandler(self):

        if self.displayYesNo("LOGOUT","DO YOU REALLY WANT TO LOGOUT ?"):
            self.firstPage()

    def quitHandler(self):

        if self.displayYesNo("QUIT","DO YOU REALLY WANT TO QUIT ?"):
            self.destroyRoot(command="CLOSE")

    def getUser(self):
        return self._user

    def resetSearchIndex(self):
        self._searchIndex=0

x = Tinder()