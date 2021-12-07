class Zamiana(object):

    def __init__(self, text):
        self.text = str(text)

    def __str__(self):
        output = ""
        words = self.text.split(' ')

        i = 0

        while(i < len(words)-1):
            output += (words[i+1] + " " + words[i] + " ")
            i+=2

        if len(words)%2 != 0:
            output += words[len(words)-1]

        return output

zamiana = Zamiana(input("in: "))
print("out: " + str(zamiana))