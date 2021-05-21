import re
string1="en%2Fimagegallery%2Fdetail%2Fpogba-cavani-and-van-de-beek-train-with-man-utd-on-16-marchTeam%20Level%2FFirst%20TeamTeam%20Level%2FFirst%20TeamTeam%20Level%2FAcademy"
match = '((.+%2F)+(%20)+)+
s = re.search(match,string1)
print(s)