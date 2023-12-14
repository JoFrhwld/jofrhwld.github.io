Functions
================
Josef Fruehwald
10/14/22

## Writing your own functions

So far, we’ve been using either built in python functions, like `len()`
or `print()`, or functions provided by other packages, like
`nltk.word_tokenize()`.

But, we can also write our *own* functions. It is super useful to write
our own functions so that we can save on retyping code, and to ensure we
carry out the same exact operations every time.

## Example - Counting tokens in a book

### Without our own function

If we wanted to count the number of tokens in a book, we could write out
some code like so:

``` python
import nltk
```

``` python
path = "gen/texts/frank.txt"
with open(path, 'r') as f:
  text = f.read()
tokens = nltk.word_tokenize(text)
n_tokens = len(tokens)
n_types = len(set(tokens))
type_token_dict = {"tokens" : n_tokens,
                   "types" : n_types}
```

``` python
type_token_dict
```

    {'tokens': 85324, 'types': 7710}

Now, if we wanted to do the same thing all over again with a different
book, say *Voyage to the Center of the Earth*, we’d have to copy-paste
our code, and maybe even change the variable names. Instead we can
rewrite this code as a *function*.

### Writing a function

To write your own function, you need to plan on what kind of *inputs*
you want to use to get specific *outputs*. A simple function in python
looks like this.

``` python
def repeat_string(input_string, n):
  """
    Repeat the input_string n times
  """
  output_string = [input_string] * n
  return(output_string)
```

``` python
repeat_string(input_string = "hello", n = 5)
```

    ['hello', 'hello', 'hello', 'hello', 'hello']

Let’s briefly pick apart each line

#### The definition line

``` python
def repeat_string(input_string, n):
```

This line *defines* (hence the `def` part) the new function. After
running this whole block of code, when we type in `repeat_string`,
python is going to interpret it as referring to this function (a lot
like how variable assignment works).

Whatever we type in after `def` is going to be the name of our new
function. The restrictions on what we name functions are the same as for
variables.

Inside the parentheses are the variables the function *will* use. This
is a lot like how we declare temporary variables in a for loop, and then
use that variable inside the for loop.

<div>

> **Naming Recommendation**
>
> I’m going to make the following recommendations about function naming:
>
> - name your functions in lower case.
>
> - use underscores `_` to separate words (you *can’t* use dots `.` or
>   dashes `-`)
>
> - make the first word in your function word an imperative verb. some
>   good options are going to be
>
>   - `get_`
>
>   - `calculate_`
>
>   - `make_`
>
> - name the whole function for what it *does*.
>
>   - `calculate_conditional_prob()`
>
>   - `convert_prob_to_surprisal()`
>
>   - `get_book()`

</div>

#### The “docstring”

Immediately after the definition line, (and indented once), include a
brief description of what the function does, marked out by three `"`.

``` python
  """
    Repeat the input_string n times
  """
```

This is important for 2 reasons:

1.  Explaining your code to other people.
2.  Explaining your code to yourself, in the future (who is effectively
    another person).

There are also a lot of python systems that automatically extract
docstrings from python scripts to build whole documentation pages.

#### The function block

Now, we have the main part of the function: the code that does stuff.

``` python
  output_string = [input_string] * n
```

Inside this function block, we can call upon the temporary variables we
defined in the definition line, and any other function, including
functions from the standard library, functions we’ve imported, or any
other function we’ve written.

We can also create and modify any variables we want inside the function.
But note, they’re going to stay locked away inside the function, and we
won’t be able to call upon them in other parts of our scripts.

#### The return statement

Once we’ve done some stuff inside the function, we’ll usually want it to
have something to show for its work. This is where the `return()`
statement comes in. This is where the function returns some kind of
output for us to work on in the rest of the script.

``` python
  return(output_string)
```

#### Planning for writing a function

Think about writing a function like packing for a trip. You need to plan
for what you’re going to bring with you, and while you’re away, you
won’t be able access anything you didn’t bring along. Then, at the end
of the trip, you can come home with a souvenir!

For example, let’s write another function that prints out the output of
the previous `repeat_string()` function where we forget to pack
something.

``` python
def print_repetition(input_string):
  """
    print the input string n times
    This function doesn't return() anything, and that's ok
  """
  rep_list = repeat_string(input_string, n = n)
  for item in rep_list:
    print(item)

print_repetition("hello!")
```

    NameError: name 'n' is not defined

Ah! In the `def` line, we forgot to pack `n`! Even if we try to pass an
argument `n` to the function, it won’t know what to do with it.

### Writing the type & token function

As a reminder, here’s the code we used before to read in `frank.txt` and
return a dictionary of

``` python
path = "gen/texts/frank.txt"
with open(path, 'r') as f:
  text = f.read()
tokens = nltk.word_tokenize(text)
n_tokens = len(tokens)
n_types = len(set(tokens))
type_token_dict = {"tokens" : n_tokens,
                   "types" : n_types}
```

Let’s turn this into a function.

#### What are we “packing on our trip”?

Or, what are our “inputs” to the function. We have a few different
possible answers here.

1.  We could decide to start with the `path` string. In that case, we’d
    tell our function to go read in the file as the first step. The only
    downside here is we wouldn’t have access to the file text at the
    end, just whatever the function `returns()`
2.  We could decide to start with the `text` string. That means outside
    of the function, we’d have to do the opening and reading of the
    function.

Let’s decide on starting on the `path` string.

#### What are we bringing home as a souvenir?

This is a little easier to answer: our target is the `type_token_dict`
dictionary.

#### The actual function!

``` python
def get_type_token(path):
  """
    Read in a file from path, and return a dictionary of type and token counts.
  """
  with open(path, 'r') as f:
    text = f.read()
  tokens = nltk.word_tokenize(text)
  n_tokens = len(tokens)
  n_types = len(set(tokens))
  type_token_dict = {"tokens" : n_tokens,
                     "types" : n_types}
  return(type_token_dict)
```

``` python
get_type_token(path = "gen/texts/frank.txt")
get_type_token(path = "gen/texts/voyage.txt")
```

    {'tokens': 102356, 'types': 8439}

## The task!

All of these tasks are asking you to reuse code from the Making and
Counting Bigrams project, but to turn them into functions.

<div>

> **Task 1**
>
> Write a function that takes as input a file path, and returns the
> tokenized and padded sentences as a flat list.
>
> ``` python
> def read_in_tokens(path):
>   """
>     Given a path, this returns the tokenized book, with sentences padded out for bigrams
>   """
>   
>   ## Things here!
>   return()
> ```

</div>

<div>

> **Task 2**
>
> Write a function that takes tokenized and padded text, and returns
> counts of bigrams.
>
> ``` python
> def make_bigram_counts(tokens):
>   """
>     Given a list of tokens, this returns the count of bigrams
>   """
>   
>   ## Things here
>   return()
> ```

</div>

<div>

> **Task 3**
>
> Write a function that takes a tokenized and padded text, and returns
> counts of unigrams.
>
> ``` python
> def make_bigram_counts(tokens):
>   """
>     Given a list of tokens, this returns the count of unigrams
>   """
>   
>   return()
> ```

</div>

<div>

> **Task 4**
>
> Write a function that if given a sequence of words `w1` and `w2`, and
> bigram & unigram counts, will return the conditional probability of
> P(w2 \| w1).
>
> **NOTE**: A simplified way to get the conditional probability of P(w2
> \| w1) is to get just the count of the bigram (w1, w2) and divide it
> by the count of the unigram (w1).
>
> ``` python
> def calculate_conditional_probability(w1, w2, bigram_count, unigram_coint):
>   """
>     Given a sequence of words, w1 and w2, as well as bigram and unigram counts, this
>     returns the conditional probability of P(w2 | w1)
>   """
>   ## Stuff here
>   return()
> ```

</div>

### Tips for doing these tasks

#### Test by doing

The best way to test if your function is working is to try it out on
things! Just try running and rerunning your function to see what it
outputs and see if it looks like you were expecting.

#### Build it up

Rather than try writing a function that works **and** does what you want
it to do in one go, try building it up by writing a function that works
but **doesn’t** do what you want it to do. Then slowly iterate and try
adjusting your function until you get to the output you’re looking for.
