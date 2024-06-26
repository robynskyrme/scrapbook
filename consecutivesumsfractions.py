# Assigning a fraction to a number based on the series
# a/1 + (a-1)/2 + (a-3)/3 + (a-6)/4 + (a-10)/5 .......


                            # m = 1, n = 2
def farey_vals(low, high,mn):
    for x in range(low,high+1):
        a = x
        b = 1
        m = n = 0

        while a > 0:
            int_str = ""
            if a % b == 0:
                int_str = "     *"
            else:
                m += a % b
                n += b
                '''print(m)
                print(n)'''

            #print((str(a)) + "/" + str(b) + int_str)
            a -= b
            b += 1

        #print((str(m)) + "/" + str(n))
        if mn == 1:
            print(m)
        if mn == 2:
            print(n)
        if mn == 3 and n != 0:
            bar = "*"
            strx = str(x)
            width = 163
            print(strx.rjust(7, " ") + bar.rjust(int(width*(m/n))," "))


def add_frac_vals(low, high):
    for x in range(low,high+1):
        fracval = 0
        a = x
        b = m = n = 1

        while a > 0:
            int_str = ""
            if a % b == 0:
                int_str = "     *"
            else:

                m += a % b
                n += b

                fracval += m/n

            #print((str(a)) + "/" + str(b) + int_str)
            a -= b
            b += 1

        #print((str(m)) + "/" + str(n))
        print(fracval)

def count_integer_divs(low, high):
    max = 0
    for x in range(low,high+1):
        a = x
        b = 1
        m = n = 0

        count = 0

        while a > 0:
            if a % b == 0:
                count += 1
            else:
                m += a % b
                n += b
                '''print(m)
                print(n)'''

            #print((str(a)) + "/" + str(b) + int_str)
            a -= b
            b += 1

        if count > max:
            max = count
            print(max)


def return_only_x_with_k_integer_divs(low, high,k):
    for x in range(low,high+1):
        a = x
        b = 1
        m = n = 0

        count = 0

        while a > 0:
            if a % b == 0:
                count += 1
            else:
                m += a % b
                n += b
                '''print(m)
                print(n)'''

            #print((str(a)) + "/" + str(b) + int_str)
            a -= b
            b += 1

        if count == k:
            print(x)
#            print("             " + str(count))


if __name__ == "__main__":
     #farey_vals(1000000,1010000,2)
     #add_frac_vals(1,15)
     count_integer_divs(1 ,250000)
     #return_only_x_with_k_integer_divs(1,10000,7)