MediaType = input("What is your media type?: ")
Date = input("What is the creation date?: ")
Title = input("What is the title?: ")
Genre = input("what is the genre?: ")
Artist= input("Who is the artist?: ")
Rating = float(input("what is your rating?: "))

KMP = ['MediaType','Date','Title','Genre','Artist','Rating']

Pop = []
HipHop = []
Rap = []
Jazz = []
Rock = []
Country = []
Others = []

if Genre == "pop":
    Pop.append(Title)
elif Genre == "hip hop":
    HipHop.append(Title)
elif Genre == "rap":
    Rap.append(Title)
elif Genre == "jazz":
    Jazz.append(Title)
elif Genre == "rock":
    Rock.append(Title)
elif Genre == "country":
    Country.append(Title)
else:
    Others.append(Title)


