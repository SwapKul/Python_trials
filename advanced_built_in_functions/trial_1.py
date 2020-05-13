friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = {f.lower() for f in friends}
guests_lower = {g.lower() for g in guests}
intersection = friends_lower.intersection(guests_lower)
print([name.title() for name in intersection])
