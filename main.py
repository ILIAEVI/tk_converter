import tkinter as tk
from tkinter import ttk

class MoneyConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Money Converter")
        self.master.geometry("500x500")
        self.master.resizable(False, False)

        self.currency_rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GEL': 3.0
        }

        self.title_frame = tk.Frame(self.master, bg='#4CAF50')
        self.title_frame.pack(fill=tk.X)

        self.title_label = tk.Label(self.title_frame, text="Money Converter", font=('Helvetica', 16, 'bold'), pady=10,
                                    bg='#4CAF50', fg='white')
        self.title_label.pack()

        self.main_frame = tk.Frame(self.master, padx=20, pady=10)
        self.main_frame.pack(fill=tk.BOTH)

        self.label1 = tk.Label(self.main_frame, text="From:")
        self.label1.pack(pady=10)

        self.source_currency = ttk.Combobox(self.main_frame, values=list(self.currency_rates.keys()))
        self.source_currency.pack()
        self.source_currency.current(0)
        self.source_currency.bind("<<ComboboxSelected>>", self.target_currency_filter)

        self.label2 = tk.Label(self.main_frame, text="To:")
        self.label2.pack(pady=10)

        self.target_currency = ttk.Combobox(self.main_frame)
        self.target_currency.pack()
        self.target_currency_filter()

        self.label3 = tk.Label(self.main_frame, text="Amount")
        self.label3.pack(pady=10)

        self.amount_entry = ttk.Entry(self.main_frame, width=20)
        self.amount_entry.pack()

        self.convert_button = tk.Button(self.main_frame, text="Convert", bg="#4CAF50",
                                        fg="white", command=self.convert_currency)
        self.convert_button.pack(pady=20)

        self.clear_button = tk.Button(self.main_frame, text="Clear", bg="#f44336", fg="white",
                                      command=self.clear_inputs)
        self.clear_button.pack()

        self.result_label = tk.Label(self.main_frame, text="", pady=20)
        self.result_label.pack()

    def target_currency_filter(self, *args):
        from_currency = self.source_currency.get()
        target_currency = [currency for currency in self.currency_rates if currency != from_currency]
        self.target_currency['values'] = target_currency
        if target_currency:
            self.target_currency.current(0)

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.source_currency.get()
            to_currency = self.target_currency.get()
            conversion_rate = self.currency_rates[to_currency] / self.currency_rates[from_currency]
            converted_amount = round(amount * conversion_rate, 2)
            self.result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
        except ValueError:
            self.result_label.config(text="Invalid input! Please enter a valid amount.")


    def clear_inputs(self):
        self.source_currency.current(0)
        self.target_currency_filter()
        self.amount_entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = MoneyConverterApp(root)
    root.mainloop()
