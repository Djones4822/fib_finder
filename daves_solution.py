from sys import argv


def recursion_fib(end_dig, cur_num = 0, prev_num = 0):
    if end_dig-1 <= 0:
        return cur_num
    else:
        if cur_num != 0:
            return recursion_fib(end_dig-1, cur_num + prev_num, prev_num = cur_num)
        else:
            return recursion_fib(end_dig-1, cur_num+1, prev_num)


def reg_fib(end_dig):
    prev_num = 0
    num = 0
    while end_dig:
        if num == 0:
            num += 1
        else:
            old = num
            num += prev_num
            prev_num = old
        end_dig -=1
    return num

    
def find_fib():
    while True:
        num = raw_input("What digit would you like to find?\n")
        try: 
            num = int(num)
            break
        except ValueError:
            print "You didn't enter a digit!"
            
    if len(argv)>1:
        if arvg[1] == 'recursive':
            return recursion_fib(num)
    else:
        while True:
            type = raw_input('Yes or No: Do you want to use recursion? (tip: helpful for large numbers!)\n')
            if type.upper() == 'YES':
                return recursion_fib(num)
            elif type.upper() == 'NO':
                return reg_fib(num)
            else: 
                print 'You need to answer "Yes" or "No", please.'


def main():
    print(find_fib())

if __name__ == '__main__':
    main()
