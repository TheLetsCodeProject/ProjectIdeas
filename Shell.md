# Custom shell implementations
***
## Command line parser
A small program that can parse text commands like `test myCommand 66` and result in execution of a function or program. The architecture for this program would exist in the form of a console application and would likely require an expression string to an intermidate form of some kind before geting handed of to some function executer. The most basic form of this program would act as a wrapper for cmd or would store a dictionary which matched functions to strings. A good article to read on this topic can be found on [code project](https://www.codeproject.com/Articles/816301/Csharp-Building-a-Useful-Extensible-NET-Console-Ap#Main)

## Custom runtime interpreter
Implement a custom scripting language and write an interpreter for it. These almost always follow the parser-lexer pattern where an input stream of characters get converted to 'tokens' and then get parsed. Often these interpreters act as virtual machines sharing their memory space with the executing script. Vassili Kaplan has a number of decent articles about [this](https://msdn.microsoft.com/en-us/magazine/mt632273.aspx) 

## Shell system.
This is similar to a command line parser in that it takes commands and does stuff with them however this should act more like its own operating system such as MS-DOS or UNIX. The architecture for this could be relatively simple. All that a basic program would need is a dictionary of alias which could be generated from a file at runtime. These aliases would link text commands to executable files which would be called as a child process from the shell. This is highly expansable as it means that users can simply write their own mini programs and link them with an alias. In fact alias itself would be a selfcontained program. A command would then simply follow the format `{alias} {arguments}` eg `ls ..`. IF we wanted to make this more complicated or advanced we could introduce output piping, which would take the result of one command and parse it into another program. If you had this capability you already have a basic scripting language. By adding a little more complexity we can add so much depth. Now we can have commands that run programs written in our own language which simply calls other programs.

### A more in depth review of the shell architecture.
Lets start be examining the command prompt (cmd). CMD is the command line interface for windows it features a number of inbuilt commands and is capable of recognising and calling other programs. An example of an inbuilt command is echo, which simply returns the given input: `echo hello world` prints "hello world". An example of a command whixh runs a program would be `notepad` which simply launches notepad.exe. For this to work properly, notepad must either be on the system PATH or be located in the System32 folder. These are the only two locations that cmd looks for programs outside of the current working directory. In unix or GNU based systems such as MacOS or Linux, these commands and programs get stored as aliases as well. 

So how does this advise our custom shell. Well, it doesnt really to much for us other than re-enforce what we already knew. The main take away is that we can maintain a list of internally recognised commands in additon to externally found. It does present us with an interesting decision. Do we use the GNU/UNIX aliasing approach or do we use the MS-DOS search locations method. The key difference is that in the unix method we must explicitly define programs that we can run, where as in DOS, we simply find them. Possibly the best approach is to combine both approaches. 

With this all said implementatiion now becomes somewhat trivial. We maintain an internal dictionary of commands which are matched with actions. When a new command is entered we first check that command against this internal dictionary, if the key is present we call the relevent function, otherwise we check our alias dictionary and run that program, parsing all relevent information to it. Finally if that also fails, we try look for the executable inside the current directory and in the root folder of our program.

It is important that we implement a system to change directories. We can change our current working directory by using `Directory.SetCurrentDirectory()` then we simply ensure that when we spawn a child proccess we set the `ProcessStartInfo.WorkingDirectory` to our current wd. 

<<<<<<< HEAD
The advantage to using this appraoch is that we can simply alias existing CLIs like Python37 to a simple string and then call them. Because of we set wd, it means python will automatically open in our desired location. If we have UseShellExecute == false in our ProcessStartInfo initialiser then the programs will also run inside eour current terminal.

### Example implementation
```C#
public static class Shell {
	static Dictionary<string, Action<string[]>> ShellCMD =
	new Dictionary<string, Action<string[]>>() 
	{
		{"pwd", Commands.PrintWorkingDirectory}
	};

	public static Run(){
		string input = null;
		do {
			Console.Write("$ ")
			input = Console.ReadLine();
			string[] command = input.Split(new char{' '});
			
			if(ShellCMD.ConatainsKey(command[0])) {
				ShellCMD.Invoke(command);
			}

		} while(input != "exit");
	}

}

public static class Commands {
	public static void PrintWorkingDirectory() {
		Console.WriteLine(Directory.GetCurrentDirectory());
	}
}
```
=======
The advantage to using this appraoch is that we can simply alias existing CLIs like Python37 to a simple string and then call them. Because of we set wd, it means python will automatically open in our desired location. If we have UseShellExecute == false in our ProcessStartInfo initialiser then the programs will also run inside our current terminal.
>>>>>>> ea9527fa49cc6b050e2bddf25ea139f6e0211db0
