import os

with open("mydata.txt", encoding="utf-8", mode="w") as my_file:
    my_file.write("Some random text\nMore random text\nAnd some more")

with open("mydata.txt", encoding="utf-8") as my_file:
    
    line_num = 1
    line = []
    while True:
        line = my_file.readline()
        word_list = line.split()
        if not line:
            break

        print("\nLine:", line_num, ":" , line, end='')
        print("Number of words:", len(word_list))

        acc = 0
        for word in word_list:
            acc += len(word)
        word_len = acc / len(word_list)
        print("Average word length: {:.3f}".format(word_len))

        # You can also make as folows:
        #     for word in word_list:
        #          for char in word:
        #              char_count += 1
        #     avg_num_chars = char_count / len(word_list)

        line_num += 1