# Creates a tkinter GUI form with multiple input types (text, spinbox, dropdown, checkbox, slider)  
# Collects user data and saves to Excel file using pandas  
# Validates required fields and email format before saving  
# Appends new entries to existing data.xlsx file or creates new file  
# Clears form after successful submission with confirmation message  

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

class DataEntryForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Entry Form")
        self.root.geometry("500x600")
        
        # Create variables to store data
        self.data = {
            "Name": tk.StringVar(),
            "Age": tk.IntVar(value=18),
            "Gender": tk.StringVar(),
            "Email": tk.StringVar(),
            "Subscription": tk.IntVar(),
            "Satisfaction": tk.IntVar(value=50),
            "Comments": tk.StringVar()
        }
        
        # Create form elements
        self.create_widgets()
        
    def create_widgets(self):
        # Form title
        title = ttk.Label(self.root, text="Data Entry Form", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Name Entry
        ttk.Label(self.root, text="Full Name:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        name_entry = ttk.Entry(self.root, textvariable=self.data["Name"], width=40)
        name_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Age Spinbox
        ttk.Label(self.root, text="Age:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        age_spin = ttk.Spinbox(self.root, from_=1, to=100, textvariable=self.data["Age"], width=10)
        age_spin.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        
        # Gender Combobox
        ttk.Label(self.root, text="Gender:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        gender_combo = ttk.Combobox(self.root, textvariable=self.data["Gender"], 
                                   values=["Male", "Female", "Other"], width=15)
        gender_combo.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
        
        # Email Entry
        ttk.Label(self.root, text="Email:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        email_entry = ttk.Entry(self.root, textvariable=self.data["Email"], width=40)
        email_entry.grid(row=4, column=1, padx=10, pady=5)
        
        # Subscription Checkbutton
        ttk.Checkbutton(self.root, text="Subscribe to newsletter", 
                       variable=self.data["Subscription"]).grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)
        
        # Satisfaction Scale
        ttk.Label(self.root, text="Satisfaction Level:").grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
        satisfaction_scale = ttk.Scale(self.root, from_=0, to=100, variable=self.data["Satisfaction"],
                                      orient=tk.HORIZONTAL)
        satisfaction_scale.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)
        
        # Comments Text
        ttk.Label(self.root, text="Comments:").grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
        self.comments_text = tk.Text(self.root, width=30, height=5)
        self.comments_text.grid(row=7, column=1, padx=10, pady=5)
        
        # Submit Button
        submit_btn = ttk.Button(self.root, text="Submit", command=self.submit_data)
        submit_btn.grid(row=8, column=1, padx=10, pady=20, sticky=tk.E)
        
    def submit_data(self):
        # Get all values from form
        try:
            # Get comments from Text widget
            self.data["Comments"].set(self.comments_text.get("1.0", tk.END).strip())
            
            # Create dictionary of values
            entry = {key: var.get() for key, var in self.data.items()}
            
            # Basic validation
            if not entry["Name"]:
                raise ValueError("Name is required")
            if not entry["Email"] or "@" not in entry["Email"]:
                raise ValueError("Valid email is required")
            
            # Save to Excel
            self.save_to_excel(entry)
            
            # Show success message
            messagebox.showinfo("Success", "Data saved successfully!")
            
            # Clear form
            for var in self.data.values():
                if isinstance(var, tk.StringVar):
                    var.set('')
                elif isinstance(var, tk.IntVar):
                    var.set(0)
            self.data["Age"].set(18)
            self.data["Satisfaction"].set(50)
            self.comments_text.delete("1.0", tk.END)
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def save_to_excel(self, data):
        # Convert data to DataFrame
        df = pd.DataFrame([data])
        
        # Try to load existing data or create new DataFrame
        try:
            existing_df = pd.read_excel("data.xlsx")
            updated_df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            updated_df = df
        
        # Save to Excel
        updated_df.to_excel("data.xlsx", index=False)

if __name__ == "__main__":
    root = tk.Tk()
    app = DataEntryForm(root)
    root.mainloop()