# 5.10.2023
# for Peter Manson on National Poetry Day

teens = [None,"one","two","three","four","five","six","seven",
         "eight","nine","ten","eleven","twelve","thirteen","fourteen",
         "fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = [None,None,"twenty","thirty","forty","fifty","sixty","seventy",
        "eighty","ninety"]

def cardinal(n):

    word = ""

    if n//100 > 0 and n//100 < 10:
        word += teens[n//100] + " hundred"
        if n % 100 != 0:
            word += " and "

    if n % 100 < 20 and n % 100 > 0:
        word += teens[n % 100]

    if n % 100 > 19:
        word += tens[n//10 % 10]
        if n % 10 != 0:
            word += "-" + teens[n % 10]

    return word

text = ["Now, of my threescore years and ",
        " and ten,\nTwenty will not come again,\nAnd take from ",
        " springs a score,\nIt only leaves me "," more.\n"]

if __name__ == "__main__":
    for j in range (1,124):
        print(text[0] + cardinal(j) +
              text[1] + cardinal(j+70) +
              text[2] + cardinal(j+50) +
              text[3])