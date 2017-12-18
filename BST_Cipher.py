class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = None
        for char in encrypt_str:
            self.insert(char)
            
    # A helper function for insert function.
    # If the character already exists, it does not add that character.
    def check_multiples(self,ch):
        curr = self.root
        while ((curr != None) and (curr.data != ch)):
            if (ch < curr.data):
                curr = curr.lChild
            else:
                curr = curr.rChild
        return curr
    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        if ch.isalpha() or ch == " ":
            new = Node(ch)
            if (self.root == None):
                self.root = new
            else:
                if not self.check_multiples(ch):
                    curr = self.root
                    par = self.root
                    while (curr != None):
                        par = curr
                        if (ch < curr.data):
                            curr = curr.lChild
                        else:
                            curr = curr.rChild
                    if (ch < par.data):
                        par.lChild = new
                    else:
                        par.rChild = new
                
    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        if not self.check_multiples(ch):
            return ""
        else:
            curr = self.root
            if ch == curr.data:
                return "*"
            else:
                strng = ""
                while ((curr != None) and (curr.data != ch)):
                    if (ch < curr.data):
                        curr = curr.lChild
                        strng += "<"
                    else:
                        curr = curr.rChild
                        strng += ">"
                return strng
            
    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding 
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        curr = self.root
        if st == "*":
            return self.root.data
        for item in st:
            if curr != None:
                if item == "<":
                    curr = curr.lChild
                elif item == ">":
                    curr = curr.rChild
            else:
                return ""
        return curr.data

    # the encrypt() function takes a string as input parameter, convert
    # it to lower case, and returns the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        copy_strng = ""
        st = st.lower()
        for item in st:
            if item.isalpha() or item == " ":
                copy_strng  += item
        encrypt_strng = ""
        for item in copy_strng :
            curr_encrypted = self.search(item)
            encrypt_strng +=curr_encrypted + "!"
            
        return encrypt_strng[0:-1]
            
    # the decrypt() function takes a string as input parameter, and
    # returns the decrypted string.
    def decrypt (self, st):
        raw_str =  ""
        for item in st:
            if item == ">" or item == "<" or item == "!" or item == "*":
                raw_str+=item       
        str_list = raw_str.split('!')
        decrypt_strng = ""
        for item in str_list:       
            decrypt_strng += self.traverse(item)
        return decrypt_strng

def main():
    encrypt_key = input("Enter encryption key: ")
    encrypt_key = encrypt_key.lower()
    key = Tree(encrypt_key)
    print()

    encrypting_str = input("Enter string to be encrypted: ")
    encrypt_strng = key.encrypt(encrypting_str)
    print("Encrypted string: ", encrypt_strng)
    print()

    decripting_str = input("Enter string to be decrypted: ")
    decrypt_strng = key.decrypt(decripting_str)
    print("Decrypted string: ", decrypt_strng)

main()
