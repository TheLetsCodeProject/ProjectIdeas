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
Now that we have a number system in place, we can move on to abstracting more types of data on top of them. So far, we have not actually done any real software work, an instead just given meaning to randoom arrangments of ON/OFF messages. This is basically the key to abstraction, simplying finding easier and easier ways to comprehend things. 

Consider the natural numbers. They map very convenienty to infinite sets. We can now choose to represent an item from a set simply by recording the position of that item in its set. This only requires one thing to work effectively, an ordered standard from which to match positions. 

One early example of these standards was the ASCII standard. ASCII stands for 'American Standard Code for Information Interchange' and was the first standardised character set. Now we could simply use numbers to represent letter, and then just match those numbers against the ASCII standard. Remember those 1 byte unsigned ints from before? Well they have 256 possible values, which was more than enough for every character in existence at the time (computers only targeted US/UK markets). In fact, representing letters and characters using a 1 byte unsigned int became so common that we starting calling that data type a 'char'.

Another example of abstraction on top of numbers is the RGB colour standard. RGB stands for Red-Green-Blue and directly correlates to the way digital screen show colour. Instead of having to memorize weird binary values for any colour we need, we can simply use RGB. RGB values have one byte of data per channel, meaning that we can give values up to 255 for each channel. This makes it incredibly easy to 'mix' colours. 

#### ASIDE: The byte boundary
Due to the design of computing architectures and RAM, it is wise to keep data inside byte boundaries, which are essentially theoretical walls between each segment of data. The occur every 2^n bytes, meaning that data types should fill 1, 2, 4, 8 or 16.. etc bytes of data. Since RGB is only 3 bytes (One byte per channel), it is often a convention to add a 'padding' byte to make the RGB data structure a total of 4 bytes.

It is interesting to see how far we have come. We are now able to say something like [A=1, B=2, C=3... etc] and then use a collection of numbers to represent words. However, we are actually using base-2 to represent those numbers, and our base-2 is infact represented in binary, which in turn represents electronic flow. 

If the following is a representation of some 'toy' RAM (Each new line is a byte boundary):
```
0000 0000 0000 0000 0000 0000 0000 0000 
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
```
If we were to place three RGB values without adding into this memory it would now look like:
```
0110 1100 0001 1110 1011 1100 0110 1100 |
0001 1110 1011 1100 0100 1111 1000 1100 |
0100 1110 0000 0000 0000 0000 0000 0000 |
0000 0000 0000 0000 0000 0000 0000 0000
```
Apart from it being difficult to tell the difference between RGB values, it is actually slower for the machine to work with as the data crosses byte boundaries, after 3 bytes, the next value starts. For a 2^n byte boundary we should instead use 4 bytes, which is why we use padding:
```
0110 1100 0001 1110 1011 1100 0000 0000 |
0001 1110 1011 1100 0100 1111 0000 0000 |
0100 1110 0011 0110 0001 1010 0000 0000 |
0000 0000 0000 0000 0000 0000 0000 0000 |
```
Our memory is now much neater and does not cross boundaries.

#### ASIDE: Hexadecimal
There are a few differrent layers throughout this, that, whilst minor and unimportant, can be very convenient. One such layer would be hexadecimal (hex for short). I will not elaborate on how it works as I would like to think my explanation of binary earlier was sufficent to use for other systems. Hex is base-16 and therefore consisting of 16 digits. These digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F, F having the value of 15. Hex is useful because the max value for a nybble (a half-byte or 4 bits: `0000`) is 15, We means we can represent one byte of data with just two hex digits. We represent hex with the prefix `0x` or `#` so it is clear what number format we are using. (binary gets prefixed with 0b or suffixed with b).

Example: If we wanted the colour white as an RGB value (white is the max of all colours), we would write something like:
```c
//This is pseudo code
WhiteColour = (255, 255, 255)
```
Now that doesnt really seem like a hassle but since we know that two hex digits map perfectly to a byte and that there are three bytes of value in RGB, we can represent any colour with just 6 digits. Futhurmore, because we know that each byte is going to be represented by two digits we eliminate the need for comma's and brackets as the are implicit between the fixed width hex bytes.
```c
WhiteColour = 0xFFFFFF
```

#### ASIDE: Encoding standards
ASCII was indeed sufficient for early systems and covered enough characters to be useful, however useful is not the same thing as adequate. Soon enough the original ASCII spec became too dated and missed many important characters both from the UK/US character set as well as those from other countries. Most modern systems now use unicode for their text encoding. Unicode includes a much greater character mapping including: The entire ASCII spec, Emoji, Every emergency symbol, Binary Digits and the symbols of virtually every language in the world. This means that modern programming languages usually define the char data type as being 16 bits (2 bytes instead of 1). 2 bytes of unsigned data is enough to represent 65,536 characters. For some very specific encodings it may be necessary to use a 32 bit integer.

## Where to next..?
We have now covered most of the super basic stuff and it leaves us with a few choices. There are no clear and obvious paths from here as we can take the abstractions in any direction. I believe the best choice going forward to to examine abstractions in programming. Building from our base of numbers and letters, we will begin to move away from binary operations and begin to look at the advent of programming as it is known today. But before we get moving, we must discuss some new concepts.

As of this point, the only hardware component we have touched on is RAM. Whilst RAM is important, but not the only necessary. To program we need a machine that is turing complete, one that can not only store data, but make decisions too. This is where those bitwise logic operators (logic gates) that I mentioned early on come important. As electronic current flows from the RAM, it enters the CPU. The CPU is not smart, it is not wise. In fact, the CPU is what makes our simple machines into real computers. It does this using billions of transistors (up to 6 billion in our phone CPUs, 19 billion in an i7 8700k) and millions of logic gates (AND, NAND, OR etc). As electricity hits the CPU, the transistors go to work flipping like a factory full of switch meddling monkeys. These switches eventually convert input to output, which can then be stored in RAM or hard storage. Of course, as with everything, there is wayyyyy more depth surrounding the implementation of CPUs, especially modern ones. However, due to the complex and messy nature of such technical proceedings and my addmittedly limited knowledge in certain edge senarios, I will not endevour to explain them.

For the next part of our journey, we will have to assume and skip some things. As I said in the intro, I do not intend to explain hardware implemtation as I find the prospect positively mind numbing. As  a result are to assume that somewhere along the line the necessary equipment to interface with the machine has been developed (Punch cards, Keyboard, Digital Storage, Monitors.. etc). I will also assume that you have experienced at least limited interaction with programming.

We will skip level 3 as it consists of early operating systems. These early systems were not important as they only provided the ability use file systems and save data and programs as well as navigate these folders of data.

## Level 4: Assembly Language
At some point (although I'm not sure when) there was a conceptual leap in programming. Originally you had to write code in binary of hex, literally considering every transistor's interaction to get the desired output. If you are masochistic and wish to experience the pain of existence caused by being a programmer in this time, try to master boolean algebra. The leap occured with the emergence of Assembly Language, Assembler Language or ASM (They are all the same thing). Assembly is the lowest level programming language and literally relied on the manual allocation of memory, meaning the programmer had to specifically specify where bytes should be placed and when. It was god awful, but still greatly better than binary or hex.  It was made even more annoying considering that every brand of CPU had their own version of ASM. Whenever you wrote some assembly code, you would have to put it through an 'assembler', which was an early attempt at a compiler written in hex. The assembler would then convert the ASM into machine code (see aside below) using twisted and peverse methods only an evil sociopath could fully comprehend. ASM is now considered so low level that it is essentially thought of as binary: So limited and basic that the CPU can just understand it (Although its not true, it still has to be put through an assembler before it can be run)

#### ASIDE: Machine code
Machine code is just plain binary information. The only difference between the binary we were looking at earlier and machine code, is that we have the intention of 'running' machine code. The goal of machine code is to be used to actually execute actions and be run through the CPU, the purpose of our simply data types was just to exist and represent data. Try this analogy: Whilst a dictionary and Spoken language are both defined using the same set of words, a dictionary purely exists to reference and define information, spoken language allows us to express ideas and convey instructions. Binary is the words, RAM and basic data is the dictionary, and machine code is the spoken part.

#### ASIDE: Too much?
If this last little bit has made you feel like we jumped a little bit too far, read the following for a much more indepth explanation.

When computers were new they had very, very limited processors. So simple that is was very concievable that one person could fully understand the entire chip. To write programs, you had to specifically lay out what individual charges need to occur in what order. If knew the system well enough you would be capable of manipulating the order in which switches flip. When a switch flipped it would redirect current allowing different switch to then flip, eventually culminating in an ouput. Its sorta of like a huge redstone circuit. If you've ever made a redstone lock, you have made a tiny processor; By manipulating certain inputs it computes a desired ouput, the door opening. Most operating systems provided basic functionalilty. Normally if you wanted to add two numbers, you'd have to write manual code for activating the adder ciruit in a processor, but with an operating system, youd just have to write some binary to interact with the OS and ask it to add the numbers instead. Modern operating systems are not responsible for such simple tasks anymore and instead deal with more complex things like graphics drivers. 

After establishing enough basic binary code, you were able to write more binary that used the stuff that was already written to do even more stuff. This in itself is a small layer of localised abstraction, hiding away the low level machine code and using it to build more complex routines. This is a pattern that is familier to all programming languages. Eventually the binary code base got sufficently large to take in an input stream of characters and turn them into more machine code. This was the true birth of Assembly. Eventually we get so abstracted that compilers don't even bother compiling to machine code, they just compile to assembly and let the operating system do the rest.

## The compiler and early programming languages
Assembly was a world faster to write than binary or hex code. It allowed for much more rapid development. For example the addtion of two itegers in binary looks like the following:
```c
Location Hex     Instruction Code Binary     Instruction Code Hex     Instruction     Comments
100              0010 0001 0000 0100         0x2104                   LDA 104         Load first operand into AC
101              0001 0001 0000 0101         0x1105                   ADD 105         Add second operand to AC
102              0011 0001 0000 0110         0x3106                   STA 106         Store sum in location 106
103              0111 0000 0000 0001         0x7001                   HLT             Halt computer
```
**NOTE:** All text in the above example was just to make the binary semi-readable to programmers of the time. The 'instruction code binary or hex' is what would have actually been written.
This same operation in assembly (specifically in intels IA-32 asm) look like the following:
```asm
leal 0x33333333, %ac
addb $-126,%ac
```
