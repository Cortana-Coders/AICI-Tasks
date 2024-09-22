# Question 3
def give_me_a_key():
  try:
    key = input("Press any key: ")
    if key.isdigit():
      return int(key) ** 2
    elif key.isalpha():
      return key.upper()
    else:
      return key
  except ValueError:
    print("Invalid input.")
  except KeyboardInterrupt:
    print("Operation interrupted.")
  finally:
    print("Operation complete.")

give_me_a_key()