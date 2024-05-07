# Procedure
## Create elements.csv
A list of all periodic element symbols, sorted alphabetically. An '_' is appended to symbols with only one letter.
1. A csv file containing data about elements was downloaded from https://gist.github.com/GoodmanSciences/c2dd862cd38f21b0ad36b8f96b4bf1ee. NOTE: The comments on the file point out a few errors, however none of which concern the symbols themselves.
2. Original csv file was opened in Libre Calc and the 'symbols' column was copied into an empty text file.
3. 'format.py' was ran against text file to apply proper formatting.
4. Text file was overwritten by the output of step 3.

## Algorithm
1. Read $ELEMENTS from 'elements.csv'.
2. Get $INPUT from user.

3. Convert $INPUT into $WORD:
Each char in $INPUT is expanded into four chars. The first two chars represent whether the char by itself is a valid symbol. The second two represent whether the current char and the next char together are valid symbols.

How each part is expanded is determined by the following rules:
Let "A" be the current char being examined.
Let "B" be the next char in $INPUT.
Let "E" be the expansion, which is appended to $WORD.

if A is valid: E = "A_"
else:          E = "A*"
if AB is valid: E = "AB"
else:           E = "00"

So the string "the" is expanded like so:
    1. 't' is not valid, so its expanded to "t*".
    2. 'th' is valid, and is expanded to "th".
$WORD = "t*th"
    3. 'h' is valid, and is expanded as "h_".
    4. "he" is valid, and is expanded as "he".
$WORD = "t*thh_he"
    5. 'e' is not valid, and is expanded as "e*".
    6. 'e ' is not valid, and is expanded to "00".
$WORD = "t*thh_hee*00"
    7. '00' is prepended to $WORD.
$WORD = "00t*thh_hee*00"

4. Iterate over $WORD and determine which symbols will be used.
Consider the $INPUT "thermodynamics". This word can be spelled completely by only using valid symbols.

After the expansion step, $WORD = "00t*thh_hee*err*00m*mod*dyy_00a*amm*00i_00c_css_00"

For each step, the program looks at a slice/window of 6 chars, which represent the valid symbols of when letter. E.g. for the letter "t" above, the program would look at "00t*th". The latter four chars are the expansion of "t" from the previous step, and the first two are whether the previous letter and "t" are valid.

This slice can be thought of as three boolean values:
0  0  1   = $W
00 t* th

If $W is 100 | 010 | 001, the only valid symbol is set. 
    If $W is 001, skip the next iteration.
Elif $W is 011 | 000, advance to the next iteration.
Elif $W is 110
Elif $W is 101 | 111

5. Cleanup and output $WORD
    - Remove '0' and '_'
    - Use '*' to parse which letters could not be used.
    - Differentiate between valid symbols and unused letters.

## Potential Problems
### Problem: What happens if the program finishes its first iteration and some letters are unclaimed, i.e. some windows have 2-3 true values. What's the minimum necessary iterations?
If a window has 2+ trues, the previous window must either also be 2+ trues, 000, 100, or 010 
This is recursive, where 000, 100, or 010 are the base cases. 

W0 = {000, 100, 010}
W1 = {011} 
W2 = {100, 101, 110, 111}
W3 = {000 - 111}
If we wait for W3+, we'd have to iterate backwards to affect W1, or find a similar workaround. Therefore, ideally W2 should fix it.

If W2 = 100 -> No extra behavior needed.
      = 110 -> W3 does not rely on any letters needed by W2.
      = 1?1 -> W3 has same range of possible values as W2.
               W3 might need a value from W2, iff W3 = 100

Therefore:
In the first 2 cases:
0123456
011     001     CLR(0,1)           
  1?0     100   SET(2), CLR(3,4)   
    0??     0??                    

3rd case, W3 needs #4
0123456
011      010     SET(1), CLR(0,2)                  
  1?1      001   SET(4), CLR(2,3), CLR(5,6)
    100      100                                        

4rd case, W3 doesn't need #4
0123456
011      001    SET(2), CLR(0,1), CLR(3,4)
  1?1      100                                         
    1??      0??                                       

~~Therefore, the program should be able to do this in one pass.~~
The current window does not have a method to differentiate between cases 3 and 4.
So the algorithm will likely have to iterate twice to find the solution.

### Problem: Can the same letter be claimed twice?
This should be impossible by definition.

When a letter is claimed, 2 bits/4 chars are cleared on either side.
Given $INPUT = ...PCN..., can C be claimed twice?
P_ PC C_ CN N_
0123456
001    001     SET(2)         
  101    100   CLR(3,4)    
    100    000

0123456
001      001    SET(2)         
  101      100  CLR(3,4)  
    110      010               

### Problem: Do middle bits have too much reach.
0123456
010      010    SET(1)         
  010      000  CLR(2,3)
    010      010                
Answer: Yes

If 001 => SET(2), CLR(0,1), CLR(3,4)
   010 => SET(1), CLR(0),   CLR(2)
   100 => SET(4), CLR(2,3), CLR(5,6)

## Testing
Creating an adequate suite of tests requires two things:
1. A wide range of inputs.
2. The correct answers to each of those inputs.

To simplify things, each input will be 4 character string. This may seem low, but since each character can only directly affect up to 2 chars away, strings longer than 3 chars hopefully can be treated as multiple units chained together. The extra char is to provide a buffer, just in case this assumption is not safe.

A 4 character input will be converted into a byte (the leading padding digit is always 0 and can be ignored for this purpose). This means that all possible inputs can be covered by mapping each binary digit onto a valid element string. 

Rather than create these test inputs by hand, a decision tree style algorithm can be used. However, with this method, care must be taken to keep this process simple enough to not need its own separate testing suite.

### Decision Tree
Each bit in the input can be thought of as the answer to a simple yes-or-no question. The tree alternates between two different questions:
1. Is the previous char a valid symbol on its own?
2. Is the previous char and the next char together a valid symbol?

Each node receives a list of all currently valid strings and knows which question it is asking. 

Files involved in producing this decision tree and parsing its test cases are kept in 'testing/'. The output of 'decision-tree.py' was ran using 'python3 decision-tree.py | tee log'. Each leaf in the resulting tree had several valid input strings. The 'log' file contains all valid solutions, while 'test-cases.txt' contains one randomly selected solution per leaf.

### Best Valid Output
While the decision tree should provide a valid answer to each of its valid_words, this isn't guaranteed to be the best solution. 

Potential Solution Finders:
- Brute force: Find every potential solution for each test case and select the one(s) with the least invalid letters.

A four char string has 5 potential combinations which could exist:
ABCD = { AbCd, AbCD, ABcD, ABCd, ABCD }
NOTE: These symbols are written in typical periodic symbol formatting, so Ab is one symbol and AB is two.

1. Generate 5 cases per test case.
2. Find number of invalid chars.
3. Select solution with least invalid chars.

Solutions are stored in 'solutions.txt'.
