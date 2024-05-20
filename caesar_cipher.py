alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
          "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ask=True
while(ask==True):
 direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
 text=input("Type your message:\n").lower()
 shift=int(input("Type the shift number:\n"))

 def caesar(d,s,txt):
   cipher_text=""
   for letter in txt:
      if letter in alphabet:
        position=alphabet.index(letter)
        if d=="decode":
         new_position=position-s
        else:
         new_position=position+s
        cipher_text+=alphabet[new_position]
      else:
        cipher_text+=letter
   print(f"the {d} text is {cipher_text}")
 caesar(d=direction,s=shift,txt=text)
 a=input("Type 'yes' if you want to go again. Otherwise type 'no'").lower()    
 if a=="no":
   ask=False
print("Goodbye")







