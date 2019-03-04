# Understanding Digital Abstractions
You gotta start somewhere
***

If you are reading this you are probably already aware of the fundamental components of a computing system. RAM, CPU, and SSD are all common vernacular these days. What you might not know, is why these components are important or how we use them to compute tasks.

## The Turing machine
Before we go on, it is important we establish a definition for 'computer'. Its one of those words we all know, but maybe don't quite understand. As with any word. the meaning differs based on context. At its most basic, a computer is a 'machine' or 'system' capable of computing a simple boolean task. That is to say, a computer must be able to make yes or no decisions. This is a nice definition however it falls a little flat of what we're aiming for. You see, modern computers are able to make billions of yes/no decisions asynchronously. This is where 'The Turing Machine' definition comes in handy.

Alan Turing was a man born in 1912. Alongside breaking the enigma code and devising the now famous 'Turing Test', Turing is widely regarded as the father of computer science, his major contribution being the 'Turing Machine'. The Turing machine is a hypothetical computer capable of meeting the following requirements:
> 1. It should be able to compute 'tasks' based on a given set of rules
> 2. It should possess a form of memory. This memory must be sufficient to compute any given task.
> 3. The memory must be linear in fashion
> 4. The machine must have a way to jump to arbitrary points in its memory.

The example Turing came up with involved a long strip of material divided into equal sections. Each section could either be 'ON' or 'OFF'. This strip would act as the memory. The machine would then be able to read through the strip and makes decisions based on the input. It would also be able to jump to random points further up or down the strip. It is interesting to think about this because, provided enough material, you would indeed satisfy all the above criteria. The ON/OFF system is what we are going to focus on from now on. Turing had proven that a simple binary state was all that was needed to represent any form of data possible. A revelation considering that other computing models of the time consisted of different types of memory depending on the data. This meant that letters, numbers and any other type of information would require new methods of memory, which is obviously pretty impractical. These models also had problems when it came to mixing different data types in computations. Suppose you wanted to count the number of times a given letter appeared in a word. The word would first need to be read from punch card memory and passed through a conversion unit before being read over and retranslated into cathode-ray-tube memory in numerical form. The Turing machine beat all of this as it provided a common language, ON/OFF. These signals needed only to be interpreted as current flow through logic gates, and Boom, we have our modern Turing machine. The only annoyance is having to define every single ON and OFF. This is where binary comes in.

## Level 0: Binary
Binary is a system that allows us to represent complex and lengthy systems of electronic signals in a small and convenient fashion.
Binary truly is the first layer of abstraction in computing. It is ground zero, the beginning of everything. A binary system is one that records only two types of data ON (1) or OFF (0). This is helpful as its very easy to represent ON/OFF electronically. Current = ON, No current = off. A single ON/OFF is called a bit, 8 bits make a byte, why choose eight? We'll get to that later. These bits and bytes are stored in RAM or Random Access Memory in the form of small electronic currents. For the time being, we will consider RAM to be the only way to store information. This is our binary model. Current flow represents 'bits' of binary data. This current flow is then stored in RAM so it can be used multiple times.

There is a key distinction between this 'binary system' and 'binary counting'. Binary counting is a numerical system with only two digits. This is an important distinction because we chose to base computers on a 'binary system' NOT on 'binary counting'. In our early computers, ON/OFF has no real meaning, it is simply a means to an end. This fact is important: The names ON/OFF are somewhat arbitrary and meaningless, we (humans) could just as easily called these opposing states CAT/DOG. By themselves, bits are meaningless, but from a series of bits (ON/OFF messages), human's can prescribe meaning. This is why computers are not based on 'Binary counting'; Counting and using numbers is a meaning we can _prescribe_ to ON/OFF messages. Counting in binary is the second layer of abstraction.

#### ASIDE: Alternate representations of binary
Throughout this guide, I will generally use a numerical representation for binary. Instead of writing a byte like this `(ON)(OFF)(ON)(ON)(ON)(OFF)(OFF)(ON)` I will write `10111001` as it is much more succinct

#### ASIDE: Binary Logic
There are a number of binary logic operations that can be performed between bits. Remembering that a 'bit' is just an abstract representation of an electrical current, we can then see how it is possible to use transistors to perform logic operations. If you are not aware of what a transistor is, I will not bother to explain it in great depth. This document focuses directly on the software layer. I may write up a guide to computing electronics at a later date but for now, a simple explanation will suffice.
> A transistor is an electronic component that takes two inputs and gives an output based off them. It does this through the use of semiconductors. The two inputs are labeled 'collector' and 'base'. The collector has continuous current passed into it however it is unable to reach to 'emitter' which is the output of the transistor. However, when the base is powered it allows the current to jump to the emitter. 

I will not show the physical implementations for all the logic gates here, rather, I will simply list the key ones.

| GATE | Number of inputs      | Description |
| ---- | --------------------- | ----------- |
| AND  | 2                     | Output is true if both inputs (bits) are true (on) |
| NAND | 2                     | Output is false if both inputs are true |
| NOT  | 1                     | Output is true if input is false |
| OR   | 2                     | Output is true if one or both inputs is true |
| XOR  | 2                     | Output is true if only one input is true |
| NOR  | 2                     | Output is true is both inputs are false |
| XNOR | 2                     | Output is true if both inputs are equal |

From just 7 gates we are able to create any circuit necessary for a turing complete machine.

## Level 1: Counting and Numbers
Remember how I mentioned that 8 bits make a byte, well that is because 8 bits were found to be the minimum size necessary to convey useful information. Early computers could store small numbers, characters and boolean values in this space (Although strictly speaking a bool can be represented in a single bit) and it quickly became the standard minimum unit of addressable memory from CPU manufacturers. This means it is impossible to use anything less than one byte to store any data. What does this have to do with counting? It all comes back to the distinction between a 'binary system' and 'binary counting'. If binary is the first layer of abstraction from pure electronics, then our ability to assign meaning to a collection of binary values is the second layer.  

#### ASIDE: Type definitions
As we begin to introduce more types of data, I will begin to reference them by specific names. We will explain why 'typing' is important later but for now, just acknowledge the following types.
**INT:** Short for integer. Pretty self-explanatory
**CHAR:** Short for a character. It contains a simple character of text.
**FLOAT:** Short for floating point integer. Essentially a decimal
**BOOL:** Short for boolean. Stores a true/false value.
**String:** Essentially just a sentence or collection of chars.

The binary counting system is just another representation of numbers, but in 'base 2'. It often seems confusing or daunting when trying to understand a new counting system but in reality, if we look back to our primary school education, it becomes a lot simpler. Let us start by dissecting base 10 or 'our' number system. 

Place values is really the key here. Remember the 'ones, tens, and hundreds' columns that seemed so pointless, well you better appreciate primary school because those columns are really what number systems are all about. Lets look at this table:

| 10000000's | 1000000's | 100000's | 10000's | 1000's | 100's | 10's | 1's |
| ---------- | --------- | -------- | ------- | ------ | ----- |----- | --- |
|           0|          0|         0|        0|       0|      0|     0|    0|

We are instantly able to tell that this number is 0, but the full representation here is actually written `00000000`. Now obviously we know that we do not need to write all the extra zeroes but it is important to realize that both representations are correct because when writing bytes, we don't drop extra zeroes. If you are particularly astute, you may have noticed an additional pattern:

| 10^7 | 10^6 | 10^5 | 10^4 | 10^3 | 10^2 | 10^1 | 10^0 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|     0|     0|     0|     0|     0|     0|     0|     0|

This is why we call our system 'base 10'; Each column has the base of 10 to an incremented index. This is what gives us place value. Additionally, there are 10 numbers in our counting system [0,1,2,3,4,5,6,7,8,9], which is why we use the base of 10. The other key component of counting with this system is 'carrying'. Whenever we want to increase the value of a column that already has the max value (9), we simply write zero in that column and add one to the next. When said in words:
> I add 9 to the 'ones' column. I wish to add an additional 1, make 10 in total. I now have 1 ten, and 0 ones.

This system works identically to any other base system. The power table for binary look like the following (recall that there is only 2 digits in binary and therefore is base 2):

| 2^7 | 2^6 | 2^5 | 2^4 | 10^3 | 2^2 | 2^1 | 2^0 |
| --- | --- | --- | --- | ---- | --- | --- | --- |
|    0|    0|    0|    0|     0|    0|    0|    0|

Or:

| 128's | 64's | 32's | 16's | 8's | 4's | 2's | 1's |
| ----- | ---- | ---- | ---- | --- | --- | --- | --- |
|      0|     0|     0|     0|    0|    0|    0|    0|

Now carrying every time we hit 1, instead of 9. You'll note that there are 8 columns above, which is exactly the same amount of bits needed for a byte and because each column can hold only one of two values, we can use a bit to represent them. A key limitation of this system is that it requires much more space to write large numbers. In base 10, the 8th column is worth 10 million, in binary it is worth a meager 128. This does not really matter though as we have plenty of bytes available to us in memory (In modern machines commonly up to 137438953472 of them). DO remember that we are essentially forced to use base 2 as our Turing machines can only handle ON/OFF states. We have now completed the second layer of abstraction, prescribing meaning to a collection of bits. Let's do a simple example of binary counting to test our knowledge:

<details><summary>What is the base 10 equivalent for binary number `00000110`?</summary>
<p>

### 6

| 128's | 64's | 32's | 16's | 8's | 4's | 2's | 1's |
| ----- | ---- | ---- | ---- | --- | --- | --- | --- |
|      0|     0|     0|     0|    0|    1|    1|    0|

`(0*128) + (0*64) + (0*32) + (0*16) + (0*8) + (1*4) + (1*2) + (0*1) = 6`

</p>
</details>

#### ASIDE: Signing numbers & Maximum values
So far our examples have consisted of one-byte unsigned integers with maximum value 255, this is a completely theoretical data type and is in practice more analogous to the char data type. 'one byte unsigned integer' may sound like a mouth full so let's break it down.

We can tell something is one byte by counting the number of bits in it. One byte is 8 bits, therefore `NumberOfBits/4 = NumberOfBytes`. If we count our above examples we can see there are 8 bits, 1 byte. Now, how about the 'unsigned' part. Unsigned simply means that the number contains no sign (+/-), it simply exists as a magnitude. There are important implications for unsigned integers as they have a significantly different range of values. The maximum value for one-byte unsigned ints is 255, the maximum value for a signed int is 127. Why? It has to do with the way which we represent sign in memory.

As we saw earlier, one-byte unsigned ints look like the following: `00000000`. The whole byte is used for storing the number, but what happens when we need negatives. Easy, just reserve the first bit as the sign: 1 = negative, 0 = positive, uhhhh not quite though. This approach allows for negative and positive zero, which would break logic gates (`10000000` and `00000000` are not the same yet they would both be considered 0..?). So instead, we use _2's compliment_, This method _does count 0 as being positive_, but that does not break maths so its fine. Two's complement can be calculated by simply flipping the bits and adding one:
`00000110` (+6) gets flipped to become `11111001` then we add '1' > `11111010` (-6).
**NOTE:** The first bit in signed ints is still reserved to denote sign. 0 = positive, 1 = negative.
It is good to realize that signed ints have the same range of numbers as their equivalent unsigned int however their max value is much lower. This is because we reserve the first bit (with place value 128) for the sign, effectively reducing the maximum possible value by 128. These two ints, however, _do_ maintain the same range as unsigned ints can go from -128 to +127 the range, therefore, being 255

#### ASIDE: Counting from zero
Due to the nature of binary, it has become standard practice in computing to count from zero. Instead of 1, 2, 3.. we get 0, 1, 2...
Hence the 1st item comes second as we start with the 0th item.

## Layer 2: Text and Typecasting
Now that we have a number system in place, we can move on to abstracting more types of data on top of them. So far, we have not actually done any real software work, an instead just given meaning to random arrangements of ON/OFF messages. This is basically the key to abstraction, simplifying finding easier and easier ways to comprehend things. 

Consider the natural numbers. They map very conveniently to infinite sets. We can now choose to represent an item from a set simply by recording the position of that item in its set. This only requires one thing to work effectively, an ordered standard from which to match positions. 

One early example of these standards was the ASCII standard. ASCII stands for 'American Standard Code for Information Interchange' and was the first standardized character set. Now we could simply use numbers to represent a letter, and then just match those numbers against the ASCII standard. Remember those 1-byte unsigned ints from before? Well, they have 256 possible values, which was more than enough for every character in existence at the time (computers only targeted US/UK markets). In fact, representing letters and characters using a 1 byte unsigned int became so common that we starting calling that data type a 'char'.

Another example of abstraction on top of numbers is the RGB colour standard. RGB stands for Red-Green-Blue and directly correlates to the way digital screen show colour. Instead of having to memorize weird binary values for any colour we need, we can simply use RGB. RGB values have one byte of data per channel, meaning that we can give values up to 255 for each channel. This makes it incredibly easy to 'mix' colours. 

#### ASIDE: The byte boundary
Due to the design of computing architectures and RAM, it is wise to keep data inside byte boundaries, which are essentially theoretical walls between each segment of data. They occur every 2^n bytes, meaning that data types should fill 1, 2, 4, 8 or 16.. etc bytes of data. Since RGB is only 3 bytes (One byte per channel), it is often a convention to add a 'padding' byte to make the RGB data structure a total of 4 bytes.

It is interesting to see how far we have come. We are now able to say something like [A=1, B=2, C=3... etc] and then use a collection of numbers to represent words. However, we are actually using base-2 to represent those numbers, and our base-2 is in fact represented in binary, which in turn represents the electronic flow. 

If the following is a representation of some 'toy' RAM (Each new line is a byte boundary):
```
0000 0000 0000 0000 0000 0000 0000 0000 |
0000 0000 0000 0000 0000 0000 0000 0000 |
0000 0000 0000 0000 0000 0000 0000 0000 |
0000 0000 0000 0000 0000 0000 0000 0000 |
```
If we were to place three RGB values without adding into this memory it would now look like:
```
0110 1100 0001 1110 1011 1100 0110 1100 |
0001 1110 1011 1100 0100 1111 1000 1100 |
0100 1110 0000 0000 0000 0000 0000 0000 |
0000 0000 0000 0000 0000 0000 0000 0000 |
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
There are a few different layers throughout this, that, whilst minor and unimportant, can be very convenient. One such layer would be hexadecimal (hex for short). I will not elaborate on how it works as I would like to think my explanation of binary earlier was sufficient to use for other systems. Hex is base-16 and therefore consisting of 16 digits. These digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F; F having the value of 15. Hex is useful because the max value for a nybble (a half-byte or 4 bits: `0000`) is 15. This means we can represent one byte of data with just two hex digits. We represent hex with the prefix `0x` or `#` so it is clear what number format we are using. (binary gets prefixed with 0b or suffixed with b).

Example: If we wanted the colour white as an RGB value (white is the max of all colours), we would write something like:
```c
//This is pseudo code
WhiteColour = (255, 255, 255)
```
Whilst that doesn't really seem like a hassle, it can still be simplified. Since we know that two hex digits map perfectly to a byte and that there are three bytes of value in RGB, we can represent any colour with just 6 digits. Furthermore, because we know that each byte is going to be represented by two digits we eliminate the need for comma's and brackets as they are implicit between the fixed width hex bytes.
```c
WhiteColour = 0xFFFFFF
```

##### ASIDE: Encoding standards
ASCII was indeed sufficient for early systems and covered enough characters to be useful, however useful is not the same thing as adequate. Soon enough the original ASCII spec became too dated and missed many important characters both from the UK/US character set as well as those from other countries. Most modern systems now use Unicode for their text encoding. Unicode includes a much greater character mapping including the entire ASCII spec, Emoji, Every emergency symbol, Binary Digits and the symbols of virtually every language in the world. This means that modern programming languages usually define the char data type as being 16 bits (2 bytes instead of 1). 2 bytes of unsigned data is enough to represent 65,536 characters. For some very specific encodings, it may be necessary to use a 32-bit integer.

## Where to next..?
We have now covered most of the super basic stuff and it leaves us with a few choices. There are no clear and obvious paths from here as we can take the abstractions in any direction. I believe the best choice going forward to examine abstractions in programming. Building from our base of numbers and letters, we will begin to move away from binary operations and begin to look at the advent of programming as it is known today. But before we get moving, we must discuss some new concepts.

As of this point, the only hardware component we have touched on is RAM. Whilst RAM is important, but not the only necessary. To program, we need a machine that is Turing complete, one that can not only store data but make decisions too. This is where those bitwise logic operators (logic gates) that I mentioned early on come important. As electronic current flows from the RAM, it enters the CPU. The CPU is not smart, it is not wise. In fact, the CPU is what makes our simple machines into real computers. It does this using billions of transistors (up to 6 billion in our phone CPUs, 19 billion in an i7 8700k) and millions of logic gates (AND, NAND, OR etc). As electricity hits the CPU, the transistors go to work flipping like a factory full of switch meddling monkeys. These switches eventually convert the input to output, which can then be stored in RAM or hard storage. Of course, as with everything, there is wayyyyy more depth surrounding the implementation of CPUs, especially modern ones. However, due to the complex and messy nature of such technical proceedings and my admittedly limited knowledge in certain edge scenarios, I will not endeavor to explain them.

For the next part of our journey, we will have to assume and skip some things. As I said in the intro, I do not intend to explain hardware implementation as I find the prospect positively mind-numbing. As a result are to assume that somewhere along the line the necessary equipment to interface with the machine has been developed (Punch cards, Keyboard, Digital Storage, Monitors.. etc). I will also assume that you have experienced at least limited interaction with programming.

We will skip level 3 as it consists of early operating systems. These early systems were not important as they only provided the ability to use file systems and save data and programs as well as navigate these folders of data.

## Level 4: Assembly Language
At some point (although I'm not sure when) there was a conceptual leap in programming. Originally you had to write code in binary or hex, literally considering every transistor's interaction to get the desired output. If you are masochistic and wish to experience the pain of existence caused by being a programmer in this time, try to master boolean algebra. The leap occurred with the emergence of Assembly Language, Assembler Language or ASM (They are all the same thing). Assembly is the lowest level programming language and literally relied on the manual allocation of memory, meaning the programmer had to specifically specify where bytes should be placed and when. It was god awful, but still greatly better than binary or hex.  It was made even more annoying considering that every brand of CPU had their own version of ASM. Whenever you wrote some assembly code, you would have to put it through an 'assembler', which was an early attempt at a compiler written in hex. The assembler would then convert the ASM into machine code (see aside below) using twisted and perverse methods only an evil sociopath could fully comprehend. ASM is now considered so low level that it is essentially thought of as binary: So limited and basic that the CPU can just understand it (Although it's not true, it still has to be put through an assembler before it can be run)

#### ASIDE: Machine code
Machine code is just plain binary information. The only difference between the binary we were looking at earlier and machine code, is that we have the intention of 'running' machine code. The goal of machine code is to be used to actually execute actions and be run through the CPU, the purpose of our simply data types was just to exist and represent data. Try this analogy: Whilst a dictionary and Spoken language are both defined using the same set of words, a dictionary purely exists to reference and define information, spoken language allows us to express ideas and convey instructions. Binary is the words, RAM and basic data is the dictionary, and machine code is the spoken part.

#### ASIDE: Too much?
If this last little bit has made you feel like we jumped a little bit too far, read the following for a much more in-depth explanation.

When computers were new they had very, very limited processors. So simple that is was very conceivable that one person could fully understand the entire chip. To write programs, you had to specifically lay out what individual charges need to occur in what order. If you knew the system well enough you would be capable of manipulating the order in which switches flip. When a switch flipped it would redirect current allowing different switches to then flip, eventually culminating in an output. It's sort of like a huge Redstone circuit. If you've ever made a Redstone lock, you have made a tiny processor; By manipulating certain inputs it computes the desired output, the door opening. Most operating systems provided basic functionality. Normally if you wanted to add two numbers, you'd have to write manual code for activating the adder circuit in a processor, but with an operating system, you'd just have to write some binary to interact with the OS and ask it to add the numbers instead. Modern operating systems are not responsible for such simple tasks anymore and instead deal with more complex things like graphics drivers. 

After establishing enough basic binary code, you were able to write more binary that used the stuff that was already written to do even more stuff. This in itself is a small layer of localized abstraction, hiding away the low-level machine code and using it to build more complex routines. This is a pattern that is familiar to all programming languages. Eventually, the binary code base got sufficiently large to take in an input stream of characters and turn them into more machine code. This was the true birth of Assembly. Eventually, we get so abstracted that compilers don't even bother compiling to machine code, they just compile to assembly and let the operating system do the rest.

## Level 5: The compiler and early programming languages
Assembly was a world faster to write than binary or hex code. It allowed for much more rapid development. For example the addition of two integers in binary looks like the following:
```c
Location Hex     Instruction Code Binary     Instruction Code Hex     Instruction     Comments
100              0010 0001 0000 0100         0x2104                   LDA 104         Load first operand into AC
101              0001 0001 0000 0101         0x1105                   ADD 105         Add second operand to AC
102              0011 0001 0000 0110         0x3106                   STA 106         Store sum in location 106
103              0111 0000 0000 0001         0x7001                   HLT             Halt computer
```
**NOTE:** All text in the above example was just to make the binary semi-readable to programmers of the time. The 'instruction code binary or hex' is what would have actually been written.

This same operation in assembly (specifically in Intel's IA-32 asm) look like the following:
```asm
leal 0x33333333, %ac
addb $-126,%ac
```
Even if you barely understand the above examples (Don't worry I only just grasp it) you can probably see that ASM code is much, much, more concise. But it wasn't perfect. It still required 50 lines of code to effectively multiply two digits, although you could define subroutines to make this easier.

As soon as programmers got their hands in ASM they began to work on new programming concepts. The problem was, not many of them cared to advance languages. Enter: Grace Hopper. Grace Hopper rarely got the credit she was due. She was the pioneer of compiler theory and actually developed one of the first programming language specs. Her concept involved a program, much like an assembler, that took an input stream of characters or text (Remember that we can define characters using binary and store that binary in files) and spat out a machine code version. The major difference is that whilst assembly just converted English instructions to machine instructions, FLOW-MATIC, and her compiler would add another layer of abstraction. You see, in the examples above the instructions are identical. You still have to Reference variables locations directly from RAM, and you have to manually push them to the CPU. Hopper saw this hassle as unnecessary and distracting from the important things. The FLOW-MATIC compiler would do something radical: It would abstract away hardware manipulation, letting the programmer get straight to business. The FlOW-MATIC compiler would be able to read:
```c
__start:
    SOME_VARIABLE = 5
    ADD(4, SOME_VARIABLE)
```
And convert it to:
```asm
push 0x05, 0x33333333
leal 0x33333333, %ac
addb $4,%ac
```
This was such a cool idea. Instead of just translating the same instructions to a different form, FLOW-MATIC would actually work out the required instructions. For another language based analogy: I want to be able to translate my book into Spanish. I hire a translator to read through my book and translate it literally to Spanish. It sells well so I decided to write another. I can't be bothered dealing with grammar and words this time though, so I just draw a collection of pictures instead, and let the translator work out the details. The assembler is like the translator with the first book, directly copying the meaning. The FLOW-MATIC concept compiler was supposed to work more like the second, inferring meaning and taking care of all the hard, boring and downright repetitive stuff. The other main advantage that Hopper's compiler had was that it compiled to assembly, not binary. Because of this, you could set up the compiler to compile to any form of ASM (Remember that each CPU brand had their own form). For the first time ever, we were able to have a cross-platform language. All you had to do was just change the compile target. Wanted to run on IBM machines? Target BAL-ASM. Want to run on PowerPC machines? Target IBM-ALP-ASM.

The first language to really implement a compiler and surpass assembly code effectively was FORTRAN (Don't ask me why the naming convention for languages seemingly meant you had to capitalize). Fortran was a really good language, and I mean really good, compared to assembly. The design team took all of their cues from Hopper and ended up with a language which could understand the following:
```fortran
Integer :: a, b, c
a = 3
b = 4
c = a + b
```
It could even handle exponentials (which would be several hundred lines of assembly):
```fortran
c = a**b ! A to the power of B
```
From this point on languages began to come out of the woodwork. COBOL, LISP (Inspired python), SmallTalk (Inspired C++, Java and C#), ALGOL, SAGE, Pascal and BASIC all became very popular. There was calm in the world of computer science, then a knock on the door... it was C.

## Level 6: The rise of C
The coming of C resulted in one of the biggest mass genocides this world has ever witnessed. It came and ruled with an iron fist, all but smiting any language that stood in its way. C was a language so revolutionary, so powerful, it is still considered a first-class language today. C was the first modern language (It was developed over 46 years ago). 

But why is it so good. What makes it deserving of its own layer of abstraction. Well to put it shortly, C is the king of abstraction. You see, languages up until this point were very procedural in nature. This meant that the language had a predefined set of features it could do, and that was that. C was better, C let you do whatever you wanted to do. This is because C allowed you to directly write binary and manipulate memory at a bit level, it let you do everything that assembly let you do (You could even embed ASM directly into a C program) whilst also being able to do everything that all the other high-level languages could do combined. It was this flexibility combined with the crazy speed that C posses that allowed you to write everything from video games to whole operating systems in it. C could run on any machine, even tiny microprocessors. It truly was and still is an incredible language. No other language gives you as much power as C (Except for maybe C++). 

It achieved all this by allowing the user to define their own data structures - Custom collections of basic data types used to represent a single coherent 'object'. Unlike almost every language up to this point, C did not make users use its own types of data. It let the user invent new rules and modify everything and anything. This meant that C literally let you define your own abstractions. It was the first language to majorly break the procedural flow from previous languages (More on this later).

#### ASIDE: Defining a the modern language
C was the first language to propose a semantic and unified syntax for its langauge. Almost every language written since C uses elements of its syntax. It was one of the earliest languages to use the brackets and braces method for scope limiting. It also introduced a lot of new ideas and concepts which are considered as common place in languages these days.

#### ASIDE: The power of C
So far I've been proclaiming the power of C without giving any real evidence. To give you some examples for how usefull C is, here is a list of project implemented in C/C++:
- The Linux Kernal
- The Windows kernal
- The Unix kernal (Used in most early operating systems and still in use for some versions of linux and MacOS)
- Google Chrome
- GNU Unix (A full operating system based on UNIX written by GNU Computing)
- The python interpreter
- Most programming languages
- PostGreSQL, NoSQL, MySQL - SOme of the most popular databases in the world
- Robotics and embedded systems
- The majority of the internet

#### ASIDE: Flavours of C
C was so revolutionary that it casued a wave of subsets. These variants of C were developed by teams of developers looking for specific additional funnctionalility from the C language. The most notable of these variants is, of course, C++. C++ made C a much more usable language. It was easier to seperate code out to individual files and it made working in team projects easier. C++ has become so ubiquitous that its more or less synonymous to 'C'. There are of course a few other notable variants too:
- Objective-C (Used to program Apps for Apple devices)
- ANSI C
- C-- (A compiler target for high level languages)

If you inlcude langauges written in C, using the C compiler, or are feature derived from C you get:
- JavaScript
- Python
- Java
- C++
- Dart
- Go
- PHP
- Visual Basic
- Perl
- R
- MATLAB
- Swift
- Lua
- Some forms of LISP
- Rust
- Erlang
- Elixir
- C-Shell
- Clojure
- Kotlin

And those are just the major ones!! Small hobby languages are not included here. Hopefully I can eventually implement [LoopDeeDoo](https://github.com/LetsCode-Angus/LoopDeeDoo) in C.

## Layer 7: Introducing the Virtual Machine
C was such a great language that it immediately inspired programmers of the world to look for the next big thing. Various other languages came and went, each with their own new set of features, but none of them ever _stuck_ as well as C did. That was until Sun Microsystems came out with Java.

Java followed after C in that it was Object Oriented in nature. It was fairly fast and very flexible. Aside from being slightly simpler than C, Java only had one advantage - It's virtual Runtime.

Remember the 'compiler', a type of program first conceptualized by Grace Hopper. It was the compiler's job to transform input text (code) to output machine code (binary) in a fast and performant way. This model of running code had been the sole method for quite some time now, and Java decided to change it up. Sun Microsystems wanted to go a layer further. Instead of recompiling to each and every different platform you wanted to run on, why couldn't you just compile once, run everywhere? The team at Sun Micro put their heads together and designed something awesome - The virtual machine.

Lets take a step back for a second and have a look at our old friend the compiler. We can recall that the compiler worked by reading an input of some 'code' and acting as translater in order to output machine friendly assembly code. This is quite a simple concept hwoever in practice it can get very messy [LINK TO COMPILER ARCHITECTURE]. The team at Sun theorised that if you a machine could run native machine code, then what was stopping someone from writing a virtual machine program that could run native Java code. They thought that if they could write a program that emulated a simple operating system, then you would be able to compile that program to run on any other opearting system. With this new virtual operating system they could then write code directly aimed at this fake system and run it. This means when you write a program in Java it was compiled to run inside a program which had been preinstalled on all computers. This way you could indeed compile once and run anywhere. 

With this new idea about virtual machines in mind, Sun Microsystems began to implement the first version. The final product was named Java Virtual Machine or JVM for short. JVM was compiled to run on all the main operating systems of the day. JVM simulated a fully fledged computer and ran programs that were written in Java Bytecode. Now all that was left to do was write a compiler to compile from java source code to JVM's bytecode. Once a program was compiled to Java bytecode it could run on any computer that had the Java Virtual Machine installed on it. If this concept sounds a little confusing it is best illustrated by a diagram:

![Diagram of JVM](http://net-informations.com/java/intro/img/java-virtual-machine.png)

But we are not done here, no not at all. For after the virtual machine came the rise of the interpreter.

## Layer 8: The interpreter
The Java virtual machine was revolutionary in the way it inspired new thinking about old problems. It proposed a brilliant solution to the problem of 'portable code', or code which could be run any where. This new felxibility allowed programers to focus on solving the problems at hand rather than writing machine specific code for forty-seven different operating systems, but it was not to be the final solution. Java was not without it's problems. The virtual machine was big, complex, and confusing. This meant it was slow and difficult to add new features or fix bugs. Not to mention that it was entirely unmoddable. These frustrations led to a few developers looking for a new, better method. The main problem was not that you had to use a clunky virtual machine, but rather that the virtual machine was extremely heavy weight for simple tasks. How could coders get the benefits of 'Code once, Run anywhere' without any of the incovenience of having to write an entire vitual machine? The answer was the interpreter

The interpreter worked similarly to the virutal machine in that it was a program used to run other programs, but with one key difference... It skipped the compilation stage. Instead of compiling code which could then be run on a hulking virtual machine, languages with an interpreter could run directly from the source code. The way this worked is rather genius. The interpreter would read in the source code and decide what it meant on the fly. There are a number of key differences and trade-offs between an interpreted language and a compiled one, and I find that these are best described through a simple analogy.
> An author writes a book in english which recieves much critical acclaim.
> In a different country someone wants to read the book to see what all of the fuss is about. They can't as they do not know english. They now have two options. They can request to have the book formally translated. On one hand an official translation will be perfect and without error. If they ever want to read the book again they can simply pick it back up and immediately read it. On the other hand an official translation will likely take months to resolve. The second option is to hire a translater to read it and live translate the text to them. This would be very quick to resolve, but would be very to slow to read as they would have to wait for the translator to read and translate each indiviual line, and when they wanted to read the book again they would have to re hire the translator. Those are the options. Wait a long time for the book to be ready for convenience and speed in the long term or hire a translator for instant pay off in exchange for speed and efficiency.
The compiler is the offical trnalation, it takes it's time to translate code to a machine language, but when done the code runs quite fast. We'd also need a different offical trnalstion for every langauge, which adds even more time. The inpreter is the live translator, they are quick and conveniant to access and you can get them pretty much everywhere, but they are slow and make mistakes.

