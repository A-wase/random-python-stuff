original_sentence = input("Enter your the full text you want to change: ")

old_word = input("Now enter the word from your text that you want changed: ")

new_word = input("And now enter the new word to replace the old one with: ")

new_sentence = original_sentence.replace(old_word, new_word)

print(new_sentence)