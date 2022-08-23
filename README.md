# Hamming-Code
When a message is sent though a network, there is a fair chance for the message to be garbled due to noise or other disturbances. But by using hamming codes, we can detect  if an error is occured and automatically correct it.
Consider a self-correcting message that contains data bits encoded with the Hamming code. The message is chucked into 40-bit code blocks, where each block encodes 4 characters or 32-bits of data. The rest of the 8 bits include check bits, extended hamming bit (1) and a padding bit (3). The extended hamming bit in this case is unused and is always set to zero. The trailing bit or the padding bit is also set to 0. 6 check bits are interleaved with the data bits
making (2) of size 38 bits. Please refer to the following figure to understand the block structure.

![image](https://user-images.githubusercontent.com/99118331/185870678-4f3a8dcf-0228-4ec4-8cdc-4b183705f740.png)

The entire message will be provided as a string of hex digits where each code block comprises of [40/4] i.e., 10 hex digits. Each block may either be error free or
have a single bit flipped. 

The program recovers the original message (ASCII character string) from the received coded message and will identify the offset of the flipped bit, if any, for each
code block and will return the original message.

A coded message to test the program (Might have flipped bits):<br>
044B5281EE2E8BCC8942220109C9D2463BA1D0D0061BBDB1486A839085726203A5B8E044B31D89E44F2B05C9760A6101855E2F2181D1504EA981ADD80EFF0DAD660A03D995E44E2901DDE82F1325AFD206D39C81E83EC3A5C9E8662B97B85C
