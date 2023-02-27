---
header-includes:
 - \usepackage{fontspec}
 - \usepackage{fvextra}
 - \setmainfont{Times New Roman}
 - \setmonofont{Consolas}
 - \fvset{breaklines=true, breakanywhere=true}
 - \renewcommand{\theFancyVerbLine}{\textcolor[rgb]{0.0,0.0,0.0}{\small\arabic{FancyVerbLine}}}
 - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{commandchars=\\\{\}, frame=leftline, numbersep=4pt, framesep=4pt}
fontsize: 12pt
geometry: left=2cm,right=2cm,top=2cm,bottom=2cm
---
Name: Aum Kulkarni  
RollNo: 36  
Div: D6AD  
**Prims Algorithm**:
```{.py include="driver.py" .numberLines}
```
**Output:**
```
0 - 2: 3
2 - 3: 2
3 - 4: 1
3 - 1: 4

Spanning tree cost: 10
```
```{.py include="priorityqueue.py" .numberLines}
```
```{.py include="stack_app/__init__.py" .numberLines}
```
```{.py include="stack_app/in_pre.py" .numberLines}
```
```{.py include="stack_app/post_eval.py" .numberLines}
```
\newline
```{.py include="linkedlist_ops/__init__.py" .numberLines}
```

```{.py include="linkedlist_ops/node.py" .numberLines}
```
\newline
```{.py include="linkedlist_ops/linkedlist.py" .numberLines}
```
```{.py include="linkedlist_ops/add_ll.py" .numberLines}
```
```{.py include="linkedlist_ops/sort_ll.py" .numberLines}
```

```{.py include="linkedlist_ops/sample_ll.py" .numberLines}
```