"""
Die Slice-Notation
string: TestString
# [<first element to include> : <first element to exclude> : <step> ]

a[start:stop]  # beginnt bei Start und endet bei Stop - 1
a[start:]      # beginnt bei Start und nimmt den Rest
a[:stop]       # beginnt bei 0 und endet bei Stop - 1
a[:]           # kopiert ganzen String
"""
city = "Nürnberg"
city_neu = city[1:] # ürnberg => erzeugt Substring von Index 1 - Ende
print(city_neu) # 
city_neu = city[1:5] # ürnb => erzeugt Substring von Index 1 - 5 (exlusive)
print(city_neu) # ürnb
city_neu = city[-2:] # Nürnberg
print(city_neu) # rg

city_neu = city[:-1] # Nürnber
print(city_neu) # Nürnber


"""
# Übung
# Schneide jeweils alle A aus den Strings
AAAAB => AAAA
BBAAABBB => AAA
AAAABBBB => AAAA
ABBBBB => A
"""
# Alle A ausschneiden
string = "AAAAB"
print("AAAAB => AAAA: ", string[:-1])

string = "BBAAABBB"
print("BBAAABBB => AAA: ", string[2:5])

string = "AAAABBBB"
print("AAAABBBB => AAAA: ", string[:-4])

string = "BBAABBBB"
print("BBAABBBB => AA: ", string[2:-4])

string = "ABBBBB"
print("ABBBBB => A: ", string[:1])