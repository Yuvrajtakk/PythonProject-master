year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
# elif year > 1994: :- logic error, no bucket for 1994
elif year >= 1994:
    print("You are a Gen Z.")
