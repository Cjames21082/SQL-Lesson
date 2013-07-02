
def parser(query):
    query = " " + query

    tokens = []

    index = 0

    while index < len(query):
        if query[index] == chr(39):
            start = index + 1

            j = start
            print "start:", j
            while query[j] != chr(39) and j < len(query):
                print " I am j1 in the quote loop:", j
                j+=1
                

            tokens.append(query[start:j])
            print tokens

            index = j +1

        elif query[index] == " ":
            start = index + 1

            j = start
            while query[j] != " " and j < len(query):
                print " I am j2 in the space loop:", j
                j += 1


            tokens.append(query[start:j])
            print tokens

            index = j
            print index

        #index += 1
        #print "index outside of while loop:", index

        
    
    return tokens


print parser("John said 'Howdy Doogie' on a house")