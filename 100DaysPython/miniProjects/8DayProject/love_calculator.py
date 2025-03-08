def calculate_love_score(name_one, name_two):
    combined_names = (name_one + name_two).lower()

    #true_count = sum(combined_names(letter) for letter in "true")
    #love_count = sum(combined_names(letter) for letter in "love")
    #love_score = int(f"{true_count}{love_count}")
    true_count = 0
    for letter in "true":
        count = combined_names.count(letter)
        true_count += count
        print(f"{letter.upper()} occurs {count} times")

    love_count = 0
    for letter in "love":
        count = combined_names.count(letter)
        love_count += count
        print(f"{letter.upper()} occurs {count} times")

    love_score = int(f"{true_count}{love_count}")
    print(f"Love Score = {love_score}")
    return love_score

calculate_love_score("Ramazan Acikgoz","Marta Weronika Acikgoz")

def angela_solution(name1,name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)

angela_solution("Ramazan Acikgoz","Marta Weronika Acikgoz")



