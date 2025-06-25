import re
import tkinter as tk

def check_password_strength(password):
    suggestions = []
    score = 0

    if len(password) < 8:
        suggestions.append("At least 8 characters required.")
    else:
        score += 1

    if not re.search(r'[A-Z]', password):
        suggestions.append("Include at least one uppercase letter.")
    else:
        score += 1

    if not re.search(r'[a-z]', password):
        suggestions.append("Include at least one lowercase letter.")
    else:
        score += 1

    if not re.search(r'\d', password):
        suggestions.append("Include at least one number.")
    else:
        score += 1

    if not re.search(r'[!@#$%^&*(){}\[\]:;<>,.?/~_+\-=|\\]', password):
        suggestions.append("Include at least one special character.")
    else:
        score += 1

    if score == 5:
        return "✅ Strong: Your password is secure!", "green"
    elif score >= 3:
        return "🟡 Moderate: Improve your password with the following suggestions:\n" + "\n".join(suggestions), "orange"
    else:
        return "🔴 Weak: Consider the following improvements:\n" + "\n".join(suggestions), "red"

def evaluate_password(event=None):  # event=None lets both button and Enter key work
    password = entry.get()
    result, color = check_password_strength(password)

    result_text.config(state='normal')
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)
    result_text.tag_add("colored", "1.0", "end")
    result_text.tag_config("colored", foreground=color)
    result_text.config(state='disabled')

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x350")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=(20, 5))

entry = tk.Entry(root, show='*', width=40, font=("Arial", 12))
entry.pack()
entry.bind("<Return>", evaluate_password)  # Bind Enter key

tk.Button(root, text="Check Strength", command=evaluate_password,
          font=("Arial", 12), bg="#007acc", fg="white", padx=10, pady=5).pack(pady=15)

result_text = tk.Text(root, height=8, width=58, font=("Arial", 10), wrap="word", borderwidth=2, relief="groove")
result_text.pack()
result_text.config(state='disabled')

# Run the app
root.mainloop()
