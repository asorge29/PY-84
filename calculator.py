import tkinter as tk

class calculator(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.num1 = 0
        self.num2 = 0
        self.solution = 0
        self.operation = ''
        self.operation_set = False
        self.number_entry = tk.Entry(self, font=(None, 25))
        self.number_entry.config(state='readonly')
        self.number_entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        self.button_7 = tk.Button(self, text='7', command=lambda:self._insert_number(7), height=3, width=6)
        self.button_7.grid(row=1, column=0, sticky='nsew')

        self.button_8 = tk.Button(self, text='8', command=lambda:self._insert_number(8), height=3, width=6)
        self.button_8.grid(row=1, column=1, sticky='nsew')

        self.button_9 = tk.Button(self, text='9', command=lambda:self._insert_number(9), height=3, width=6)
        self.button_9.grid(row=1, column=2, sticky='nsew')

        self.button_plus = tk.Button(self, text='+', command=lambda:self._set_operation('+'), height=3, width=6)
        self.button_plus.grid(row=1, column=3, sticky='nsew')

        self.button_4 = tk.Button(self, text='4', command=lambda:self._insert_number(4), height=3, width=6)
        self.button_4.grid(row=2, column=0, sticky='nsew')
        
        self.button_5 = tk.Button(self, text='5', command=lambda:self._insert_number(5), height=3, width=6)
        self.button_5.grid(row=2, column=1, sticky='nsew')

        self.button_6 = tk.Button(self, text='6', command=lambda:self._insert_number(6), height=3, width=6)
        self.button_6.grid(row=2, column=2, sticky='nsew')

        self.button_minus = tk.Button(self, text='-', command=lambda:self._set_operation('-'), height=3, width=6)
        self.button_minus.grid(row=2, column=3, sticky='nsew')

        self.button_1 = tk.Button(self, text='1', command=lambda:self._insert_number(1), height=3, width=6)
        self.button_1.grid(row=3, column=0, sticky='nsew')

        self.button_2 = tk.Button(self, text='2', command=lambda:self._insert_number(2), height=3, width=6)
        self.button_2.grid(row=3, column=1, sticky='nsew')

        self.button_3 = tk.Button(self, text='3', command=lambda:self._insert_number(3), height=3, width=6)
        self.button_3.grid(row=3, column=2, sticky='nsew')

        self.button_multiply = tk.Button(self, text='*', command=lambda:self._set_operation('*'), height=3, width=6)
        self.button_multiply.grid(row=3, column=3, sticky='nsew')

        self.button_0 = tk.Button(self, text='0', command=lambda:self._insert_number(0), height=3, width=6)
        self.button_0.grid(row=4, column=0, sticky='nsew')

        self.button_decimal = tk.Button(self, text='.', command=lambda:self._insert_number('.'), height=3, width=6)
        self.button_decimal.grid(row=4, column=1, sticky='nsew')

        self.button_clear = tk.Button(self, text='CE', height=3, width=6, command=self._clear)
        self.button_clear.grid(row=4, column=2, sticky='nsew')

        self.button_divide = tk.Button(self, text='/', command=lambda:self._set_operation('/'), height=3, width=6)
        self.button_divide.grid(row=4, column=3, sticky='nsew')

        self.button_equal = tk.Button(self, text='=', command=self._calculate, height=3)
        self.button_equal.config(state='disabled')
        self.button_equal.grid(row=5, column=0, columnspan=4, sticky='nsew')

    def _insert_number(self, number):
        self.number_entry.config(state='normal')
        self.number_entry.insert(tk.END, str(number))
        self.number_entry.config(state='readonly')

    def _set_operation(self, operation):
        self.operation = operation
        self.num1 = self.number_entry.get()
        self.number_entry.config(state='normal')
        self.number_entry.delete(0, 'end')
        self.number_entry.config(state='readonly')
        self.operation_set = True
        self._disable_ops()

    def _disable_ops(self):
        self.button_multiply.config(state='disabled')
        self.button_plus.config(state='disabled')
        self.button_minus.config(state='disabled')
        self.button_divide.config(state='disabled')
        self.button_equal.config(state='normal')

    def _enable_ops(self):
        self.button_multiply.config(state='normal')
        self.button_plus.config(state='normal')
        self.button_minus.config(state='normal')
        self.button_divide.config(state='normal')
        self.button_equal.config(state='disabled')

    def _calculate(self):
        self.num2 = self.number_entry.get()
        exec(f'self.solution = {self.num1} {self.operation} {self.num2}')
        self.number_entry.config(state='normal')
        self.number_entry.delete(0, 'end')
        self._insert_number(self.solution)
        self.num1 = self.solution
        self._enable_ops()

    def _clear(self):
        self.number_entry.config(state='normal')
        self.number_entry.delete(0, 'end')
        self.number_entry.config(state='readonly')
        self.num1 = 0
        self.operation = ''
        self.num2 = 0
        self.solution = 0
        

if __name__ == '__main__':
    root = tk.Tk()
    calculator_gui = calculator(root)
    calculator_gui.pack()
    root.resizable(False, False)
    root.mainloop()