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
- Each char in $INPUT is expanded into 4 chars + 4 chars for padding.
- Each char in $INPUT has a $WINDOW, which is separated into 3 $PARTS of 2 chars each (6 chars total).
    - First $PART: previous-char + current-char.
    - Second $PART: current-char + '_'.
    - Third $PART: current-char + next-char.

- If a $PART is in $ELEMENTS, its value is its symbol.
- **Otherwise, the second $PART = current-char + '*'.
- and the other $PARTS become '00'.
- Note: The third $PART of one char is the first $PART of the next.

** Having a special indicator like this allows for the second $PART to keep a reference to what letter it represents, while also marking it as invalid. If the importance of this is unclear, it should hopefully make more sense in the example below.

E.G.
$INPUT = 'the'
Padding chars are added:
'0the0'

The char 't' is expanded like so:
        '0t'   't'    'th'
$WORD = '00' + 't*' + 'th'

Likewise for 'h' and 'e':
         'h'    'he'   'e'    'e0'
$WORD += 'h_' + 'he' + 'e*' + '00'
Notice how 'th' and 'he' are shared by two letters (e.g. 'th' is the third $PART of 't' and the first $PART of 'h').

Therefore:
$WORD = '00t*thh_hee*00'

4. For i in 2..lengthOf($WORD) - 4
i += 2
Let p = i - 2
Let n = i + 2

These correspond with the 3 parts of the $WINDOW:
Let prev = $WORD[p] + $WORD[p + 1]
Let curr = $WORD[i] + $WORD[i + 1]
Let next = $WORD[n] + $WORD[n + 1]

For this next part, its easier to think of each $PART as a boolean value, where true means it represents a valid periodic symbol (If $PART != '00' && '*' not in $PART).
Bool($WORD) => 0011100

This is separated into 3 $WINDOWS:
'0t' and 't' are not valid, 'th' is valid:
- $W0 = 001 
'th', 'h', and 'he' are all valid:
- $W1 = 111 
'he' is valid, 'e' and 'e0' are not:
- $W2 = 100

Foreach $W:
- If $W has only 1 true: 
    - Letters used in that symbol are considered claimed and cannot be used again.
    - This is done by setting the 2 previous and 2 next bits to 0, aka clearing the adjacent bits.
    - If $W = 001, the next window is skipped.
- If $W has 0 true values it is skipped.

E.G. 
$W0 satisfies this condition, so the 't' and 'h' chars are claimed. This means 'h' and 'he' are no longer valid.
Of course, t is also claimed. And while its boolean form is already 0, the value of 't*' must be cleared, so it actually does change. 

$W0 = 001      => 001
    = '00t*th' => '0000th'
$W1 = 111      => 100
    = 'thh_he' => 'th0000'
$W2 = 100      => 000
    = 'hee*00' => '00e*00'

Both $W1 and $W2 are skipped 

$WORD = '0000th0000e*00'

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

3rd case, W3 doesn't need #4
0123456
011      001    SET(2), CLR(0,1), CLR(3,4)
  1?1      100                                         
    1??      0??                                       

Therefore, the program should be able to do this in one pass.

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
