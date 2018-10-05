# Understanding Digital Abstractions
You gotta start somewhere
***

If you are reading this you are probably already aware of the fundamental components of a computing system. RAM, CPU and SSD are all common vernacular these days. What you might not know, is why these components are important or how we use them to compute tasks.

## The turing machine
Before we go on, it is important we establish a definition for 'computer'. Its one of those words we all know, but maybe don't quite understand. As with any word. the meaning differs based on context. At its most basic, computer is a 'machine' or 'system' capable of computing simple boolean task. That is to say, a computer must be able to make yes or no decisions. This is a nice definition however it falls a little flat of what we're aiming for. You see, modern computers are able to make billions of yes/no decisions asyncronously. This is where 'The Turing Mcahine' definition comes in handy.

Alan Turing was a man born in 1912. Alongside breaking the enigma code and devising the now famous 'Turing Test', Turing is widely regarded as the father of computer science, his major contribution being the 'Turing Machine'. The turing machine is a hypothetical computer capable of meeting the following requirements:
1. It should be able to compute 'tasks' based on a given set of rules
2. It should posses a form of memory. This memory must be sufficeint to compute any given task.
3. The memory must be linear in fashion
4. The machine must have a way to jump to abitrary points in its memory.
The example Turing came up with involved a long strip of material devided into equal sections. Each section could either be 'ON' or 'OFF'. This strip would act as the memory. The machine would then be able to read through the strip and makes decisions based on the input. It would also be able to jump to random points further up or down the strip. It is interesting to think about this becasue, provided enough material, you would indeed satisfy all the above criterea. The ON/OFF system is what we are going to focus on from now on. Turing had proven that simple binary state was all that was needed to represent any form of data possible. A revelation considering that other computing models of the time consisted on different types of memory depenending on the data. This meant that letters, numbers and any other type of information would require new methods of memory, which is obviously pretty impractical. These models also had problems when it came to mixing different data types in computations. Suppose you wanted to count the number of times a given letter appeared in a word. The word would first need to be read from punch card memory and passed through a conversion unit before being read over and retranslated into cathode-ray-tube memory in numercial form. The Turing machine beat all of this as it provided a common language, Binary.

## Level 0: Binary
Binary truly is the first layer of abstraction in computing. It is ground zero, the begining of everything. A binary system is one that records only two types of data ON (1) or OFF (0). This is helpful as its very easy to represent ON/OFF electronically. Current = ON, No current = off. A single ON/OFF is called a bit, 8 bits make a byte, why choose eight? We'll get to that later. These bits and bytes are stored in RAM or Random Access Memory in the form of small electronic currents. For the time being, we will consider RAM to be the only way to store information. This is our binary model. Current flow represents 'bits' of binary data. This current flow is then stored in RAM so it can be used multiple times.

There is a key distinction between this 'binary system' and 'binary counting'. Binary counting is a numerical system with only two digits. This is an important destinction because we chose to base computers on a 'binary system' NOT on 'binary counting'. In our early computers, ON/OFF has no real meaning, it is simply a means to an end. This fact is important: The names ON/OFF are somewhat abitrary and meaningless, we (humans) could just as easily called these opposing states CAT/DOG. By themselves, bits are meaningless, but from a series of bits (ON/OFF messages), human's can prescribe meaning. This is why computers are not based on 'Binary counting'; Counting and using numbers is a meaning we can _prescribe_ to ON/OFF messages. Counting in binary is the second layer of abstraction.

### Alternate representations of binary
Throughout this guide I will generally use a numercial represenatation for binary. Instead of writing a byte like this `(ON)(OFF)(ON)(ON)(ON)(OFF)(OFF)(ON)` I will write `10111001` as it is much more succinct

# Level 1: Counting
Remember how I mentioned that 8 bits make a byte
