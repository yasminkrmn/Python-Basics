# Strings

'Sustainability'.upper() # converts to uppercase
# 'SUSTAINABILITY'

'SUSTAINABILITY'.lower() # converts to lowercase
# 'sustainability'

'sustainability'.capitalize() # makes the first character have uppercase
# 'Sustainability'

'sustainable developments'.title()  # return words start with uppercased and all remaining characters have lowercase
# 'Sustainable Developments'

"sustainability".ljust(50, "#")
# 'sustainability####################################'

"sustainability".rjust(50, "#")
# '####################################sustainability'

"sustainability".center(50, "#")
# '##################sustainability##################'

"sustainable developments".split()
# ['sustainable', 'developments']

"sustainable development goals and ESG".split(" ", 2)
# ['sustainable', 'development', 'goals and ESG']

"".join(['sustainable', 'developments'])
# 'sustainabledevelopments'

" ".join(['sustainable', 'developments'])
# 'sustainable developments'

"sustainable".replace("a", "ı")
# 'sustıinıble'

"sustainable".replace("s", "r").replace("t", "z")
# 'rurzainable'

"sustainable".translate(str.maketrans("st","rz"))
# 'rurzainable'

"sustainable development goals and ESG".startswith("sus")
# True

"sustainable development goals and ESG".endswith("SG")
# True

"SUSTAINABILITY".islower()
# False

"SUSTAINABILITY".isupper()
# True

"Sustainable Developments".istitle()
# True

"12345".isnumeric()
# True
"12345A".isnumeric()
# False

"ARFRA".isalpha()
# True
"1ARFRA".isalpha()
# False

"C12345".isalnum()
# True
"111-".isalnum()
# False

"ABC KLM".isidentifier()
# False
"ABC_KLM".isidentifier()
# True

"Hello Python".isprintable()
# True
"Hello\nPython".isprintable()
# False

"ABC KLM".isspace()
# False
"".isspace()
# False
"  ".isspace()
# True

# # f-String
pi_number = 3.14159265358
pi_ = "Pi Number: " + str(pi_number)
# 'Pi Number: 3.14159265358'

pi_ = f"Pi Number: {pi_number}"
# 'Pi Number: 3.14159265358'

pi_ = f"Pi Number: {pi_number:.4f}"
# Pi Number: 3.1416






















