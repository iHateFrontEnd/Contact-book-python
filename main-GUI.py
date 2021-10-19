import tkinter as tk

root = tk.Tk()
root.title('Contact book GUI')
root.geometry('500x500')

#this is the function which creates the contacts
def create_contact(name, name_inp, email, email_inp, number, number_inp, contact_data_frame):
    name = name_inp.get()

    email = email_inp.get()

    number = number_inp.get()

    #writing contacts to the file
    with open ('contacts.txt', 'a+') as write_contacts:
        write_contacts.write('Name: ')
        write_contacts.write(name)

        write_contacts.write(' \n ')

        write_contacts.write('Email ID: ')
        write_contacts.write(email)

        write_contacts.write(' \n ')

        write_contacts.write('Number: ')
        write_contacts.write(number)

        write_contacts.write(' \n ')

    tk.Label(contact_data_frame, text='Done!').pack()

def enter_contact_data():
    startup_frame.pack_forget()

    contact_data_frame = tk.Frame(root)
    contact_data_frame.pack()

    tk.Label(contact_data_frame, text='Enter name: ').pack()

    name = tk.StringVar()

    name_inp = tk.Entry(contact_data_frame, textvariable=name)
    name_inp.pack()

    email = tk.StringVar()

    tk.Label(contact_data_frame, text='Enter Email ID: ').pack()

    email_inp = tk.Entry(contact_data_frame, textvariable=email)
    email_inp.pack()

    number = tk.StringVar()

    tk.Label(contact_data_frame, text='Enter phone number: ').pack()

    number_inp = tk.Entry(contact_data_frame, textvariable=number)
    number_inp.pack()

    def pass_params():
        create_contact(name, name_inp, email, email_inp, number, number_inp, contact_data_frame)

    save_contact = tk.Button(contact_data_frame, text='Save', command=pass_params)
    save_contact.pack()

#this the function list the contacts
def view_contacts():
    startup_frame.pack_forget()

    #reading from file 
    with open('contacts.txt', 'r') as listing_contacts:
        tk.Label(root, text=listing_contacts.read()).pack()

def app():
    global startup_frame

    startup_frame = tk.Frame(root)
    startup_frame.pack()

    new_contact_btn = tk.Button(startup_frame, text='Make new contact', command=enter_contact_data)
    new_contact_btn.pack()

    view_contact_btn = tk.Button(startup_frame, text='View contacts', command=view_contacts)
    view_contact_btn.pack()


app()

root.mainloop()
