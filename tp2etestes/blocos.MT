bloco main 1
    1 _ -- _ e 2
    1 1 -- 1 d 1
    2 moveIni 3
    3 * -- * d pare
fim ; main

bloco moveIni 1
    1 _ -- * d 2
    1 * -- * e 1
    2 moveOla retorne
fim ; moveIni

bloco moveOla 1
    1 * -- o d 2
    2 * -- l d 3
    3 * -- a d 4
    4 * -- * d retorne
fim ; moveOla

bloco moveFim 1
    1 _ -- * e retorne
    1 * -- * d 1
fim ; moveFim