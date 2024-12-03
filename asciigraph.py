# Code to take a numerical dataset and output it crudely using ascii, with a given width parameter

def asciigraph(data,width,barchar,topchar):
    lower = min(data)
    upper = max(data)

    span = upper-lower

    scale = width/span

    display = ""

    for i in range(len(data)):
        display += topchar.rjust(int(data[i] * scale)-1,barchar) + "\n"

    print(display)

if __name__ == "__main__":
    test = [1,2]
    asciigraph(test,175,"-","|")