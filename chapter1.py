# https://medium.com/the-python-corner/using-virtual-environments-with-python-7166d3bfa218
# Scripts/activate.bat

from __future__ import division
from collections import Counter

users = [
    { "id": 0, "name" : "Hero" },
    { "id": 1, "name" : "Dunn" },
    { "id": 2, "name" : "Sue" },
    { "id": 3, "name" : "Chi" },
    { "id": 4, "name" : "Thor" },
    { "id": 5, "name" : "Clive" },
    { "id": 6, "name" : "Hicks" },
    { "id": 7, "name" : "Devin" },
    { "id": 8, "name" : "Kate" },
    { "id": 9, "name" : "Klein" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# for each user, thanks to the friendships data we assign their friends to the "friends" column
for user in users:
    user["friends"] = []

for i, j in friendships: 
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

# counting friends
def number_of_friends(user):
    return(len(user["friends"]))

total_connections = sum(number_of_friends(user)
                        for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

# most connected people
num_friends_by_id = [(user["id"], number_of_friends(user))
                        for user in users]

sorted(num_friends_by_id,
    key=lambda (user_id, num_friends): num_friends,
    reverse = True)

# friends of friends
def friends_of_friends_ids_bad(user):
    return [foaf["id"]
        for friend in user["friends"]
        for foaf in friend["friends"]]

