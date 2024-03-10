# cause i have nothing better to do :)
Just a repo containing oneliners that I think are cool. Also, I am a newb, so they might not actually be cool. But who cares?

## Patterns

#### [Verticle Star](./patterns/verticleStar.py)
```python
for i in range(int(input(""))*2): print(" " * (([0, 2, 4, 2][(i//2) % 4]) * 2)) if i % 2 != 0 else print(" " * (([0, 2, 4, 2][(i//2) % 4]) * 2), end="*\n")
```
```
*

    *
    
        *
        
    *
    
*

    *
```
