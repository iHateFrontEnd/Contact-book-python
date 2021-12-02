from email_validator import validate_email, EmailNotValidError
import tkinter as tk
from tkinter import filedialog
import os
import json

def back(now, future):
    now.pack_forget()
    future.pack()

#this function allows the user to delete his/her contacts
def delete_conc():
    startup_frame.pack_forget()

    global delete_conc_frame
    delete_conc_frame = tk.Frame(root)

    delete_conc_frame.pack()
    tk.Label(delete_conc_frame, text='Enter the contact name that you want to remove').pack() 
    keyword = tk.StringVar() 
    keyword_inp = tk.Entry(delete_conc_frame, textvariable=keyword)
    keyword_inp.pack()

    #this function removes or deletes contacts
    def remove_conc():
        keyword = keyword_inp.get()

        with open(username + '.txt') as contacts:
            line_num = 0
            text_found = False

            for line in contacts:
                line_num += 1

                if keyword in line:
                    text_found = True
                    break

            if text_found == True and keyword == '':
                tk.Label(delete_conc_frame, text='Please enter a contact name to delete it').pack()
            elif text_found == True:
                #loading the file into a variable
                with open(username + '.txt') as load_file:
                    rm_content = load_file.readlines()

                    #this function searches through the list returned by rm_content and deletes the contact that the user doesn't want
                    def search_list(rm_content, keyword):
                        for i in range(len(rm_content)):
                            if rm_content[i] == 'Name: ' + keyword + '\n':
                                for n in range(-2, 3):
                                    rm_content[i + n] = ''

                                break

                search_list(rm_content, keyword)

                with open(username + '.txt', 'w') as write_concs:
                    write_concs.writelines(rm_content)

                    delete_conc_frame.pack_forget()

                    global deleted_conc_frame
                    deleted_conc_frame = tk.Frame(root)
                    deleted_conc_frame.pack()

                    tk.Label(deleted_conc_frame, text='Done!').pack()

                    #this function passes params to back
                    def pass_params_back():
                        back(deleted_conc_frame, startup_frame)

                    home_btn = tk.Button(deleted_conc_frame, text='Home', command=pass_params_back)
                    home_btn.pack()
            else:
                delete_conc_frame.pack_forget()

                global err_del_conc_frame
                err_del_conc_frame = tk.Frame(root)
                err_del_conc_frame.pack()

                tk.Label(err_del_conc_frame, text='Contact not found').pack()

                #this function passes params to back
                def pass_params_back():
                    back(err_del_conc_frame, delete_conc_frame)

                back_btn = tk.Button(err_del_conc_frame, text='Back', command=pass_params_back)
                back_btn.pack()

    delete_conc_btn = tk.Button(delete_conc_frame, text='Delete', command=remove_conc)
    delete_conc_btn.pack()

    #this function passes params back()
    def pass_params_back():
        back(delete_conc_frame, startup_frame)

    back_btn = tk.Button(delete_conc_frame, text='Back', command=pass_params_back)
    back_btn.pack()

#this function allows the user the to edit contacts
def edit_concs():
    startup_frame.pack_forget()

    global edit_conc_frame
    edit_conc_frame = tk.Frame(root)
    edit_conc_frame.pack()

    tk.Label(edit_conc_frame, text='Enter the contact name that you want to replace').pack()

    keyword = tk.StringVar()
    keyword_inp = tk.Entry(edit_conc_frame, textvariable=keyword)
    keyword_inp.pack()

    tk.Label(edit_conc_frame, text='Enter new contact name').pack()

    new_name = tk.StringVar()
    new_name_inp = tk.Entry(edit_conc_frame, textvariable=new_name)
    new_name_inp.pack()

    tk.Label(edit_conc_frame, text='Enter the new number for your contact').pack()

    new_number = tk.StringVar()
    new_number_inp = tk.Entry(edit_conc_frame, textvariable=new_number)
    new_number_inp.pack()

    tk.Label(edit_conc_frame, text='Enter the new Email-ID for your contact').pack()

    new_email = tk.StringVar()
    new_email_inp = tk.Entry(edit_conc_frame, textvariable=new_email)
    new_email_inp.pack()

    #this function replaces contacts
    def replace_conc():
        keyword = keyword_inp.get()
        new_name = new_name_inp.get()
        new_number = new_number_inp.get()
        new_email = new_email_inp.get()

        try:
            valid = validate_email(new_email)
            new_email = valid.email

            if new_number.isnumeric() and len(new_number) >= 10:
                with open(username + '.txt') as contacts:
                    line_num = 0
                    text_found = False

                    for line in contacts:
                        line_num += 1

                        if keyword in line:
                            text_found = True
                            break

                    if text_found == True and keyword == '':
                        tk.Label(edit_conc_frame, text='Please enter a contact name to repalce it').pack()
                    elif text_found == True:
                        #editing the contact
                        with open(username + '.txt') as edit_concs:
                            new_content = edit_concs.readlines()

                            new_content[line_num - 3] = '\n'
                            new_content[line_num - 2] = '\n'
                            new_content[line_num - 1] = 'Name: ' + new_name + '\n'
                            new_content[line_num] = 'Number: ' + new_number + '\n'
                            new_content[line_num + 1] = 'Email: ' + new_email + '\n'

                        #writing the contacts
                        with open(username + '.txt', 'w') as write_edited_conc:
                            write_edited_conc.writelines(new_content)

                            edit_conc_frame.pack_forget()

                            global edit_result_frame
                            edit_result_frame = tk.Frame(root)
                            edit_result_frame.pack()

                            tk.Label(edit_result_frame, text='Done!').pack()

                            #this function passes params to back()
                            def pass_params_back():
                                back(edit_result_frame, startup_frame)

                            home_btn = tk.Button(edit_result_frame, text='Home', command=pass_params_back)
                            home_btn.pack()
                    else:
                        tk.Label(edit_conc_frame, text='The contact that you want to replace is not found').pack()
            else:
                tk.Label(edit_conc_frame, text='Please check the Email-ID or phone number you entered').pack()
        except EmailNotValidError:
            tk.Label(edit_conc_frame, text='Please check the Email-ID or phone number you entered').pack()

    save_conc_btn = tk.Button(edit_conc_frame, text='Save', command=replace_conc)
    save_conc_btn.pack()

    #this function passes params to back()
    def pass_params_back():
        back(edit_conc_frame, startup_frame)

    back_btn = tk.Button(edit_conc_frame, text='back', command=pass_params_back)
    back_btn.pack()

#this function backs up all the contacts 
def back_up_concs():
    startup_frame.pack_forget()

    global back_up_frame
    back_up_frame = tk.Frame(root)
    back_up_frame.pack()

    tk.Label(back_up_frame, text='Click the Start button below to choose where you wnat to backup your contact').pack()

    def choose_backup_location():

        try:
            select_target_dir = filedialog.askdirectory()

            #loading the content from current contact file
            with open(username + '.txt') as current_contacts:
                content = current_contacts.readlines()

            os.chdir(str(select_target_dir))

            backup_file = os.path.join(os.getcwd(), username + '.txt')

            #creating a the backup file and writing to it
            with open(backup_file, 'a') as write_backup_file:
                write_backup_file.writelines(json.dumps(content))

            back_up_frame.pack_forget()

            global back_to_home_frame
            back_to_home_frame = tk.Frame(root)
            back_to_home_frame.pack()

            tk.Label(back_to_home_frame, text='Done!').pack()

            #this function passes params to back
            def pass_params_back():
                back(back_to_home_frame, startup_frame)

            home_btn = tk.Button(back_to_home_frame, text='Home', command=pass_params_back)
            home_btn.pack()
        except:
            tk.Label(back_up_frame, text="Seems like you haven't saved any contacts").pack()


    start_backup = tk.Button(back_up_frame, text='Start', command=choose_backup_location)
    start_backup.pack()

    #this function passes params to back
    def pass_params_back():
        back(back_up_frame, startup_frame)

    back_btn = tk.Button(back_up_frame, text='Back', command=pass_params_back)
    back_btn.pack()

#this function allows the user to view his/her contacts
def search_concs():
    startup_frame.pack_forget()

    global search_conc_frame
    search_conc_frame = tk.Frame(root)
    search_conc_frame.pack()

    tk.Label(search_conc_frame, text='Enter the contact name that you searching for').pack()

    keyword = tk.StringVar()
    keyword_inp = tk.Entry(search_conc_frame, textvariable=keyword)
    keyword_inp.pack()

    #this function searches the contact and returns the searched contact
    def return_result():
        keyword = keyword_inp.get()

        with open(username + '.txt') as contacts:
            line_num = 0
            text_found = False

            for line in contacts:
                line_num += 1

                if keyword in line:
                    text_found = True
                    break

            if len(keyword) == 0 and text_found == True:
                tk.Label(search_conc_frame, text='Please enter a contact name').pack()
            elif text_found == True:
                search_conc_frame.pack_forget()

                global searched_result_frame
                searched_result_frame = tk.Frame(root)
                searched_result_frame.pack()

                number = contacts.readlines(line_num)
                email = contacts.readlines(line_num)

                tk.Label(searched_result_frame, text=number[0]).pack()
                tk.Label(searched_result_frame, text=email[0]).pack()

                #this function passes params to back()
                def pass_params_back():
                    back(searched_result_frame, startup_frame)

                home_btn = tk.Button(searched_result_frame, text='Home', command=pass_params_back)
                home_btn.pack()
            else:
                search_conc_frame.pack_forget()

                global conc_not_found_frame
                conc_not_found_frame = tk.Frame(root)
                conc_not_found_frame.pack()

                tk.Label(conc_not_found_frame, text='Contact not found').pack()

                #this function passes params to back()
                def pass_params_back():
                    back(conc_not_found_frame, search_conc_frame)

                back_btn = tk.Button(conc_not_found_frame, text='back', command=pass_params_back)
                back_btn.pack()

    search_conc_btn = tk.Button(search_conc_frame, text='Search', command=return_result)
    search_conc_btn.pack()

    #this function passes params to back()
    def pass_params_back():
        back(search_conc_frame, startup_frame)

    back_btn = tk.Button(search_conc_frame, text='Back', command=pass_params_back)
    back_btn.pack()

#this function the user creates a contact
def save_conc():
    startup_frame.pack_forget()

    global save_conc_frame
    save_conc_frame = tk.Frame(root)

    save_conc_frame.pack()

    tk.Label(save_conc_frame, text='Enter a name for your new contact').pack()

    name = tk.StringVar()
    name_inp = tk.Entry(save_conc_frame, textvariable=name)
    name_inp.pack()

    tk.Label(save_conc_frame, text='Enter a number for your contact').pack()

    number = tk.StringVar()
    number_inp = tk.Entry(save_conc_frame, textvariable=number)
    number_inp.pack()

    tk.Label(save_conc_frame, text='Enter a Email-ID for your contact').pack()

    email = tk.StringVar()
    email_inp = tk.Entry(save_conc_frame, textvariable=email)
    email_inp.pack()

    #this function writes the contact to contacts.txt
    def write_conc():
        name = name_inp.get()
        number = number_inp.get()
        email = email_inp.get()


        try:
            valid = validate_email(email)
            email = valid.email

            if number.isnumeric() and len(number):
                with open(username + '.txt', 'a') as contacts:
                    contacts.write('\n')
                    contacts.write('\n')

                    contacts.write('Name: ' + name)
                    contacts.write('\n')

                    contacts.write('Number: ' + number)
                    contacts.write('\n')

                    contacts.write('Email: ' + email)
                    contacts.write('\n')

                    save_conc_frame.pack_forget()

                    global saved_conc_frame
                    saved_conc_frame = tk.Frame(root)
                    saved_conc_frame.pack()

                    tk.Label(saved_conc_frame, text='Done!').pack()

                    #this function passes params to back()
                    def pass_params_back():
                        back(saved_conc_frame, startup_frame)

                    home_btn = tk.Button(saved_conc_frame, text='Home', command=pass_params_back)
                    home_btn.pack()
            else:
                tk.Label(save_conc_frame, text='Please check your phone number').pack()
        except EmailNotValidError:
            tk.Label(save_conc_frame, text='Please check the Email-ID your entered').pack()

    save_conc_btn = tk.Button(save_conc_frame, text='Save', command=write_conc)
    save_conc_btn.pack()

    #this function passes params to back()
    def pass_params_back():
        back(save_conc_frame, startup_frame)

    back_btn = tk.Button(save_conc_frame, text='Back', command=pass_params_back)
    back_btn.pack()

#this function allows the user to do everything 
def startup():
    global startup_frame
    startup_frame = tk.Frame(root)
    startup_frame.pack()

    make_conc_btn = tk.Button(startup_frame, text='Make a contact', command=save_conc)
    make_conc_btn.pack()

    view_conc_btn = tk.Button(startup_frame, text='View contacts', command=search_concs)
    view_conc_btn.pack()

    edit_conc_btn = tk.Button(startup_frame, text='Edit contact', command=edit_concs)
    edit_conc_btn.pack()

    delete_conc_btn = tk.Button(startup_frame, text='Delete contact', command=delete_conc)
    delete_conc_btn.pack()    

    backup_btn = tk.Button(startup_frame, text='Back up', command=back_up_concs)
    backup_btn.pack()

    #this function logs out the user by reopening the same window
    def logout_user():
        back(startup_frame, login_frame)

    log_out_btn = tk.Button(startup_frame, text='Logout', command=logout_user)
    log_out_btn.pack()

#this function allows the user to login 
def login(username, password):
    try:
        with open('account.json') as users:
            accounts = users.readlines()
        
            #this function loads the users file into a list then searches for the username and password
            def search_username_password():
                username_found = True

                #checking username
                for i in range(len(accounts)):
                    if accounts[i] == '"username": "' + username + '",\n':
                        username_found = True
                        break
                
                if username_found == True:
                    password_found = False
                    
                    #checking password
                    for n in range(len(accounts)):
                        if accounts[n] == '"password": "' + password + '"\n':
                            password_found = True
                            break

                    if password_found == True:
                        username_list = accounts[i]
                        password_list = accounts[n]

                        if len(username_list) == 16 + len(username):
                            if len(password_list) == 15 + len(password):
                                login_frame.pack_forget()
                                startup()
                            else:
                                tk.Label(login_frame, text='Incorrect password or username').pack()
                        else:
                            tk.Label(login_frame, text='Incorrect password or username').pack()
                    else:
                        tk.Label(login_frame, text='Incorrect password or username').pack()
                else:
                    tk.Label(login_frame, text='Incorrect password or username').pack()

            search_username_password()
    except:
        with open('account.json', 'a'):
            pass

        login()

def create_account():
    login_frame.pack_forget()

    global create_account_frame
    create_account_frame = tk.Frame(root)
    create_account_frame.pack()

    tk.Label(create_account_frame, text='Enter your new username:').pack()

    new_username = tk.StringVar()
    new_username_inp = tk.Entry(create_account_frame, textvariable=new_username)
    new_username_inp.pack()

    tk.Label(create_account_frame, text='Enter your new password:').pack()

    new_password = tk.StringVar()
    new_password_inp = tk.Entry(create_account_frame, textvariable=new_password)
    new_password_inp.pack()

    #this function saves the users info in account.json
    def write_username_pwd():
        new_username = new_username_inp.get()
        new_password = new_password_inp.get()

        if new_username == '' and new_password == '':
            tk.Label(create_account_frame, text='Please enter a proper username and password').pack()
        elif len(new_username) >= 1 and new_password == '':
            tk.Label(create_account_frame, text='Please enter a proper password').pack()
        elif new_username == '' and len(new_password):
            tk.Label(create_account_frame, text='Please enter a  proper username').pack()
        elif len(new_username) >= 1 and len(new_password) >= 1:
            with open('account.json', 'a') as users:
                json_data = {
                    "username": new_username,
                    "password": new_password
                }

                users.write('\n')

                users.write(json.dumps(json_data, indent=0))

            back(create_account_frame, login_frame)

    create_conc_btn = tk.Button(create_account_frame, text='Create', command=write_username_pwd)
    create_conc_btn.pack()
   
    #this function pass params to back
    def pass_params_back():
        back(create_account_frame, login_frame)

    home_btn = tk.Button(create_account_frame, text='Home', command=pass_params_back)
    home_btn.pack()
 
def login_data():
    global root
    root = tk.Tk()
    root.title('Contact book')
    root.geometry('500x500')

    global login_frame
    login_frame = tk.Frame(root)
    login_frame.pack()

    tk.Label(login_frame, text='Enter your user name to login').pack()

    username = tk.StringVar()
    username_inp = tk.Entry(login_frame, textvariable=username)
    username_inp.pack()

    tk.Label(login_frame, text='Enter the password to login').pack()

    password = tk.StringVar()
    password_inp = tk.Entry(login_frame, textvariable=password)
    password_inp.pack()

    def pass_params_login():
        global username
        username = username_inp.get()

        global password
        password = password_inp.get()

        login(username, password)

    login_btn = tk.Button(login_frame, text='Login', command=pass_params_login)
    login_btn.pack()

    tk.Label(login_frame, text="If you don't yet have an account then create one by click the button below").pack()

    sign_up_btn = tk.Button(login_frame, text='Sign up', command=create_account)
    sign_up_btn.pack()

    root.mainloop()

if __name__ == '__main__':
    login_data()
