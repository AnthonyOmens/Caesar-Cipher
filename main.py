from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

keep_on = True
while keep_on == True:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  

  def caesar(text, shift, direction):
    if direction == "encode":
      shift *= 1 # not necessary but makes code easier to compare
    elif direction == "decode":
      shift *= -1 #shifts word to the left
  
    shifted_word_list = [ord(x) - 97 + shift for x in text]
    new_word = []
    for index in shifted_word_list:
      new_word.append(alphabet[index % 26])
      # % 26 makes it so higher letters loop back to the start of the alphabet 
    print(f"The encoded text is {''.join(new_word)}")

    keep = input("Do you want to keep going?\nY or N")
    if keep == "Y":
      keep_on == True
    else:
      keep_on == False

  # def keep_on_check():
  #   keep = input("Do you want to keep going?\n Y or N")
  #   if keep == "Y":
  #     keep_on == True
  #   else:
  #     keep_on == False
  
  caesar(text, shift,direction)
  # keep_on_check()
  