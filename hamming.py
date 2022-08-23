import math 

def toBinary(a):
    m = ''
    for i in a:
        m = m + bin(int(i, 16))[2:].zfill(4)
    return m

def toHex(a):
    m = hex(int(a, 2))[2:].zfill(8)
    return m
  
def main_decode_block(blk):
    par_bit_pos = [1,2,4,8,16,32]
    no_flip_list = []
    flip_list = []
    for i in par_bit_pos:
        pos = []
        temp = 0
        for j in range(i+1, len(blk)):
            if((i & j) != 0):
                pos.append(j)
                temp = temp + (blk[j] ^ 0)
            else:
                continue    
        
        if(temp%2 == 0):
            temp = 0
        else: 
            temp = 1

        if(blk[i] == temp):
            no_flip_list += pos
        else:
            flip_list.append(pos)

    if(len(flip_list) == 0):
        return 'NoFlips'
    
    else:
        flip_index=[]
        comm_indx1 = flip_list[0]
        for i in flip_list[1:]:
            comm_indx1 = list(set(comm_indx1).intersection(i))
    
        for k in comm_indx1:
            if k in no_flip_list:
                continue
            else:
                flip_index.append(k)
        return flip_index
         

def start_dec(codedmsg):
    print("Recieved encoded message: ", codedmsg)
    print("Number of blocks: ", int(len(codedmsg)/10))
    Flip_Indices = [] #to store flip index
    sol = ''
    for i in range(int(len(codedmsg)/10)):
        blk = toBinary(codedmsg[10*i:10*i+10])
        block_i=[int(x) for x in blk]
        k = main_decode_block(block_i)
        
        if(k == 'NoFlips'):
            blk2 = [str(x) for x in block_i]
            blk3 = [blk2[3]]+blk2[5:8]+blk2[9:16]+blk2[17:32]+blk2[33:39]
            sol = sol + toHex("".join(blk3))

        else:
            for pos in k:
                Flip_Indices.append(pos)
                if(block_i[pos] == 0):
                    block_i[pos] = 1
                else:
                    block_i[pos] = 0
            blk2 = [str(x) for x in block_i]
            blk3 = [blk2[3]]+blk2[5:8]+blk2[9:16]+blk2[17:32]+blk2[33:39]
            sol = sol + toHex("".join(blk3))

    if(len(Flip_Indices)==0):
        print("There is no flips in the encoded message!!")
    else:
        print("There are flips in bit positions: ", sorted(list(set(Flip_Indices))))         
    return sol

def hex_to_ascii(a):
    m = bytes.fromhex(a)
    return m.decode("ASCII")

h = "044B5281EE2E8BCC8942220109C9D2463BA1D0D0061BBDB1486A839085726203A5B8E044B31D89E44F2B05C9760A6101855E2F2181D1504EA981ADD80EFF0DAD660A03D995E44E2901DDE82F1325AFD206D39C81E83EC3A5C9E8662B97B85C"
k = start_dec(h)

print("The decoded message is: ", hex_to_ascii(k))  

