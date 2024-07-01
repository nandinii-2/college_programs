print("Welcome to the Indian Cuisine Menu!")

region = input("Do you prefer North Indian (N) or South Indian (S) cuisine? ")

if region.upper() == "N":
    meal = input("What meal would you like? Breakfast (B), Lunch (L), or Dinner (D)? ")
    if meal.upper() == "B":
        print("North Indian Breakfast Menu:")
        print("1. Chole Bhature")
        print("2. Parathas with Paneer")
        print("3. Poha")
    elif meal.upper() == "L":
        print("North Indian Lunch Menu:")
        print("1. Chana Masala with Rice")
        print("2. Tandoori Chicken with Naan")
        print("3. Palak Paneer with Roti")
    elif meal.upper() == "D":
        print("North Indian Dinner Menu:")
        print("1. Butter Chicken with Rice")
        print("2. Tandoori Chicken with Rice")
        print("3. Dal Makhani with Rice")
    else:
        print("Invalid meal choice!")
elif region.upper() == "S":
    meal = input("What meal would you like? Breakfast (B), Lunch (L), or Dinner (D)? ")
    if meal.upper() == "B":
        print("South Indian Breakfast Menu:")
        print("1. Idli with Sambar")
        print("2. Dosa with Chutney")
        print("3. Vada with Sambhar")
    elif meal.upper() == "L":
        print("South Indian Lunch Menu:")
        print("1. Sambhar Rice with Papad")
        print("2. Dosa with Chutney and Sambar")
        print("3. Upma with Fruits")
    elif meal.upper() == "D":
        print("South Indian Dinner Menu:")
        print("1. Chicken Biryani with Raita")
        print("2. Sambhar Rice with Vegetables")
        print("3. Dosa with Chutney and Sambar")
    else:
        print("Invalid meal choice!")
else:
    print("Invalid region choice!")
