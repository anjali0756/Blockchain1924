import tkinter as tk
import hashlib
import time

# Blockchain-style variables
money_received = 0
previous_hash = "GENESIS_HASH"
current_hash = "GENESIS_HASH"


def generate_hash(amount, timestamp):
    data = f"{amount}{timestamp}{previous_hash}"
    return hashlib.sha256(data.encode()).hexdigest()


def send_money():
    global money_received, previous_hash, current_hash

    try:
        amount = float(entry_amount.get())
    except ValueError:
        label_status.config(text="Enter a valid number!")
        return

    money_received += amount

    previous_hash = current_hash
    current_hash = generate_hash(amount, time.time())

    label_received.config(text=f"{money_received} ETH")
    label_prev_hash.config(text=previous_hash)
    label_curr_hash.config(text=current_hash)

    label_status.config(text="Transaction Successful ✅")
    entry_amount.delete(0, tk.END)


# GUI Window
window = tk.Tk()
window.title("Simple Storage Blockchain App")
window.geometry("450x500")

# Heading
tk.Label(window, text="SMART STORAGE BLOCKCHAIN APP",
         font=("Arial", 14, "bold")).pack(pady=10)

# Money input
tk.Label(window, text="Money to Send").pack()
entry_amount = tk.Entry(window)
entry_amount.pack(pady=5)

# Button
tk.Button(window, text="Send Money", command=send_money).pack(pady=10)

# Display fields
tk.Label(window, text="Received Money").pack()
label_received = tk.Label(window, text="0 ETH")
label_received.pack(pady=5)

tk.Label(window, text="Previous Hash").pack()
label_prev_hash = tk.Label(window, text=previous_hash, wraplength=400)
label_prev_hash.pack(pady=5)

tk.Label(window, text="Current Hash").pack()
label_curr_hash = tk.Label(window, text=current_hash, wraplength=400)
label_curr_hash.pack(pady=5)

# Status
label_status = tk.Label(window, text="")
label_status.pack(pady=10)

window.mainloop()