# TP 1

## Exercice 1

### Question a

```python
import numpy as np
from logging import Logger

class NumberLogger(Logger):
    def __init__(self, file):
        self.file = file
    def log_nb(self, nb):
        self.log("INFO", np.format_float_scientific(nb))

if __name__ == "__main__":
    lg = NumberLogger()
    lg.log_nb(1.245)
```

<details>
<summary>Tableau du lexer correspondant au code python ci-dessus</summary>

| Category | Valeur | Position |
| :--- | :--- | :--- |
| kw_import| import | 1.1|
| space |  | 1.7|
| indent | numpy | 1.8|
| space |  | 1.13|
| kw_as | as | 1.14|
| space |   | 1.16|
| indent | np | 1.17|
| kw_from | from | 2.1|
| space |  | 2.5|
| indent | logging | 2.6|
| space |  | 2.13|
| kw_import | import | 2.14|
| space |  | 2.20|
| indent | Logger | 2.21|
| kw_class | class | 4.1|
| space |  | 4.6|
| indent | NumberLogger | 4.7|
| lparen | ( | 4.20|
| indent | Logger | 4.21|
| rparen | ) | 4.27|
| colon | : | 4.28|
| kw_tab | \t | 5.1|
| kw_def | def | 5.5|
| kw_init | \__init__ | 5.9|
| lparen | ( | 5.17|
| kw_self | self | 5.18|
| comma | , | 5.22|
| indent | file | 5.24|
| rparen | ) | 5.28|
| colon | : | 5.29|
| kw_tab | \t | 6.1|
| kw_tab | \t | 6.5|
| kw_self | self | 6.9|
| dot | . | 6.13|
| indent | file | 6.14|
| space |  | 6.18|
| assign | = | 6.19|
| space | | 6.20|
| indent | file | 6.21|
| kw_tab | \t | 7.1|
| kw_def | def | 7.5|
| indent | log_nb | 7.9|
| lparen | ( | 7.15|
| kw_self | self | 7.16|
| comma | , | 7.20|
| indent | nb | 7.22|
| rparen | ) | 7.24|
| colon | : | 7.25|
| kw_tab | \t | 8.1|
| kw_tab | \t | 8.5|
| kw_tab | \t | 8.9|
| kw_self | self | 8.13|
| dot | . | 8.17|
| indent | log | 8.18|
| lparen | ( | 8.21|
| quote | " | 8.22|
| str_lit | INFO | 8.22|
| quote | " | 8.26|
| comma | , | 8.27|
| space |  | 8.28|
| indent | np | 8.29|
| dot | . | 8.31|
| indent | format_float_scientific | 8.32|
| lparen | ( | 8.52|
| indent | nb | 8.53|
| rparen | ) | 8.55|
| rparen | ) | 8.56|
| kw_if | if | 10.1|
| space |  | 10.3|
| kw_filename | \__name__ | 10.4|
| space |  | 10.12|
| equal | == | 10.13|
| space |  | 10.15|
| quote | " | 10.16|
| str_lit | \__main__ | 10.16|
| quote | " | 10.24|
| colon | : | 10.25|
| kw_tab | \t | 11.1|
| kw_tab | \t | 11.5|
| indent | lg | 11.9|
| space |  | 11.11|
| assign | = | 11.12|
| space |  | 11.13|
| indent | NumberLogger | 11.14|
| lparen | ( | 11.27|
| rparen | ) | 11.28|
| kw_tab | \t | 12.1|
| kw_tab | \t | 12.5|
| indent | lg | 12.9|
| dot | . | 12.11|
| indent | log_nb | 12.12|
| lparen | ( | 12.18|
| float_lit | 1.245 | 12.19|
| rparen | ) | 12.23|
</details>

### Question b

```c
#include <stdio.h>

typedef struct complex {
    float real;
    float imag;
} complex;

complex add(complex n1, complex n2) {
    complex temp;
    temp.real = n1.real + n2.real;
    temp.imag = n1.imag + n2.imag;
    return temp;
}

int main() {
    complex n1 = {.float = 1, .imag = 3};
    complex n2 = {.float = 2, .imag = 4};
    complex result;
    result = add(n1, n2);
    printf("Sum = %.1f + %.1fi", result.real, result.imag);
    return 0;
}
```

> **Note:** Commentaires
> Les commentaires peuvent être géré de différentes manières. Le plus souvent, on les considère comme des lexers puis on les enlève au moment du passage en arbre syntaxique (ast)

On ne prend pas en compte la première ligne du code C car il est géré par le préprocesseur. Cela ne fait pas partie de l'étape de lexing.

<details>
<summary>Tableau lexer correspondant au code c</summary>

| Category | Valeur | Position |
| :--- | :--- | :--- |
| kw_typedef | typedef | 2.1|
| kw_struct | struct | 2.9|
| indent | complex | 2.15|
| lbrace | { | 2.22|
| kw_float | float | 2.24|
| indent | real | 2.29|
| semi | ; | 2.33|
| kw_float | float | 2.35|
| indent | imag | 2.40|
| semi | ; | 2.44|
| rbrace | } | 3.1|
| indent | complex | 3.3|
| semi | ; | 3.10|
| indent | complex | 4.1|
| indent | add | 4.9|
| lparen | ( | 4.12|
| indent | complex | 4.13|
| indent | n1 | 4.20|
| comma | , | 4.23|
| indent | complex | 4.25|
| indent | n2 | 4.32|
| rparen | ) | 4.35|
| lbrace | { | 4.37|
| indent | complex | 5.1|
| indent | temp | 5.9|
| semi | ; | 5.13|
| indent | temp | 6.1|
| dot | . | 6.5|
| indent | real | 6.6|
| assign | = | 6.10|
| indent | n1 | 6.12|
| dot | . | 6.15|
| indent | real | 6.16|
| plus | + | 6.20|
| indent | n2 | 6.22|
| dot | . | 6.25|
| indent | real | 6.26|
| semi | ; | 6.30|
| indent | temp | 7.1|
| dot | . | 7.5|
| indent | imag | 7.6|
| assign | = | 7.10|
| indent | n1 | 7.12|
| dot | . | 7.15|
| indent | imag | 7.16|
| plus | + | 7.20|
| indent | n2 | 7.22|
| dot | . | 7.25|
| indent | imag | 7.26|
| semi | ; | 7.30|
| indent | return | 8.1|
| indent | temp | 8.8|
| semi | ; | 8.12|
| rbrace | } | 9.1|
| kw_int | int | 11.1|
| kw_main | main | 11.5|
| lparen | ( | 11.9|
| rparen | ) | 11.10|
| lbrace | { | 11.12|
| indent | complex | 12.1|
| indent | n1 | 12.9|
| assign | = | 12.12|
| lbrace | { | 12.14|
| dot | . | 12.16|
| indent | float | 12.17|
| assign | = | 12.22|
| float_lit | 1 | 12.24|
| comma | , | 12.25|
| dot | . | 12.27|
| indent | imag | 12.28|
| assign | = | 12.32|
| float_lit | 3 | 12.34|
| rbrace | } | 12.35|
| semi | ; | 12.36|
| indent | complex | 13.1|
| indent | n2 | 13.9|
| assign | = | 13.12|
| lbrace | { | 13.14|
| dot | . | 13.16|
| indent | float | 13.17|
| assign | = | 13.22|
| float_lit | 2 | 13.24|
| comma | , | 13.25|
| dot | . | 13.27|
| indent | imag | 13.28|
| assign | = | 13.32|
| float_lit | 4 | 13.34|
| rbrace | } | 13.35|
| semi | ; | 13.36|
| indent | complex | 14.1|
| indent | result | 14.9|
| semi | ; | 14.15|
| indent | result | 15.1|
| assign | = | 15.8|
| indent | add | 15.10|
| lparen | ( | 15.13|
| indent | n1 | 15.14|
| comma | , | 15.17|
| indent | n2 | 15.19|
| rparen | ) | 15.22|
| semi | ; | 15.23|
| indent | printf | 16.1|
| lparen | ( | 16.7|
| string_lit | "Sum = %.1f + %.1fi" | 16.8|
| comma | , | 16.26|
| indent | result | 16.28|
| dot | . | 16.35|
| indent | real | 16.36|
| comma | , | 16.41|
| indent | result | 16.43|
| dot | . | 16.50|
| indent | imag | 16.51|
| rparen | ) | 16.55|
| semi | ; | 16.56|
| kw_return | return | 17.1|
| int_lit | 0 | 17.8|
| semi | ; | 17.9|
| rbrace | } | 18.1|
</details>

## Exercice 2 : découverte regex

### Question a

S'entraîner à faire des regex sur le site [regex101.com](regex101.com) (par exemple).
Lien : [Un regex pour reconnaître les flottants](https://regex101.com/r/qj63Wc/1)

Une solution : `[+-]?\d+\.\d+([eE][+-]?[0-9]+)?`

### Question b

cf. fichier python.

## Exercice 3
