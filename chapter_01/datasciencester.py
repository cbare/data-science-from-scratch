"""
Code from Chapter 1 of Data Science from Scratch
"""
from collections import Counter
from collections import defaultdict
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# a social network for data scientists
# ------------------------------------------------------------

names = [
    'Hero',
    'Dunn',
    'Sue',
    'Chi',
    'Thor',
    'Clive',
    'Hicks',
    'Devin',
    'Kate',
    'Klein']

users = [{'id':i, 'name':name, 'friends':[]} for i, name in enumerate(names)]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for i, j in friendships:
    users[i]["friends"].append(users[j]) # add i as a friend of j
    users[j]["friends"].append(users[i]) # add j as a friend of i


# ------------------------------------------------------------
# counting friends
# ------------------------------------------------------------

def number_of_friends(user):
    """how many friends does _user_ have?"""
    return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections / num_users

# create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
sorted(num_friends_by_id,
       key=lambda t: t[1],
       reverse=True)


# ------------------------------------------------------------
# finding friends-of-friends
# ------------------------------------------------------------

def not_the_same(user, other_user):
    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    """other_user is not a friend if he's not in user["friends"];
    that is, if he's not_the_same as all the people in user["friends"]"""
    return all(not_the_same(friend, other_user)
               for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]    # for each of my friends
                   for foaf in friend["friends"]    # count *their* friends
                   if not_the_same(user, foaf)      # who aren't me
                   and not_friends(user, foaf))     # and aren't my friends

print(friends_of_friend_ids(users[3]))


# ------------------------------------------------------------
# finding users with common interests
# ------------------------------------------------------------

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

# keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# keys are user_ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(interested_user_id
                   for interest in interests_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"])

most_common_interests_with(users[0])
# Counter({1: 2, 5: 1, 8: 1, 9: 3})

most_common_interests_with(users[3])
# Counter({2: 1, 4: 1, 5: 2, 6: 2})


# ------------------------------------------------------------
# understanding effect of experience on salary
# ------------------------------------------------------------

salaries_and_tenures = sorted([
    (83000, 8.7), (88000, 8.1),
    (48000, 0.7), (76000, 6),
    (69000, 6.5), (76000, 7.5),
    (60000, 2.5), (83000, 10),
    (48000, 1.9), (63000, 4.2)],
    key=lambda x: x[0])

# plot salary vs. experience
plt.plot([s[0] for s in salaries_and_tenures],
         [s[1] for s in salaries_and_tenures],
         'b*')
plt.ylabel('salary')
plt.xlabel('years of experience')
plt.show()

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

# keys are years, values are lists of the salaries for each tenure
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure_bucket[tenure_bucket(tenure)].append(salary)

# keys are tenure buckets, values are average salary for that bucket
average_salary_by_bucket = {
    tenure_bucket : sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

print(average_salary_by_bucket)
# {'between two and five': 61500.0,
#  'less than two': 48000.0,
#  'more than five': 79166.66666666667}

