def palindrom (any_str):
    if any_str.lower() == any_str[::-1].lower():
        return print ("True")
    else: 
        return print ("False")

any_string = input("Введите любую строку: ") 

palindrom(any_string)