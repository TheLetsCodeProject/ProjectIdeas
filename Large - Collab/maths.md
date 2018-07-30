# Fully featured maths library
What fun!!!
***
## Concept
To complelety reaimplement a new and improved maths library. Ideally it would be able to handle anything from complex numbers to linear algebra and could consist of a numbers of sub libraries such as the standard maths library (sin, cos, tan, exp, log.. etc) and a library for doing coordinate geometry (distance, coord, vector.. etc). This library is a cool ideas because it is almost infinite in its expandability and, if done right, suits a large range of coding abilities (even people who can only write variables would be able to contribute). It could also support a large variety of languages such as C, C++ and C#

## Execution
To work on this project only minimal planning would be required. Most of it would simply consist of laying out ideas for things to implement, then researching how to do it. Eg; Reimplementing the Sin() function would require a little bit of research into how sinx is actually calculated. After a bit of digging I found this solution written in C:
```C
// C implementation of sin and cos (Uses standard GNU C lib)
float cos(float x){
	if( x < 0.0f ) 
		x = -x;
	while( M_PI < x ) // M_PI = Pi
		x -= M_2_PI; //M_2_PI double reciprocal of pi
	return 1.0f - (x*x/2.0f)*( 1.0f - (x*x/12.0f) * ( 1.0f - (x*x/30.0f) * (1.0f - x*x/56.0f )));
}
 
float sin(float x){return cos(x-M_PI_2);} // M_PI_2 double pi
// tan can be implemented using sinx/cosx = tanx
```
This could also be easily ported to C#. The above example shows a number of other things which would have to be implemented first such as a constants class:
```C#
public static class Constants {
        public static const double PI = 3.14159265358979;
}
```
Which could be coviniently be used with C#'s `using static`:
```C#
var circumference = 2 * Constants.PI * r;
// Becomes
var circumference = 2 * PI * r;
```
# Tags
***
#math #csharp #library
