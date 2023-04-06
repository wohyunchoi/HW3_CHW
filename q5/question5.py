def reverse_word(str1):

    str_list = str1.split(" ")
    for word in str_list[::-1]:
        print(word,end=' ')


if __name__ == "__main__":
    
    str1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth"
    str2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
    
    print("input str1")
    print(str1)
    print("\noutput str1")
    reverse_word(str1)

    print("\n\n\n\ninput str2")
    print(str2)
    print("\noutput str2")
    reverse_word(str2)
