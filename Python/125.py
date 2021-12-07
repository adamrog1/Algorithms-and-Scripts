znaki = [(1, 'I'),
         (5, 'V'),
         (10, 'X'),
         (50, 'L'),
         (100, 'C'),
         (500, 'D'),
         (1000, 'M')]


def derom(input):

    output = 0

    for i in range(0, len(input)):
        for each in znaki:
            if input[i] == each[1]:
                if each[0] > output:
                    output = each[0] - output
                else:
                    output += each[0]

    return output


print(derom("MMDLXVI"))
