# TP 1

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
