friends = ['Rolf', 'Charlie', 'Anna']
friends_lower = map(lambda x: x.lower(), friends)

print(friends_lower)
print(next(friends_lower))

print(list(friends_lower))

# or

friends_lower = [friend.lower() for friend in friends] # list comprehension

friends_lower = (friend.lower() for friend in friends) # generator comprehension


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])

users = [
    { 'username': 'rolf', 'password': '123' },
    { 'username': 'tecladoisawesome', 'password': 'youaretoo' }
]

user_objects = map(User.from_dict, users)

user_objects = [User.from_dict(u) for u in users]