bloco main 1
    1 _ -- _ e 2
    1 1 -- 1 d 1
    2 moveIni 3
    3 * -- * d pare
fim ; main

bloco moveIni 1
    1 _ -- * d 2
    1 * -- * e 1
    2 movePao retorne
fim ; moveIni

bloco movePao 1
    1 * -- p d 2
    2 * -- a d 3
    3 * -- o d 4
    4 * -- * d retorne
fim ; movePao

bloco moveFim 1
    1 _ -- * e retorne
    1 * -- * d 1
fim ; moveFim