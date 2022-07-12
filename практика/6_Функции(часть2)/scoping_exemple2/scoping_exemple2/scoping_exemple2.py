def outer_f():
    q = 8

    def inner_f():
        nonlocal q
        print(q)
        q = 10

    print(q)
    inner_f()
    print(q)


q = 0
print(q)
outer_f()
print(q)

