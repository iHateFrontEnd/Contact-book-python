from email_validator import validate_email, EmailNotValidError
import json

#this function makes a new contact
def create_contact():
    print('Enter the contact name')
    name = input('> ')

    print('Enter contact number')
    contact_number = input('> ')

    print('Enter contact Email - ID')
    email = input('> ')

    try:
        #validating email id
        valid = validate_email(email)
        email = valid.email
        
        pass
    except EmailNotValidError:
        print('Enter proper Email - ID')
        create_contact()

    #this is the json data that will be written to the file
    conc_data = {
        "name": name,
        "number": contact_number,
        "email": email
    }
    
    #writing the json data
    with open('contacts.json', 'a') as contacts:
        contacts.write(json.dumps(conc_data, indent=3))

        contacts.write('\n')
        contacts.write('\n')
        
        print('Done!')

#this function prints all the contacts
def read_all_concs():
    with open('contacts.json', 'r') as contacts:
        print(contacts.read())

#this function only searches for a contact
def read_single_conc():
    print('Enter the contact name you are searching for: ')
    keyword = input('> ')

    flag = 0
    index = 0 

    with open('contacts.json', 'r') as contacts:
        #this the for loop which will go line by line
        for line in contacts:
            index += 1
            
            #checking if string is found in every line 
            if keyword in line:
                flag = 1
                break

        if flag == 1:
            print(contacts.readlines(index))
            print(contacts.readlines(index))
        else:
            print('Contact not found, please re-check the contact name that you entered')
            read_single_conc()

def main():
    print('To make a new contact type "!conc" and to search for contacts type "!view"')
    choose = input('> ')

    if choose == '!conc':
        create_contact()
    elif choose == '!view':
        print('To read all the contacts type "!all" and to search for a single contact type "!search"')
        choose = input('> ')

        if choose == '!all':
            read_all_concs()
        elif choose == '!search':
            read_single_conc()
        else: 
            main()
    else: 
        main()

if __name__ == '__main__':
    main()
