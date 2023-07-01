def coding():
    message = input("type here")
    y = message.split()
    ans = []

    for x in range(len(y)):

        i = list(y[x])
        if len(i) >= 3:

            i.append(i[0])
            i.pop(0)
            i.insert(0, "abc")
            i.append("xyz")

            result = "".join(i)
            ans.append(result)

        else:
            i.reverse()
            result = "".join(i)
            ans.append(result)

    print(' '.join(ans))


def decode():

    message = input("type here")
    y = message.split()
    ans = []

    for x in range(len(y)):

        i = list(y[x])
        if len(i) >= 3:

            i.pop(0)
            i.pop(0)
            i.pop(0)
            i.pop(len(i)-1)
            i.pop(len(i) - 1)
            i.pop(len(i) - 1)
            i.insert(0, i[len(i) - 1])
            i.pop(len(i)-1)

            result = "".join(i)
            ans.append(result)

        else:
            i.reverse()
            result = "".join(i)
            ans.append(result)

    print(' '.join(ans))


coding()
decode()
