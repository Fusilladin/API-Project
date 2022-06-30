import bcrypt

bcrypt.help
input = "dog"
saltRounds = "8"

hash = bcrypt.hash(input, saltRounds)

print(hash)
