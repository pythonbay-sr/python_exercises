def longest_word():
    x = int(input("How many words are you willing to enter : "))
    word_1 = input("Enter a word : ")
    length = x-1
    for i in range(length):
        word_2 = input("Enter a word : ")
        if len(word_2)>len(word_1):
            longest_word=word_2
        else:
            longest_word=word_1
    print("The longest word is : ", longest_word)
    print("It's length is : ", len(longest_word))
longest_word()
