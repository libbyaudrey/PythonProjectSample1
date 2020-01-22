#Libby Snedaker
#11/24/2019
#Program Name: Snedaker_JoeAutomotive.py
#Purpose: Create a GUI that uses checkboxes to display totals
import tkinter

class JoeAutomotiveGUI:
     def __init__(self):
          
          # create the main window
          self.main_window = tkinter.Tk()
          self.main_window.geometry('400x200')
          self.main_window.title("Joe's Automotive")

          # create the frames
          self.frame1 = tkinter.Frame(self.main_window)
          self.frame2 = tkinter.Frame(self.main_window)
          self.frame3 = tkinter.Frame(self.main_window)
          self.frame4 = tkinter.Frame(self.main_window)
          self.frame5 = tkinter.Frame(self.main_window)
          self.frame6 = tkinter.Frame(self.main_window)
          self.frame7 = tkinter.Frame(self.main_window)
          self.frame8 = tkinter.Frame(self.main_window)
          self.frame9 = tkinter.Frame(self.main_window)

          # create IntVar objects
          self.oilChangeVar = tkinter.IntVar()
          self.lubeJobVar = tkinter.IntVar()
          self.radiatorFlushVar = tkinter.IntVar()
          self.transmissionFlushVar = tkinter.IntVar()
          self.inspectionVar = tkinter.IntVar()
          self.mufflerReplacementVar = tkinter.IntVar()
          self.tireRotationVar = tkinter.IntVar()

          # set intVar objects to 0
          self.oilChangeVar.set(0)
          self.lubeJobVar.set(0)
          self.radiatorFlushVar.set(0)
          self.transmissionFlushVar.set(0)
          self.inspectionVar.set(0)
          self.mufflerReplacementVar.set(0)
          self.tireRotationVar.set(0)
    
          # create the checkbutton widgets for each frame
          self.oilChangeCB = tkinter.Checkbutton(self.frame1, text = 'Oil Change - $30 ', variable = self.oilChangeVar, onvalue = 30)
          self.lubeJobCB = tkinter.Checkbutton(self.frame2, text = 'Lube Job - $20 ', variable = self.lubeJobVar, onvalue = 20)
          self.radiatorFlushCB = tkinter.Checkbutton(self.frame3, text = 'Radiator Flush - $40 ', variable = self.radiatorFlushVar, onvalue = 40)
          self.transmissionFlushCB = tkinter.Checkbutton(self.frame4, text = 'Transmission Flush - $100 ', variable = self.transmissionFlushVar, onvalue = 100)
          self.inspectionCB = tkinter.Checkbutton(self.frame5, text = 'Inspection - $35 ', variable = self.inspectionVar, onvalue = 35)
          self.mufflerReplacementCB = tkinter.Checkbutton(self.frame6, text = 'Muffler Replacement - $200 ', variable = self.mufflerReplacementVar, onvalue = 200)
          self.tireRotationCB = tkinter.Checkbutton(self.frame7, text = 'Tire Rotation - $20', variable = self.tireRotationVar, onvalue = 20)

          # pack the checkbuttons
          self.oilChangeCB.pack()
          self.lubeJobCB.pack()
          self.radiatorFlushCB.pack()
          self.transmissionFlushCB.pack()
          self.inspectionCB.pack()
          self.mufflerReplacementCB.pack()
          self.tireRotationCB.pack()

          # create button to total up the charges selected
          self.totalChargesButton = tkinter.Button(self.frame8, text = 'Total Charges', command = self.totalCharges)

          # create label to display total costs
          self.totalOutput = tkinter.Label(self.frame9, text ="$0.00")

          # pack the buttons
          self.totalChargesButton.pack(side = 'left')
          self.totalOutput.pack(side = 'left')

          # pack the frames
          self.frame1.pack()
          self.frame2.pack()
          self.frame3.pack()
          self.frame4.pack()
          self.frame5.pack()
          self.frame6.pack()
          self.frame7.pack()
          self.frame8.pack()
          self.frame9.pack()

          tkinter.mainloop()

     # method to display the value of the services
     def totalCharges(self):
           self.totalOutput.config(text="${}.00".format(sum(map(tkinter.IntVar.get,
                                                         [self.oilChangeVar, self.lubeJobVar, self.radiatorFlushVar,
                                                          self.transmissionFlushVar, self.inspectionVar, self.mufflerReplacementVar,self.tireRotationVar]))))

# this calls the __init__/main method
if __name__ == "__main__":

     # creates a class object
     myGUI = JoeAutomotiveGUI()
        

