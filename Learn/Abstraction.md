# Understanding Digital Abstractions
You gotta start somewhere
***

If you are reading this you are probably already aware of the fundamental components of a computing system. RAM, CPU and SSD are all common vernacular these days. What you might not know, is why these components are important or how we use them to compute tasks.

## The turing machine
Before we go on, it is important we establish a definition for 'computer'. Its one of those words we all know, but maybe don't quite understand. As with any word. the meaning differs based on context. At its most basic, computer is a 'machine' or 'system' capable of computing simple boolean task. That is to say, a computer must be able to make yes or no decisions. This is a nice definition however it falls a little flat of what we're aiming for. You see, modern computers are able to make billions of yes/no decisions asyncronously. This is where 'The Turing Mcahine' definition comes in handy.

Alan Turing was a man born in 1912. Alongside breaking the enigma code and devising the now famous 'Turing Test', Turing is widely regarded as the father of computer science, his major contribution being the 'Turing Machine'. The turing machine is a hypothetical computer capable of meeting the following requirements:
> 1. It should be able to compute 'tasks' based on a given set of rules
> 2. It should posses a form of memory. This memory must be sufficeint to compute any given task.
> 3. The memory must be linear in fashion
> 4. The machine must have a way to jump to abitrary points in its memory.

The example Turing came up with involved a long strip of material devided into equal sections. Each section could either be 'ON' or 'OFF'. This strip would act as the memory. The machine would then be able to read through the strip and makes decisions based on the input. It would also be able to jump to random points further up or down the strip. It is interesting to think about this becasue, provided enough material, you would indeed satisfy all the above criterea. The ON/OFF system is what we are going to focus on from now on. Turing had proven that simple binary state was all that was needed to represent any form of data possible. A revelation considering that other computing models of the time consisted on different types of memory depenending on the data. This meant that letters, numbers and any other type of information would require new methods of memory, which is obviously pretty impractical. These models also had problems when it came to mixing different data types in computations. Suppose you wanted to count the number of times a given letter appeared in a word. The word would first need to be read from punch card memory and passed through a conversion unit before being read over and retranslated into cathode-ray-tube memory in numercial form. The Turing machine beat all of this as it provided a common language, ON/OFF. These signals needed only to be interpreted as current flow through logic gates, and Boom, we have our modern turing machine. The only annoyance is having to define every single ON and OFF. This is where binary comes in.

## Level 0: Binary
Binary is a system that allows us to represent complex and lengthy systems of electronic signals in a small and convienient fashion.
Binary truly is the first layer of abstraction in computing. It is ground zero, the begining of everything. A binary system is one that records only two types of data ON (1) or OFF (0). This is helpful as its very easy to represent ON/OFF electronically. Current = ON, No current = off. A single ON/OFF is called a bit, 8 bits make a byte, why choose eight? We'll get to that later. These bits and bytes are stored in RAM or Random Access Memory in the form of small electronic currents. For the time being, we will consider RAM to be the only way to store information. This is our binary model. Current flow represents 'bits' of binary data. This current flow is then stored in RAM so it can be used multiple times.

There is a key distinction between this 'binary system' and 'binary counting'. Binary counting is a numerical system with only two digits. This is an important destinction because we chose to base computers on a 'binary system' NOT on 'binary counting'. In our early computers, ON/OFF has no real meaning, it is simply a means to an end. This fact is important: The names ON/OFF are somewhat abitrary and meaningless, we (humans) could just as easily called these opposing states CAT/DOG. By themselves, bits are meaningless, but from a series of bits (ON/OFF messages), human's can prescribe meaning. This is why computers are not based on 'Binary counting'; Counting and using numbers is a meaning we can _prescribe_ to ON/OFF messages. Counting in binary is the second layer of abstraction.

#### ASIDE: Alternate representations of binary
Throughout this guide I will generally use a numercial represenatation for binary. Instead of writing a byte like this `(ON)(OFF)(ON)(ON)(ON)(OFF)(OFF)(ON)` I will write `10111001` as it is much more succinct

#### ASIDE: Binary Logic
There are a number of binary logic operations that can be performed between bits. Remembering that a 'bit' is just an abstract representation of an electrical current, we can then see how it is possible to use transistors to perform logic operations. If you are not aware of what a transistor is, I will not bother to explain it in great depth. This document focuses directly on the software layer. I may write up a guide to computing electronics at a later date but for now, a simple explanation will suffice.
> A transistor is an electronic compenent that takes two inputs and gives an output based off them. It does this through the use of semiconductors. The two inputs are labeled 'collecter' and 'base'. The collecter has continuous current passed into it however it is unable to reach to 'emitter' which is the transistors output. However, when the base is powered it allows the current to jump to the emitter. 

I will not show the physical implementations for all the logic gates here, rather, I will simply list the key ones.

| GATE | Number of inputs      | Description |
| ---- | --------------------- | ----------- |
| AND  | 2                     | Output is true if both inputs (bits) are true (on) |
| NAND | 2                     | Output is false if both inputs are true |
| NOT  | 1                     | Output is true if input is false |
| OR   | 2                     | Output is true if one or both inputs is true |
| XOR  | 2                     | Ouput is true if only one input is true |
| NOR  | 2                     | Output is true is both inputs are false |
| XNOR | 2                     | Output is true if both inputs are equal |

From just 7 gates we are able to create any circuit necessary for a turing complete machine.

## Level 1: Counting and Numbers
Remember how I mentioned that 8 bits make a byte, well that is because 8 bits was found to be the minimum size necessary to convey useful information. Early computers could store small numbers, characters and boolean values in this space (Altough strictly speaking a bool can be represented in a single bit) and it quickly became the standard minumum unit of addressable memory from CPU manufacturers. This means it is impossible to use anything less than one byte to store any data. What does this have to do with counting? It all comes back to the distinction between a 'binary system' and 'binary counting'. If binary is the first layer of abstraction from pure electronics, then our ability to assign meaning to a collection of binary values is the second layer.  

#### ASIDE: Type definitions
As we begin to introduce more types of data, I will begin to reference them by specific names. We will explain why 'typing' is important later but for now just acknowledge the following types.
**INT:** Short for integer. Pretty self explanatory
**CHAR:** Short for charcter. It contains a simple character of text.
**FLOAT:** Short for floating point integer. Essentially a decimal
**BOOL:** Short for boolean. Stores a true/false value.
**String:** Essentially just a sentence or collection of chars.

The binary counting system is just another representation of numbers, but in 'base 2'. It often seems confusing or daunting when trying to understand a new counting system but in reality, if we look back to our primary school education, it comes a lot simpler. Lets start by disecting base 10 or 'our' number system. 

Place values is really the key here. Remember the 'ones, tens, and hundreds' columns that seemed so pointless, well you better appreciate primary school because those columns are really what number systems are all about. Lets look at this table:

| 10000000's | 1000000's | 100000's | 10000's | 1000's | 100's | 10's | 1's |
| ---------- | --------- | -------- | ------- | ------ | ----- |----- | --- |
|           0|          0|         0|        0|       0|      0|     0|    0|

We are instantly able to tell that this number is 0, but the full representation here is actually written `00000000`. Now obviously we know that we do not need to write all the extra zeroes but it is important to realise that both representations are correct, because in bytes, we don't drop extra zeroes. If you are particularly astute, you may have noticed an additional pattern:

| 10^7 | 10^6 | 10^5 | 10^4 | 10^3 | 10^2 | 10^1 | 10^0 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|     0|     0|     0|     0|     0|     0|     0|     0|

This is why we call our system 'base 10'; Each column has the base of 10 to an incremented index. This is what gives us place value. Additionally, there are 10 numbers in our counting system [0,1,2,3,4,5,6,7,8,9], which is why we use the base of 10. The other key compenent of counting with this system is 'carrying'. Whenever we want to increase the value of a column that already has the max value (9), we simply write zero in that collumn and add one to the next. When said in words:
> I add 9 to the 'ones' column. I wish to add an additional 1, make 10 in total. I now have 1 ten, and 0 ones.

This system works identically to any other base system. The power table for binary look like the following (recall that there is only 2 digits in binary and therefore is base 2):

| 2^7 | 2^6 | 2^5 | 2^4 | 10^3 | 2^2 | 2^1 | 2^0 |
| --- | --- | --- | --- | ---- | --- | --- | --- |
|    0|    0|    0|    0|     0|    0|    0|    0|

Or:

| 128's | 64's | 32's | 16's | 8's | 4's | 2's | 1's |
| ----- | ---- | ---- | ---- | --- | --- | --- | --- |
|      0|     0|     0|     0|    0|    0|    0|    0|

Carrying now everytime we hit 1, instead of 9. You'll note that there is 8 columns above, which is exactly the same amount of bits needed for a byte and because each column can hold only one of two values, we can use a bit to represent them. A key limitation of this system is that it requires much more space to write large numbers. In base 10, the 8th column is worth 10 million, in binary it is worth a meagre 128. This does not really matter though as we have plenty of bytes avaiblable to us in memory (In modern machines commonly up to 137438953472 of them). DO remember that we are essentially forced to use base 2 as our turing machines can only handle ON/OFF states. We have now completed the second layer of abstraction, prescribing meaning to a collection of bits. Lets do a simple example of binary counting to test our knowledge:

<details><summary>What is the base 10 equivilent for binary number `00000110`?</summary>
<p>

### 6

| 128's | 64's | 32's | 16's | 8's | 4's | 2's | 1's |
| ----- | ---- | ---- | ---- | --- | --- | --- | --- |
|      0|     0|     0|     0|    0|    1|    1|    0|

`(0*128) + (0*64) + (0*32) + (0*16) + (0*8) + (1*4) + (1*2) + (0*1) = 6`

</p>
</details>

#### ASIDE: Signing numbers & Maximum values
So far our examples have consisted of one byte unsigned integers with maximum value 255, this is a competely theoretical data type and is in practice more analogous to the char data type. 'one byte unsigned integer' may sound like a mouth full so lets break it down.

We can tell something is one byte by counting the number of bits in it. One byte is 8 bits so therefore `NumberOfBits/4 = NumberOfBytes`. If we count our above examples we can see there are 8 bits, 1 byte. Now how about the 'unsigned' part. Unsigned simply means that the number contains no sign (+/-), it simply exists as a magnitude. There are important implications for usinged integers as they have a significantly different range of values. The maximum value for a one byte unsigned int is 255, the maximum value for a signed int is 127. Why? It has to do with the way which we represent sign in memory.

As we saw earlier, a one byte unsigned int look like the following: `00000000`. The whole byte is used for storing the number, but what happens when we need negatives. Easy, just reserve the first bit as the sign: 1 = negative, 0 = positive, uhhhh not quite though. This approach allows for negative and positive zero, which would break logic gates (`10000000` and `00000000` are not the same yet they would both be considered 0..?). So instead, we use _2's compliment_, This method _does count 0 as being positive_, but that does not break maths so its fine. Two's compliment can be calculated by simply flipping the bits and adding one:
`00000110` (+6) gets flipped to become `11111001` then we add '1' > `11111010` (-6).
**NOTE:** The first bit in signed ints is still reserved to denote sign. 0 = positive, 1 = negative.
It is good to realise that signed ints have the same range of numbers as there equivilent unsigned int however their max value is much lower. This is because we reserve the first bit (with place value 128) for sign, effectively reducing the maxiumum possible value by 128. These two ints however, do maintain the same range as unsigned ints can go from -128 to +127 the range therefore being 255

#### ASIDE: Counting from zero
Due to the nature of binary, it has become standard practice in computing to count from zero. Instead of 1, 2, 3.. we get 0, 1, 2...
Hence the 1st item, comes second as we start with 0th item.

## Layer 2: Text and Typecasting
