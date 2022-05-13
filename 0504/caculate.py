import tkinter as tk


class Calc(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.pack()
        self.startOfNextOperand = True
        self.expr = tk.StringVar()
        self.expr.set('')
        self.exprLabel = tk.Label(self, font=('Helvetica', 10), fg='#828282', width=32, anchor='e',
                                  textvariable=self.expr)
        self.exprLabel.grid(row=0, column=0, columnspan=4)
        self.result = tk.StringVar()
        self.result.set('0')
        self.resultLabel = tk.Label(self, font=('Helvetica', 20), width=16, anchor='e',
                                    textvariable=self.result)
        self.resultLabel.grid(row=1, column=0, columnspan=4)

        buttons = [['CE', 'C', '←', '/'],
                   ['7', '8', '9', '*'],
                   ['4', '5', '6', '-'],
                   ['1', '2', '3', '+'],
                   ['±', '0', '.', '=']]

        for r in range(5):
            for c in range(4):
                def cmd(key=buttons[r][c]):
                    self.click(key)

                b = tk.Button(self, text=buttons[r][c], width=8, command=cmd)
                b.grid(row=r + 2, column=c)

    def click(self, key):
        if key == '=':
            resultExpr = self.expr.get() + self.result.get()
            resultNum = eval(resultExpr)
            self.result.set(resultNum)
            self.expr.set('')
            self.startOfNextOperand = True
        elif key in '+-*/':
            resultExpr = self.expr.get() + self.result.get() + key
            self.expr.set(resultExpr)
            self.startOfNextOperand = True
        elif key == 'C':
            self.expr.set('')
            self.result.set('0')
        elif key == 'CE':
            self.result.set('0')
        elif key == '←':
            oldnum = self.result.get()
            if len(oldnum) == 1:
                newnum = 0
            else:
                newnum = oldnum[:-1]
            self.result.set(newnum)
        elif key == '±':
            oldnum = self.result.get()
            if oldnum[0] == '-':
                newnum = oldnum[1:]
            else:
                newnum = '-' + oldnum
            self.result.set(newnum)
        else:
            if self.startOfNextOperand:
                self.result.set('0')
                self.startOfNextOperand = False
            oldnum = self.result.get()
            if oldnum == '0':
                self.result.set(key)
            else:
                newnum = oldnum + key
                self.result.set(newnum)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('简易计算器')
    calc = Calc(root)
    root.mainloop()
