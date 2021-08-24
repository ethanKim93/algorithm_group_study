# String

#### 

```python
Example = ['sdfafdasfsxcvb']
word = ['fa']
```



### Brueteforce

```python
for i in range(len(Example)-1):
  	i = i + cnt*len(word)
    if i >= len(Example):
      break
      
    if Example[i:i+len(word)] == word:
      cnt += 1
```



### Pattern Matching

```python
E = len(Example)
w = len(word)


def Pattern_Matching(Example, word):
    Example_idx = 0
    word_idx = 0
    while word_idx < w and Example_idx < E:
        if Example[Example_idx] != word[word_idx]:
            Example_idx -= word_idx
            word_idx -= 1
        Example_idx += 1
        word_idx += 1


if word_idx == w:
    return True
else:
    return False

```

