# Homework Tasks

## Each of these tasks is worth 10 points. You can do **any two** of them. Or all of them if you are a madman :)

*TASK 1.* Spacy's PhraseMatcher is painfully slow. Create your own method of matching phrases against a text **using a trie structure**. (Trust me, all other methods are slower.)
Input: gazetteers, a long string of text
Output: character coordinates of matched phrases in the text
Calculate the execution time.

*TASK 2.* Expand the ELIZA bot. You'll find the description for this task in the folder ELIZA.

*TASK 3.* Create your own implementation of the Porter stemmer. It is not complicated, but it does have a very particular structure, so be sure to follow it! You can find a really nice guide here: http://snowball.tartarus.org/algorithms/porter/stemmer.html
Input: a word (string)
Output: the stem of the word (string)

*TASK 4.* **!!! WARNING: LEVEL 10000** Program your own transducer (rule parser) that would take Spacy's doc and a rule in Spacy format and would the pattern to find all matching phrases in the doc. In an essense, you would be creating your own regular expressions parser. This sounds easy until you start thinking about the operators! Each token in Spacy's script can have an operator !, ?, * or +.
TIP: To handle the operators, process each elemenent of the rule separately and save the endings of the previous result, then for the next element search starting with the previous endings. Code separate ways to extend the results for each operator.
Input: Spacy's doc, a rule in Spacy format
Output: word coordinates (token.i) of matched phrases
