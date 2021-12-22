#ff camelcase

kata = input()

kata = ''.join(x for x in kata.title() if not x.isspace())

katafix = kata[0].lower() + kata[1:]

print(str(katafix))

