# CollatzConjecturePatterns
Script displaying animated patterns based on Collatz Conjecture. You can choose between diffrent animations and coloring schemes. Script also allows you to change various properties via command line arguments (color, position, angle, size, etc.).
![demo image](examples/demo.png)
<br></br>
## What is the Collatz sequence?
You start with single positive number n. Each number in the sequence is based on the previous one. If the term is even the next one is half of that term. If it's odd next one is 3 times that term +1. Sequence ends when n = 1.

<pre>
n/2   if n is even
3n+1  if n is odd
</pre>

#### For example:
- 5,16,8,4,2,1
- 12,6,3,10,5,16,8,4,2,1

#### Actualy good explanation:
[Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture)  
[Numberphile](https://www.youtube.com/watch?v=5mFpVDpKX70)  
[Coding Train](https://www.youtube.com/watch?v=EYLWxwo1Ed8)

<br></br>
## Requirements
- PyGame  
`pip install pygame`

<br></br>
## How to run the script
Just do: `python collatz.py`  
It will run with default settings.

#### Command line arguments
**-a** Animation index. Int number from 0 to 4. Default is 0.  
**-s** Color scheme index. Int number from 0 to 8. Default is 0.  
**-l** Line length, size of pattern. Int number of pixels. Default is 6.  
**-d** Initial angle. Int/Float number of degrees. Default is 1.  
**-c** Colors used in some of schemes. Float from 0 to 1. Default is 1.  
**-f** Creates an image with currently displayed pattern when you close the window using **X** button. True or False. Default is False.  
**-x** x position of the pattern. Int number of pixels. Default is 100.  
**-y** y position of the pattern. Int number of pixels. Default is 350.  

#### Examples
- `python collatz.py -a 3 -d 90 -l 10 -x 350`  
- `python collatz.py -s 6`  
- `python collatz.py -a 1 -s 8`  
- `python collatz.py -a 3 -s 4 -c 0.95 -d 120 -l 15 -x 350`
- `python collatz.py -a 3 -s 2 -d 10 -x 350 -y 450`  
- `python collatz.py -s 6`  
- `python collatz.py -a 3 -s 8 -d 45 -l 10 -x 350` 
- `python collatz.py -a 1 -s 6 -l 20 -x 250`  
