def enq(q_list, ie, aa):
    q_list[ie] = aa
    return q_list

def deq(q_list, id):
    q_list[id] = "null"
    return q_list
    
def main():
    a = input("リストの個数を入れよ")
    q_list = ["null" for i in range(int(a))]
    print(q_list)
    id = 0
    ie = 0
    while True:
        hh = input("deqかenqかbreakを押してください")
        if hh == "deq":
            q_list = deq(q_list, id)
            id += 1
            if id >= len(q_list):
                id = 0
        elif hh == "enq":
            num = input("入れたい数値を入れろ")
            q_list = enq(q_list, ie, int(num))
            ie += 1
            if ie >= len(q_list):
                ie = 0
        elif hh == "break":
            break
        else:
            print("何してんの")
        print(q_list)
            
if __name__ == '__main__':
    main()