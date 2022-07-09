# FoodSelector
Is your team awful at choosing what to have for lunch? This is the script for you! Simply provide your restaurant 
and menu items preferences to the script, and you have your lunch order!

### Sample input
```yaml
---
- name: Applebees
  choices:
    - person: Bob
      likes:
        - chicken
        - burger
        - sandwich
    - person: Jill
      likes:
        - sandwich
        - salad
        - burger
        - wings
        - apples
        - bees
- name: McDonalds
  choices:
    - person: Bob
      likes:
        - chicken
        - burger
        - sandwich
    - person: Jill
      likes:
        - salad
        - spicy chicken sandwich
...
```

### Sample output
```commandline
Applebees
Bob: chicken
Jill: salad
```

### Supported formats
* YAML 
* JSON
* CSV*

### CSV converter
Data from a spreadsheet can be imported to the lunch script using the CSV converter script.

Format is
```
Restaurant1
Person1, choice1, choice2 ...
Person2, choice1, choice2 ...
...
<blank line>
Restaurant2
Person1 ...
...
```

#### Sample input
```csv
Applebees,,,
Raju,apples,bees,
Al,sandwich,fries,
,,,
Wendy's,,,
Ed,baconator,spicy chicken,chili
Rosa,baconator,salad,
```