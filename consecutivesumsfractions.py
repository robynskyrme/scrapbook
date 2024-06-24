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


def add_frac_vals(low, high,mn):
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



if __name__ == "__main__":
     farey_vals(1,12345,3)
     #add_frac_vals(1,1234,2)