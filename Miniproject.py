import tkinter as tk
from datetime import datetime

window = tk.Tk()
window.title("Vehicle Management System")
window.geometry("1800x900")
window.configure(bg="black")

SN = 1
exit_time = datetime.now().strftime("%Y-%m-%d %I:%M %p")
# Initialize a variable to keep track of the slot number
current_slot = 1

# Initialize an empty list to store vehicle details
vehicle_data = []
exit_data = []

def move_to_page(page):
    for widget in frame_container.winfo_children():
        widget.destroy()
    page()

side_frame = tk.Frame(window)

# Create buttons
buttons = []

home = tk.Button(side_frame, height=3, width=15, text='HOME', font=('Cambria', 20), bg='orange', command=lambda: move_to_page(home_page))
home.pack(side=tk.TOP)

buttons.append(home)

add_vehicle = tk.Button(side_frame, height=3, width=15, text='ADD VEHICLE', font=('Cambria', 20), bg='orange', command=lambda: move_to_page(add_vehicle_page))
add_vehicle.pack(side=tk.TOP)

buttons.append(add_vehicle)

manage_vehicle = tk.Button(side_frame, height=3, width=15, text='MANAGE VEHICLE', font=('Cambria', 20), bg='orange', command=lambda: move_to_page(manage_vehicle_page))
manage_vehicle.pack(side=tk.TOP)

buttons.append(manage_vehicle)

history = tk.Button(side_frame, height=3, width=15, text='HISTORY', font=('Cambria', 20), bg='orange', command=lambda: move_to_page(history_page))
history.pack(side=tk.TOP)

buttons.append(history)

side_frame.pack(side=tk.LEFT)

frame_container = tk.Frame(window)
frame_container.pack(expand=True)

# Create a 8x5 grid of frames
def home_page():
    global vehicle_data
    num_rows, num_columns = 8, 5

    frames = [[tk.Frame(frame_container, width=100, height=500, borderwidth=1, relief="solid") for _ in range(num_columns)] for _ in range(num_rows)]

    # Use the grid geometry manager to arrange the frames
    for i in range(num_rows):
        for j in range(num_columns):
            frames[i][j].grid(row=i, column=j, padx=5, pady=5)

            # Check if the slot is assigned to a vehicle, if yes, display it in red
            for vehicle in vehicle_data:
                if vehicle != None and vehicle["Slot"] == (i * num_columns + j + 1):
                    label_text = f"Slot {vehicle['Slot']}\n{vehicle['Vehicle Number']}"
                    label = tk.Label(frames[i][j], text=label_text, bg="red", fg="white")
                    label.pack(expand=True, padx=50, pady=3) # Center the label in the frame
                    break
            else:
                    # If the slot is not assigned, display it in green
                    label_text = f"Slot {i * num_columns + j + 1}\nNone"
                    label = tk.Label(frames[i][j], text=label_text, bg="green", fg="white")
                    label.pack(expand=True, padx=50, pady=3) # Center the label in the frame

def add_vehicle_page():
    global owner_name_entry, mobile_number_entry, vehicle_number_entry, message_label

    title_label = tk.Label(frame_container, fg='white', bg='black', text='VEHICLE DETAILS', font=('cambria', 30))
    title_label.pack()

    owner_name_label = tk.Label(frame_container, text="Owner Name:", font=('cambria', 20), fg='black')
    owner_name_label.pack()
    owner_name_entry = tk.Entry(frame_container, font=('cambria', 15))
    owner_name_entry.pack(pady=10)

    mobile_number_label = tk.Label(frame_container, text="Mobile Number:", font=('cambria', 20), fg='black')
    mobile_number_label.pack()
    mobile_number_entry = tk.Entry(frame_container, font=('cambria', 15))
    mobile_number_entry.pack(pady=10)

    vehicle_number_label = tk.Label(frame_container, text="Vehicle Number:", font=('cambria', 20), fg='black')
    vehicle_number_label.pack()
    vehicle_number_entry = tk.Entry(frame_container, font=('cambria', 15))
    vehicle_number_entry.pack(pady=10)

    add_button = tk.Button(frame_container, text="Add Vehicle", font=('cambria', 15), fg='black', command=add_vehicle_details)
    add_button.pack(pady=20)

    message_label = tk.Label(frame_container, text="", fg="red")
    message_label.pack()

def is_valid_phone_number(phone_number):
    return len(phone_number) == 10 and phone_number.isdigit()

def add_vehicle_details():
    global owner_name_entry, mobile_number_entry, vehicle_number_entry, message_label, current_slot, vehicle_data, SN, exit_time

    owner_name = owner_name_entry.get()
    mobile_number = mobile_number_entry.get()
    vehicle_number = vehicle_number_entry.get()

    if owner_name and is_valid_phone_number(mobile_number):
        # Create a dictionary to store the current vehicle details
        vehicle_details = {
            "SN" : SN,
            "Owner Name": owner_name,
            "Mobile Number": mobile_number,
            "Vehicle Number": vehicle_number,
            "Slot": current_slot, # Assign the current slot number to the vehicle
            "Entry Time" : datetime.now().strftime("%Y-%m-%d %I:%M %p"),
            "EXIT" : exit_time
        }
        # Increment the slot number and S no. for the next vehicle
        current_slot += 1
        SN += 1

        # Add the dictionary to the list of vehicle_data
        vehicle_data.append(vehicle_details)

        # Update the message label
        message_label.config(text="Vehicle details added successfully", fg="green")

        # Clear the entry fields
        owner_name_entry.delete(0, tk.END)
        mobile_number_entry.delete(0, tk.END)
        vehicle_number_entry.delete(0, tk.END)
    else:
        message_label.config(text="Please fill in all the fields correctly", fg="red")

def exit(i) :
    global SN

    vehicle_data[i]['EXIT'] = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    exit_data.append(vehicle_data[i])
    vehicle_data[i] = None
    sn = 1

    for row in vehicle_data :
        if row == None :
            continue
        else :
            row['SN'] = sn
            sn += 1

    SN = sn
    move_to_page(home_page)

def Refresh(refresh):
    label = tk.Label(refresh)
    label.config(text='Data refreshed!',font=('cambria', 16,'bold'),bg='green',fg='red')
    label.pack()

    manage_vehicle_page()

def manage_vehicle_page() :
    global SN

    manage = tk.Frame(frame_container, width=window.winfo_width() - side_frame.winfo_width(),height=900,bg='white',bd=1)
    refresh = tk.Button(manage,bg='green',bd=1,text='Refresh',font=("Cambria",10,"bold"),fg='white',command=lambda:Refresh(refresh))
    refresh.place(x=0,y=0,width=manage.winfo_reqwidth(),height=40)
    table = tk.Frame(manage)

    headers = ["SN","Name","Mobile No","Vehicle No","Slot","Entry Time","Action"]

    for j, header in enumerate(headers):
        header_label = tk.Label(table, text=header,font=("Cambria",11,"bold"),fg="blue", borderwidth=1,width=19)
        header_label.grid(row=0, column=j, padx=1)

    for i, row in enumerate(vehicle_data):
        if row==None :
                continue
        for j, data in enumerate(row):
            if data == "EXIT" :
                cell_label = tk.Label(table,borderwidth=1,width=19)
                cell_label.grid(row=i+1, column=j, padx=1, pady=1)
                tk.Button(cell_label,bg='green',bd=1,text='EXIT',fg='white',command=lambda i=i:exit(i)).place(x=0,y=0,width=40,height=20,relx=0.5,rely=0.5,anchor="center")
                continue
            cell_label = tk.Label(table,text=row[data],font=("Cambria",10,"bold"),borderwidth=1, width=19)
            cell_label.grid(row=i+1, column=j, padx=1)

    table.place(x=0,y=40,width=manage.winfo_reqwidth(),height=860)
    manage.pack(side=tk.RIGHT)

def history_page():
    global exit_data
    history_frame = tk.Frame(frame_container, width=window.winfo_width() - side_frame.winfo_width(), height=900, bg='white', bd=1)
    table = tk.Frame(history_frame)
    headers = ["SN", "Name", "Mobile No", "Vehicle No", "Slot", "Entry Time", "Exit Time"]

    for j, header in enumerate(headers):
        header_label = tk.Label(table, text=header, font=("Cambria", 11, "bold"), fg="blue", borderwidth=1, width=19)
        header_label.grid(row=0, column=j, padx=1)

    for i, row in enumerate(exit_data):
        for j, data in enumerate(row):
            cell_label = tk.Label(table, text=row[data], font=("Cambria", 10, "bold"), borderwidth=1, width=19)
            cell_label.grid(row=i + 1, column=j, padx=1)

    table.place(x=0, y=0, width=history_frame.winfo_reqwidth(), height=860)
    history_frame.pack(side=tk.RIGHT)

window.mainloop()