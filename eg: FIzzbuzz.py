
def fizzbuzzer():
    for i in range(1,101):
        yield("fizz"*(i%3==0)
              +"buzz"*(i%5==0)
              or str(i))

print("\n".join(list(fizzbuzzer())))
