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
The example Turing came up with involved a long strip of material devided into equal sections. The 
