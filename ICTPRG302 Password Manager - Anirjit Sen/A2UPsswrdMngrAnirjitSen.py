# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 19:19:04 2022

@author: Loopsmech
"""

# Give the user some context.
print("\nThis program you are able to store and read credentials for resources that you use!")

# Set an initial value for choice other than the value for 'quit'.
choice = '1, 2, 3, 4'

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[1] Enter 1 to create a resource entry.")
    print("[2] Enter 2 to retrieve the credentials of a resource")
    print("[3] Enter 3 to see list of all stored credentials")
    print("[4] Enter 4 to change credentials for a resource (creates new resource entry if there is no existing entry)")
    print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
    choice = input("\nMake your choice ")
    
    # Respond to the user's choice.
    
    if choice == '1':
    
        
        def writeCredentials(resource, username, password): #function module to write a credential to a text file
            import json #import the json module to access dump functionality. 
                    
                    #The credential is created as a dictionary type with key, value as stated:
            Credential_Entry = {       
                       
                        "Resource": resource,
                       
                        "Username": username,
                       
                        "Password": password
                     
                        }
                   
                    # print(Credential_Entry)
                    
                    #creates new file with the name of the resource + txt
            newfile = str(resource + ".txt")
                    
                    #json converts the dictionary type into a string when writing to a text file
            with open(newfile,"x") as f:
                        f.write(json.dumps(Credential_Entry, indent=2)) #json writing to a new file with indentation for formatting           

                
           
        
        global resource 
        
        resource = input("What is the name or domain of the resource you want to store credentials for?: ")
        #print(resource)
        
        global username
        
        username = input("What is your username for this resource?: ")
        
        
        #print(username)
        
        global password
        
        password = input("What is your password for this resource?: ")
        
        #rot3 encryption for password
        ClearText = password
        charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
        encPassword = "".join([charSet[(charSet.find(c)+3)%95] for c in ClearText])
        # print(encPassword)2
        #print(password)
        
        # calls writeCredentials(), passing user inputs as arguments to module1
       
        if True:   
            try:
            
                writeCredentials(resource, username, encPassword)
                
            except FileExistsError:
                    print("The credentials for this file already exists! Try menu option 4 to overwrite credentials!")
    
    elif choice == '2':
        
        def readCredentials(resource):
            
            #reconverting string json type into a dictionary type 
            import json
            
            #initialise dictionary
            d = {}
            
            newfile = str(resource + ".txt")
            
            #opening file as read only
            with open(newfile, "r") as f:
                d = (json.load(f))
                
                # print(d)
                print ("Resource is: " + (d['Resource']))
                print ("Username is: " +(d['Username']))
                
                #password decryption
                clearText = d['Password']
                charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
                d['Password'] = "".join([charSet[(charSet.find(c)-3)%95] for c in clearText])
                
                print ("Password is: " + (d['Password']))
        
        resource = input("\nWhat is the name of the resource you want to view credentials for?: ")
       
        readCredentials(resource)
        
    elif choice == '3':
        
            def readAll ():
                import glob
                
                
                def AllCredentials(credEntry):
                    
                    import json
                    
                    d = {}
                    
                    newfile = str(credEntry)
                    
                    with open(newfile, "r") as f:
                        d = (json.load(f))
                        
                        # print(d)
                        print ("\nResource is: " + (d['Resource']))
                        print ("Username is: " +(d['Username']))
                        
                        clearText = d['Password']
                        charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
                        d['Password'] = "".join([charSet[(charSet.find(c)-3)%95] for c in clearText])
                        
                        print ("Password is: " + (d['Password']))
                
                credentials = glob.glob('*.txt')
                
                # print(credentials)
                
                for x in range(len(credentials)):
                    
                    
                    global credEntry
                    
                    credEntry = (str(credentials[x]))
                    
                    
                    
                    
                
                    AllCredentials(credEntry)
               
                        
                            


            readAll() 
    
    elif choice == '4':
     
        #essentially the same as writeCredentials() but text file is overwritten!
        def writeCredentials(resource, username, password):
            
            import json 
            
            
            Credential_Entry = {       
               
                "Resource": resource,
               
                "Username": username,
               
                "Password": password
             
                }
           
            # print(Credential_Entry)
            
            newfile = str(resource + ".txt")
            
            
            with open(newfile,"w") as f:
                f.write(json.dumps(Credential_Entry, indent=2))           

        
        
        
        resource = input("What is the name or domain of the resource you want to change credentials for?: ")
        #print(resource)

        username = input("What is your username for this resource?: ")
        
        
        #print(username)
        
        password = input("What is your password for this resource?: ")
        
        #rot3 encryption for password
        clearText = password
        charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
        encPassword = "".join([charSet[(charSet.find(c)+3)%95] for c in clearText])
        # print(encPassword)
        #print(password)
        
        # passing user inputs as arguments to module
        writeCredentials(resource, username, encPassword)


        
    elif choice == 'q':
        print("\nExiting the menu\n")
    else:
        print("\nInvalid option, please try again.\n")
        
# Print a message that we are all finished.
print("Happy Surfing!")



