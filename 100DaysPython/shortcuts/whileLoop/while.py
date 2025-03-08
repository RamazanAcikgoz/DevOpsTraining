# WHILE LOOP

count = 1
while count <= 5:
    print("Looping")
    count += 1

counter = 0
while counter < 10:
    if counter % 2 == 0:
        counter += 1
        continue
    print(f"We're counting odd numbers: {counter}")
    counter += 1   