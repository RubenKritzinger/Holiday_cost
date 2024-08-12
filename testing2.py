def handleGo(x):
    return "Handeling a go ! " + x

def handleOk(x):
    return "handeling an ok! " + x

codewords = {
    'go': handleGo,
    'ok': handleOk,
}

codeword = "go"

if codeword in codewords:
    answer = codewords[codeword]("Argument")
    print(answer)
else:
        print("I don't know that codeword.")
