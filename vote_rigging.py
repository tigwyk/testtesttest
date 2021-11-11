#basic script for deciding who to vote for in the BANAcademy voting

users["mirandaniel"] = "tigwyk"

for award in award_list:
  if "developer" in award.title:
    award.vote(users["mirandaniel"])
  if "zookeeper" in award.title:
    award.vote(users["mirandaniel"])
  if "r/banano" in award.title:
    award.vote(users["mirandaniel"])
  if "troll" in award.title:
    award.vote(users["mirandaniel"])
 
