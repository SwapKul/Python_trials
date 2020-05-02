for nos in range(2, 101):
    for no in range(2, nos):
        if nos % no == 0:
            print(f"{nos} is a composite no")
            break
    else:
        print(f"{nos} is a prime no")
