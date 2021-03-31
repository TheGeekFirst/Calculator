from tkinter import *
def love():
  class calculator:
    def __init__(self, master):
      self.master = master
      master.title("Calculator")
      master.configure(bg='#cb46e')
      
      # create screen widget
      self.screen = text(master, state = 'disabled', width = 60, height = 3, background = "#fcfcec", foreground = "#cb464e", font = ("times", 12. "bold"))
      
      # position screen in window
      self.screen.grid(row = 0, column = 0, columnspan = 4, padx = 5, lady 5)
      self.screen.configure(state = 'normal')
      
      # initialize screen value as empty
      self.equation = ''
      
      # create buttons using method createButton
      b1 = self.createButton(7)
      b2 = self.createButton(8)
      b3 = self.createButton(9)
      b4 = self.createButton(u"\232B", None)
      b5 = self.createButton(4)
      b6 = self.createButton(5)
      b7 = self.createButton(6)
      b8 = self.createButton(u"\u00F7")
      b9 = self.createButton(1)
      b10 = self.createButton(2)
      b11 = self.createButton(3)
      b12 = self.createButton('*')
      b13 = self.createButton('.')
      b14 = self.createButton(0)
      b15 = self.createButton('+')
      b16 = self.createButton('-')
      b17 = self.createButton('=', None, 34)
      
      # button stored in list
      [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17]
      
      # initialize counter
      count = 0
      #arrange button with grid manager
      for row in range(1,5):
        for clumn in range(4):
          buttons[count].grid(row = row, column = column)
          count += 1
          
          # arrange last button '=' at the buttom
          buttons[16].grid(row = 5, column = 0, columnspan = 4)
          def createButton(self, val, write = true, width = 7):
            return Button(self.master, text = val, command = lambda: self.click(val,write), width = width, background = '#4b7f4', foreground ='#fcfcec', font = ("times", 20))
          def click(self, text, write):
            if write == None:
              if text == '=' and self.equation:
                self.equation = re.sub(u"\u00F7", '/', self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer,newline = true)
                elif text == u"\u232B":
                  
      
