# Parsing and Pre-Proccessing 
***
A fundamental concept in computer science is the idea of lexing and parsing. These two patterns are itegral to a number of things including compiling, transcribing, translating and data reading. All of these projects would involve the Parser & Lexer pattern.

## Language pre-processor
Take a basic language such as python or JavaScript and design some simple changes you want to make to it. Then write a pre-proccesor which translates your version of the language to the actual standard. 

An example of a simple pre-proccessor might translate this:
```C#
class Example {
	public Example(int i) {
		// Constructor
  	}
	
	// Rest of the class
}
```
To the more python-like:
```Python
class Example(int i){}:
	# Rest of the class
```

## Custom object notation
Write a simple object notation language such as JSON or XML which can then be read and transformed into an object.
This notation may look like this:
```text
# AnObject #
{
	i = 333
	str = "string data"
	array = [1,2,3,4,5]
}
```

## Custom runtime interpreter
Implement a custom scripting language and write an interpreter for it. These almost always follow the parser-lexer pattern where an input stream of characters get converted to 'tokens' and then get parsed. Often these interpreters act as virtual machines sharing their memory space with the executing script. Vassili Kaplan has a number of decent articles about [this](https://msdn.microsoft.com/en-us/magazine/mt632273.aspx). This works well in conjucntion with [shell projects](./Shell.md)

## The parser and lexer pattern
The parser and lexer pattern is the most common approach to proccessing source file. The lexer takes care of reading an input stream of characters and turns them into a 'token'. A token is a representation of a code symbol. A code symbol is any keyword or phrase used in code. Typically tokens are represented using simple data structures, strings or enums. An example might be:
```C#
int i = 3;
```
would be lexed to:
```
TYPE int
IDENTIFIER i
OPERATOR ASSIGNMENT
LITERAL 3
```