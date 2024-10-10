'''
Baahir's Repository link - https://github.com/Baahir2007/GCIS.git
Hishaam's Repository link - https://github.com/hb7464/hb7464 
Munzir's Repository link - https://github.com/munzir1910/GCIS123 
'''
def numbers():
    Total_Sum = 0
    while True:
        filename = input("Enter the filename: ").strip() #To strip the trailing and leading spaces while prompting filename from the user.
        if filename == "":
            break
        try:
            with open(filename) as f:
                Sum = 0
                for line in f:
                    words = line.split()
                    for word in words:
                        '''
                        if word.isdigit():
                            Sum += float(word)
                        '''
                        try:
                            Sum += float(word)
                        except ValueError :
                            print("Skipping non-numerical data",word)
                                
            print("Sum of numbers:",Sum)
            Total_Sum += Sum
        except FileNotFoundError :
            print("File does not exist..")
    print("Total Sum: ",Total_Sum)

def main():
    numbers()
if __name__ == "__main__":
    main()
