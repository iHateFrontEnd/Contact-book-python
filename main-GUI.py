from email_validator import validate_email, EmailNotValidError
import tkinter as tk
import json

def back(now, future):
    now.pack_forget()
    future.pack()

def make_conc(name, number, email):
    try:
        #validating email-id
        valid = validate_email(email)
        email = valid.email
    except EmailNotValidError:
        tk.Label(conc_data_frame, text='Please check your Email-ID or phone number you have entered').pack()

    if number.isnumeric() and len(number) >= 10:
        with open('contacts.json', 'a') as contacts:
            json_data = {
                "name": name,
                "number": number,
                "email": email
            }

            contacts.write(json.dumps(json_data, indent=3))

            contacts.write('\n')
            contacts.write('\n')

        back(conc_data_frame, startup_frame)
    elif len(number) == 0 and len(email) == 0:
        pass
    elif len(number) >= 1 and len(email) >= 1 :
        pass
    elif len(number) == 0:
        tk.Label(conc_data_frame, text='Please check the phone number you entered').pack()

#in this function the user will enter the contact data to make a contact
def enter_conc_data():
    startup_frame.pack_forget()

    global conc_data_frame

    conc_data_frame = tk.Frame(root)
    conc_data_frame.pack()

    tk.Label(conc_data_frame, text='Enter contact name').pack()

    name = tk.StringVar()   
    name_inp = tk.Entry(conc_data_frame, textvariable=name)
    name_inp.pack()

    tk.Label(conc_data_frame, text='Enter contact number').pack()

    number = tk.StringVar()
    number_inp = tk.Entry(conc_data_frame, textvariable=number)
    number_inp.pack()

    tk.Label(conc_data_frame, text='Enter contact Email-ID').pack()

    email = tk.StringVar()
    email_inp = tk.Entry(conc_data_frame, textvariable=email)
    email_inp.pack()

    #this function passes params to make_conc()
    def pass_params_save():
        name = name_inp.get()
        number = number_inp.get()
        email = email_inp.get()

        make_conc(name, number, email)

    save_conc_btn = tk.Button(conc_data_frame, text='Save', command=pass_params_save)
    save_conc_btn.pack()
    
    #this function passes parameters to back()
    def pass_params_back():
        back(conc_data_frame, startup_frame)

    back_btn = tk.Button(conc_data_frame, text='Back', command=pass_params_back)
    back_btn.pack()

#in this function the user enters the contact name that he/she is searching for
def search_conc():
    startup_frame.pack_forget() 

    global search_conc_frame

    search_conc_frame = tk.Frame(root)
    search_conc_frame.pack()

    tk.Label(search_conc_frame, text='Enter contact name to search it').pack()

    keyword = tk.StringVar()

    keyword_inp = tk.Entry(search_conc_frame, textvariable=keyword)
    keyword_inp.pack()

    #this function passes params to return_result()
    def pass_params_return_result():
        keyword = keyword_inp.get()
        return_result(keyword)

    return_result_btn = tk.Button(search_conc_frame, text='Search', command=pass_params_return_result)
    return_result_btn.pack()

    #this function pass parmas to back()
    def pass_params_back():
        back(search_conc_frame, startup_frame) 

    back_btn = tk.Button(search_conc_frame, text='Back', command=pass_params_back)
    back_btn.pack()

#this function returns the searched contact
def return_result(keyword):
    search_conc_frame.pack_forget()

    global result_frame

    result_frame = tk.Frame(root)
    result_frame.pack()

    with open('contacts.json', 'r') as contacts:
        text_found = False 
        line_num = 0

        for line in contacts:
            line_num += 1 

            if keyword in line:
                text_found = True
                break
        
        if text_found == True and keyword == '':
            search_conc_frame.pack()
            tk.Label(search_conc_frame, text='Enter a contact name').pack()
        elif text_found == True:
            search_conc_frame.pack_forget()

            number = contacts.readlines(line_num)
            email = contacts.readlines(line_num)

            tk.Label(result_frame, text=number[0]).pack()
            tk.Label(result_frame, text=email[0]).pack()

            #this function pass params to back()
            def pass_params_back():
                back(result_frame, startup_frame)

            home_btn = tk.Button(result_frame, text='Home', command=pass_params_back)
            home_btn.pack()
        else:
            search_conc_frame.pack_forget()
            tk.Label(result_frame, text='Contact not found').pack()

            #this function pass params to back()
            def pass_params_back():
                back(result_frame, startup_frame)

            home_btn = tk.Button(result_frame, text='Home', command=pass_params_back)
            home_btn.pack()

def main():
    global root 
    root = tk.Tk()
    root.title('Contact book')
    root.geometry('500x500')

    global startup_frame

    startup_frame = tk.Frame(root) 
    startup_frame.pack()

    make_conc_btn = tk.Button(startup_frame, text='Make a new contact', command=enter_conc_data)
    make_conc_btn.pack()

    view_concs_btn = tk.Button(startup_frame, text='View your contacts', command=search_conc)
    view_concs_btn.pack()

    root.mainloop()

if __name__ == '__main__':
    m
