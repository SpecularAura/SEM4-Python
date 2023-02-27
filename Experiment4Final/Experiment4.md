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

**arithmetic_op driver**:
```{.py include="arithmetic_op_driver.py" .numberLines}
```

**arithmetic_op module**:

```{.py include="arithmetic_op/__init__.py" .numberLines}
```
&nbsp;
```{.py include="arithmetic_op/add.py" .numberLines}
```
&nbsp;
```{.py include="arithmetic_op/diff.py" .numberLines}
```
&nbsp;
```{.py include="arithmetic_op/modulo.py" .numberLines}
```
&nbsp;
```{.py include="arithmetic_op/square.py" .numberLines}
```