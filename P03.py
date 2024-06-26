import string

def ispangram():
    #The quick brown fox jumps over the lazy dog!!"
    str1=input("Enter your sentence: ")
    alphabet =set(string.ascii_lowercase)
    set_str1 = set(str1.lower())
    return alphabet <= set_str1

def sum_of_digits(number):
    try:
        if number <0:
            raise ValueError("Negative number is not allowed.")
        if number <10:
            return number
        return number % 10 + sum_of_digits(number // 10)
    except Exception as e:
        print(e)

def lambda_func():

    L = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
    print("Original list: ",L)
    L_positive = list(filter(lambda x: x > 0,L))
    print(L_positive)

def map_func():
    L = [1, 2, 3, 4, 5]
    print("Original list: ", L)
    L_positive = list(map(lambda x: x*2,L))
    print(L_positive)

def pascals_triangle(n=None):
    triangle =[[1]]
    no_of_rows=n or 5
    for i in range(1,no_of_rows):
        row=[1]
        for j in range(0,i-1):
            row.append(triangle[i-1][j]+triangle[i-1][j+1])
        row.append(1)
        triangle.append(row)
    # for row in triangle:
    #     for element in row:
    #         print(element, end=' ')
    #     print('\n')
    return triangle

def write_triangles_to_file():

    for i in range (1,11):
        triangle = pascals_triangle(i)
        with open('./dataset/pascals_triangles.txt', 'a') as file:
            file.write(f"Pascal's triangle with {i} rows:\n")
            for row in triangle:
                for element in row:
                    # print(element, end=' ')
                    file.write(str(element))
                file.write("\n")





def caesar_cipher_decrypt(message, shift):
    decrypted_message = []

    for char in message:
        if char in string.ascii_uppercase:
            new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_message.append(new_char)
        elif char in string.ascii_lowercase:
            new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_message.append(new_char)
        else:
            decrypted_message.append(char)

    return ''.join(decrypted_message)


def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
    return set(words)


def count_valid_words(decrypted_message, dictionary):
    words = decrypted_message.split()
    valid_words_count = 0

    for word in words:
        cleaned_word = word.lower().strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
        if cleaned_word in dictionary:
            valid_words_count += 1

    return valid_words_count


def find_best_shift(encrypted_message, dictionary):
    max_valid_words = 0
    best_shift = 0
    best_decryption = ""

    for shift in range(1, 26):
        decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
        valid_words_count = count_valid_words(decrypted_message, dictionary)

        if valid_words_count > max_valid_words:
            max_valid_words = valid_words_count
            best_shift = shift
            best_decryption = decrypted_message

    return best_shift, best_decryption




while True:
    user_input = str(input("Enter exercise number (1-6) or 'q' to exit: "))

    match user_input:
        case "1":
            result =ispangram()
            print(result)
        case "2":
            input_number = int(input("Enter a positive integer: "))
            result =sum_of_digits(input_number)
            print(result)
        case "3":
            lambda_func()
        case "4":
            map_func()
        case "5":
            pascals_triangle()
        case "6":
            write_triangles_to_file()
        case "7":
            encrypted_message = input("Enter the text to be decrypted: ")
            dictionary = load_dictionary('./dataset/words.txt')

            best_shift, best_decryption = find_best_shift(encrypted_message, dictionary)

            print("Best shift:", best_shift)
            print("Decrypted message:", best_decryption)
        case "q":
            exit()
