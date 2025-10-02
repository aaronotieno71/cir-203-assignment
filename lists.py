
routes = ["Nairobi-Mombasa", "Kisumu-Nakuru", "Nairobi-Eldoret", "Nakuru-Kitale", "Meru-Embu",
          "Nairobi-Kisii", "Eldoret-Malaba", "Nakuru-Kericho", "Nyeri-Nanyuki", "Kisumu-Migori"]


routes.append("Busia-Malaba")
routes.remove("Nakuru-Kitale")


routes.sort()
routes.reverse()
print("Reversed sorted routes:", routes)

pcount_N = sum(route.startswith("N") for route in routes)
print("Routes starting with 'N':", count_N)


long_routes = [route for route in routes if len(route) > 10]
print("Routes longer than 10 characters:", long_routes)
