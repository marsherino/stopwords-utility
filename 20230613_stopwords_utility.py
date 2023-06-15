import string

def removestops(textfile, stopfile):
    with open(textfile, 'r') as fulltext, open(stopfile, 'r') as stopwords:
        textstring = fulltext.readlines()
        textstring = ''.join(textstring)
        textstring = textstring.lower()
        textstring = textstring.translate(str.maketrans('', '', string.punctuation))
        textstring = textstring.split()
        stopstring = stopwords.readlines()
        stopstring = ''.join(stopstring)
        stopstring = stopstring.split()
        filtered = [t for t in textstring if t.lower() not in stopstring]
    writefile = open('cleanedfile.txt', 'w')
    writefile.writelines([str(i)+'\n' for i in filtered])
    writefile.close()

def main():
    textfile = input("Please enter the file location of the text you'd like to clean here, making sure it's a .txt file and to remove any quotation marks surrounding it: ")
    stopfile = input("Please enter the file location of your list of words to be removed here, making sure it's a .txt file and to remove quotation marks surrounding it: ")
    removestops(textfile, stopfile)
    print("Thank you! Your file is ready at cleanedfile.txt. Please remember to move or rename the file to prevent it being overwritten on future runs of this program.")

if __name__ == '__main__':
    main()