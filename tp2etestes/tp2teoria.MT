bloco main 0
    ; Transforma os Numeros em letras maiusculas
    0 0 -- A d 0
    0 1 -- B d 0
    0 2 -- C d 0
    0 3 -- D d 0
    0 4 -- E d 0
    0 5 -- F d 0
    0 6 -- G d 0
    0 7 -- H d 0
    0 8 -- I d 0
    0 9 -- J d 0
    0 + -- * d 0
    0 = -- * d 0
    0 _ -- * e 1

    ; Funcao que apenas retorna até o início e chama a funcao 2 que identifica o primeiro número
    1 _ -- * d 2
    1 * -- * e 1

    ; Procura o simbolo do + para que possa armazenar o primeiro numero
    2 + -- * e 3
    2 * -- * d 2

    ; Este estado que armazena qual número foi reconhecido, o primeiro numero
    3 A -- a d 4
    3 B -- b d 5
    3 C -- c d 6
    3 D -- d d 7
    3 E -- e d 8
    3 F -- f d 9
    3 G -- g d 10
    3 H -- h d 11
    3 I -- i d 12
    3 J -- j d 13
    3 _ -- * d 124
    3 * -- * e 3

    ; Procura o segundo numero que sera somado com 0
    4 = -- * e 14
    4 * -- * d 4

    ; Procura o segundo numero que sera somado com 1
    5 = -- * e 15
    5 * -- * d 5

    ; Procura o segundo numero que sera somado com 2
    6 = -- * e 16
    6 * -- * d 6

    ; Procura o segundo numero que sera somado com 3
    7 = -- * e 17
    7 * -- * d 7

    ; Procura o segundo numero que sera somado com 4
    8 = -- * e 18
    8 * -- * d 8

    ; Procura o segundo numero que sera somado com 5
    9 = -- * e 19
    9 * -- * d 9

    ; Procura o segundo numero que sera somado com 6
    10 = -- * e 20
    10 * -- * d 10

    ; Procura o segundo numero que sera somado com 7
    11 = -- * e 21
    11 * -- * d 11

    ; Procura o segundo numero que sera somado com 8
    12 = -- * e 22
    12 * -- * d 12

    ; Procura o segundo numero que sera somado com 9
    13 = -- * e 23
    13 * -- * d 13

    ; Procura o segundo numero que sera somado com vazio
    124 = -- * e 125
    124 * -- * d 124

    ; Identifica qual o numero que sera somado com o vazio
    125 A -- a d 24
    125 B -- b d 25
    125 C -- c d 26
    125 D -- d d 27
    125 E -- e d 28
    125 F -- f d 29
    125 G -- g d 30
    125 H -- h d 31
    125 I -- i d 32
    125 J -- j d 33
    125 + -- * i 126
    125 * -- * e 125

    ; Identifica qual o numero que sera somado com o 0
    14 A -- a d 24
    14 B -- b d 25
    14 C -- c d 26
    14 D -- d d 27
    14 E -- e d 28
    14 F -- f d 29
    14 G -- g d 30
    14 H -- h d 31
    14 I -- i d 32
    14 J -- j d 33
    14 + -- * d 24
    14 * -- * e 14

    ; Identifica qual o numero que sera somado com o 1
    15 A -- a d 34
    15 B -- b d 35
    15 C -- c d 36
    15 D -- d d 37
    15 E -- e d 38
    15 F -- f d 39
    15 G -- g d 40
    15 H -- h d 41
    15 I -- i d 42
    15 J -- j d 43
    15 + -- * d 34
    15 * -- * e 15

    ; Identifica qual o numero que sera somado com o 2
    16 A -- a d 44
    16 B -- b d 45
    16 C -- c d 46
    16 D -- d d 47
    16 E -- e d 48
    16 F -- f d 49
    16 G -- g d 50
    16 H -- h d 51
    16 I -- i d 52
    16 J -- j d 53
    16 + -- * d 44
    16 * -- * e 16

    ; Identifica qual o numero que sera somado com o 3
    17 A -- a d 54
    17 B -- b d 55
    17 C -- c d 56
    17 D -- d d 57
    17 E -- e d 58
    17 F -- f d 59
    17 G -- g d 60
    17 H -- h d 61
    17 I -- i d 62
    17 J -- j d 63
    17 + -- * d 54
    17 * -- * e 17

    ; Identifica qual o numero que sera somado com o 4
    18 A -- a d 64
    18 B -- b d 65
    18 C -- c d 66
    18 D -- d d 67
    18 E -- e d 68
    18 F -- f d 69
    18 G -- g d 70
    18 H -- h d 71
    18 I -- i d 72
    18 J -- j d 73
    18 + -- * d 64
    18 * -- * e 18

    ; Identifica qual o numero que sera somado com o 5
    19 A -- a d 74
    19 B -- b d 75
    19 C -- c d 76
    19 D -- d d 77
    19 E -- e d 78
    19 F -- f d 79
    19 G -- g d 80
    19 H -- h d 81
    19 I -- i d 82
    19 J -- j d 83
    19 + -- * d 74
    19 * -- * e 19

    ; Identifica qual o numero que sera somado com o 6
    20 A -- a d 84
    20 B -- b d 85
    20 C -- c d 86
    20 D -- d d 87
    20 E -- e d 88
    20 F -- f d 89
    20 G -- g d 90
    20 H -- h d 91
    20 I -- i d 92
    20 J -- j d 93
    20 + -- * d 84
    20 * -- * e 20

    ; Identifica qual o numero que sera somado com o 7
    21 A -- a d 94
    21 B -- b d 95
    21 C -- c d 96
    21 D -- d d 97
    21 E -- e d 98
    21 F -- f d 99
    21 G -- g d 100
    21 H -- h d 101
    21 I -- i d 102
    21 J -- j d 103
    21 + -- * d 94
    21 * -- * e 21

    ; Identifica qual o numero que sera somado com o 8
    22 A -- a d 104
    22 B -- b d 105
    22 C -- c d 106
    22 D -- d d 107
    22 E -- e d 108
    22 F -- f d 109
    22 G -- g d 110
    22 H -- h d 111
    22 I -- i d 112
    22 J -- j d 113
    22 + -- * d 104
    22 * -- * e 22

    ; Identifica qual o numero que sera somado com o 9
    23 A -- a d 114
    23 B -- b d 115
    23 C -- c d 116
    23 D -- d d 117
    23 E -- e d 118
    23 F -- f d 119
    23 G -- g d 120
    23 H -- h d 121
    23 I -- i d 122
    23 J -- j d 123
    23 + -- * d 114
    23 * -- * e 23

    ; Daqui pra frente estão os resultados das somas feitas com o vazio
    24 + -- 1 i 1
    24 _ -- 0 i 1
    24 * -- * d 24

    25 + -- 2 i 1
    25 _ -- 1 i 1
    25 * -- * d 25

    26 + -- 3 i 1
    26 _ -- 2 i 1
    26 * -- * d 26

    27 + -- 4 i 1
    27 _ -- 3 i 1
    27 * -- * d 27

    28 + -- 5 i 1
    28 _ -- 4 i 1
    28 * -- * d 28

    29 + -- 6 i 1
    29 _ -- 5 i 1
    29 * -- * d 29

    30 + -- 7 i 1
    30 _ -- 6 i 1
    30 * -- * d 30

    31 + -- 8 i 1
    31 _ -- 7 i 1
    31 * -- * d 31

    32 + -- 9 i 1
    32 _ -- 8 i 1
    32 * -- * d 32

    33 + -- 0 d 164
    33 _ -- 9 i 1
    33 * -- * d 33

    ; Daqui pra frente estão os resultados das somas feitas com o 1
    34 + -- 2 i 1
    34 _ -- 1 i 1
    34 * -- * d 34

    35 + -- 3 i 1
    35 _ -- 2 i 1
    35 * -- * d 35

    36 + -- 4 i 1
    36 _ -- 3 i 1
    36 * -- * d 36

    37 + -- 5 i 1
    37 _ -- 4 i 1
    37 * -- * d 37

    38 + -- 6 i 1
    38 _ -- 5 i 1
    38 * -- * d 38

    39 + -- 7 i 1
    39 _ -- 6 i 1
    39 * -- * d 39

    40 + -- 8 i 1
    40 _ -- 7 i 1
    40 * -- * d 40

    41 + -- 9 i 1
    41 _ -- 8 i 1
    41 * -- * d 41

    42 + -- 0 d 164
    42 _ -- 9 i 1
    42 * -- * d 42

    43 + -- 1 d 164
    43 _ -- 0 d 164
    43 * -- * d 43

    ; Daqui pra frente estão os resultados das somas feitas com o 2
    44 + -- 3 i 1
    44 _ -- 2 i 1
    44 * -- * d 44

    45 + -- 4 i 1
    45 _ -- 3 i 1
    45 * -- * d 45

    46 + -- 5 i 1
    46 _ -- 4 i 1
    46 * -- * d 46

    47 + -- 6 i 1
    47 _ -- 5 i 1
    47 * -- * d 47

    48 + -- 7 i 1
    48 _ -- 6 i 1
    48 * -- * d 48

    49 + -- 8 i 1
    49 _ -- 7 i 1
    49 * -- * d 49

    50 + -- 9 i 1
    50 _ -- 8 i 1
    50 * -- * d 50

    51 + -- 0 d 164
    51 _ -- 9 i 1
    51 * -- * d 51

    52 + -- 1 d 164
    52 _ -- 0 d 164
    52 * -- * d 52

    53 + -- 2 d 164
    53 _ -- 1 d 164
    53 * -- * d 53

    ; Daqui pra frente estão os resultados das somas feitas com o 3
    54 + -- 4 i 1
    54 _ -- 3 i 1
    54 * -- * d 54

    55 + -- 5 i 1
    55 _ -- 4 i 1
    55 * -- * d 55

    56 + -- 6 i 1
    56 _ -- 5 i 1
    56 * -- * d 56

    57 + -- 7 i 1
    57 _ -- 6 i 1
    57 * -- * d 57

    58 + -- 8 i 1
    58 _ -- 7 i 1
    58 * -- * d 58

    59 + -- 9 i 1
    59 _ -- 8 i 1
    59 * -- * d 59

    60 + -- 0 d 164
    60 _ -- 9 i 1
    60 * -- * d 60

    61 + -- 1 d 164
    61 _ -- 0 d 164
    61 * -- * d 61

    62 + -- 2 d 164
    62 _ -- 1 d 164
    62 * -- * d 62

    63 + -- 3 d 164
    63 _ -- 2 d 164
    63 * -- * d 63

    ; Daqui pra frente estão os resultados das somas feitas com o 4
    64 + -- 5 i 1
    64 _ -- 4 i 1
    64 * -- * d 64

    65 + -- 6 i 1
    65 _ -- 5 i 1
    65 * -- * d 65

    66 + -- 7 i 1
    66 _ -- 6 i 1
    66 * -- * d 66

    67 + -- 8 i 1
    67 _ -- 7 i 1
    67 * -- * d 67

    68 + -- 9 i 1
    68 _ -- 8 i 1
    68 * -- * d 68

    69 + -- 0 d 164
    69 _ -- 9 i 1
    69 * -- * d 69

    70 + -- 1 d 164
    70 _ -- 0 d 164
    70 * -- * d 70

    71 + -- 2 d 164
    71 _ -- 1 d 164
    71 * -- * d 71

    72 + -- 3 d 164
    72 _ -- 2 d 164
    72 * -- * d 72

    73 + -- 4 d 164
    73 _ -- 3 d 164
    73 * -- * d 73

    ; Daqui pra frente estão os resultados das somas feitas com o 5
    74 + -- 6 i 1
    74 _ -- 5 i 1
    74 * -- * d 74

    75 + -- 7 i 1
    75 _ -- 6 i 1
    75 * -- * d 75

    76 + -- 8 i 1
    76 _ -- 7 i 1
    76 * -- * d 76

    77 + -- 9 i 1
    77 _ -- 8 i 1
    77 * -- * d 77

    78 + -- 0 d 164
    78 _ -- 9 i 1
    78 * -- * d 78

    79 + -- 1 d 164
    79 _ -- 0 d 164
    79 * -- * d 79

    80 + -- 2 d 164
    80 _ -- 1 d 164
    80 * -- * d 80

    81 + -- 3 d 164
    81 _ -- 2 d 164
    81 * -- * d 81

    82 + -- 4 d 164
    82 _ -- 3 d 164
    82 * -- * d 82

    83 + -- 5 d 164
    83 _ -- 4 d 164
    83 * -- * d 83

    ; Daqui pra frente estão os resultados das somas feitas com o 6
    84 + -- 7 i 1
    84 _ -- 6 i 1
    84 * -- * d 84

    85 + -- 8 i 1
    85 _ -- 7 i 1
    85 * -- * d 85

    86 + -- 9 i 1
    86 _ -- 8 i 1
    86 * -- * d 86

    87 + -- 0 d 164
    87 _ -- 9 i 1
    87 * -- * d 87

    88 + -- 1 d 164
    88 _ -- 0 d 164
    88 * -- * d 88

    89 + -- 2 d 164
    89 _ -- 1 d 164
    89 * -- * d 89

    90 + -- 3 d 164
    90 _ -- 2 d 164
    90 * -- * d 90

    91 + -- 4 d 164
    91 _ -- 3 d 164
    91 * -- * d 91

    92 + -- 5 d 164
    92 _ -- 4 d 164
    92 * -- * d 92

    93 + -- 6 d 164
    93 _ -- 5 d 164
    93 * -- * d 93

    ; Daqui pra frente estão os resultados das somas feitas com o 7
    94 + -- 8 i 1
    94 _ -- 7 i 1
    94 * -- * d 94

    95 + -- 9 i 1
    95 _ -- 8 i 1
    95 * -- * d 95

    96 + -- 0 d 164
    96 _ -- 9 i 1
    96 * -- * d 96

    97 + -- 1 d 164
    97 _ -- 0 d 164
    97 * -- * d 97

    98 + -- 2 d 164
    98 _ -- 1 d 164
    98 * -- * d 98

    99 + -- 3 d 164
    99 _ -- 2 d 164
    99 * -- * d 99

    100 + -- 4 d 164
    100 _ -- 3 d 164
    100 * -- * d 100

    101 + -- 5 d 164
    101 _ -- 4 d 164
    101 * -- * d 101

    102 + -- 6 d 164
    102 _ -- 5 d 164
    102 * -- * d 102

    103 + -- 7 d 164
    103 _ -- 6 d 164
    103 * -- * d 103

    ; Daqui pra frente estão os resultados das somas feitas com o 8
    104 + -- 9 i 1
    104 _ -- 8 i 1
    104 * -- * d 104

    105 + -- 0 d 164
    105 _ -- 9 i 1
    105 * -- * d 105

    106 + -- 1 d 164
    106 _ -- 0 d 164
    106 * -- * d 106

    107 + -- 2 d 164
    107 _ -- 1 d 164
    107 * -- * d 107

    108 + -- 3 d 164
    108 _ -- 2 d 164
    108 * -- * d 108

    109 + -- 4 d 164
    109 _ -- 3 d 164
    109 * -- * d 109

    110 + -- 5 d 164
    110 _ -- 4 d 164
    110 * -- * d 110

    111 + -- 6 d 164
    111 _ -- 5 d 164
    111 * -- * d 111

    112 + -- 7 d 164
    112 _ -- 6 d 164
    112 * -- * d 112

    113 + -- 8 d 164
    113 _ -- 7 d 164
    113 * -- * d 113

    ; Daqui pra frente estão os resultados das somas feitas com o 9
    114 + -- 0 d 164
    114 _ -- 9 i 1
    114 * -- * d 114

    115 + -- 1 d 164
    115 _ -- 0 d 164
    115 * -- * d 115

    116 + -- 2 d 164
    116 _ -- 1 d 164
    116 * -- * d 116

    117 + -- 3 d 164
    117 _ -- 2 d 164
    117 * -- * d 117

    118 + -- 4 d 164
    118 _ -- 3 d 164
    118 * -- * d 118

    119 + -- 5 d 164
    119 _ -- 4 d 164
    119 * -- * d 119

    120 + -- 6 d 164
    120 _ -- 5 d 164
    120 * -- * d 120

    121 + -- 7 d 164
    121 _ -- 6 d 164
    121 * -- * d 121

    122 + -- 8 d 164
    122 _ -- 7 d 164
    122 * -- * d 122

    123 + -- 9 d 164
    123 _ -- 8 d 164
    123 * -- * d 123

    ; Esta parte do código é responsável por verificar se o programa finalizou, onde ele achou vazio tanto no primeiro numero quanto no segundo
    126 _ -- * d 127
    126 * -- * e 126

    ; Aqui o código retorna os números para as letras, e caso tenha um + ele entra em um caso especial, e coloca um hashtag no final
    127 a -- 0 d 127
    127 b -- 1 d 127
    127 c -- 2 d 127
    127 d -- 3 d 127
    127 e -- 4 d 127
    127 f -- 5 d 127
    127 g -- 6 d 127
    127 h -- 7 d 127
    127 i -- 8 d 127
    127 j -- 9 d 127
    127 = -- * i 163
    127 _ -- # i 128
    127 * -- * d 127

    ; Aqui ele faz o processo de inverter a palavra utilizando o hashtag como base para contruir corretamente e no final arrasta o número através do hashtag
    128 _ -- * e 128
    128 0 -- _ i 129
    128 1 -- _ i 130
    128 2 -- _ i 131
    128 3 -- _ i 132
    128 4 -- _ i 133
    128 5 -- _ i 134
    128 6 -- _ i 135
    128 7 -- _ i 136
    128 8 -- _ i 137
    128 9 -- _ i 138
    128 = -- * d 150
    128 * -- * e 128

    129 # -- * d 139
    129 * -- * d 129

    130 # -- * d 140
    130 * -- * d 130

    131 # -- * d 141
    131 * -- * d 131

    132 # -- * d 142
    132 * -- * d 132

    133 # -- * d 143
    133 * -- * d 133

    134 # -- * d 144
    134 * -- * d 134

    135 # -- * d 145
    135 * -- * d 135

    136 # -- * d 146
    136 * -- * d 136

    137 # -- * d 147
    137 * -- * d 137

    138 # -- * d 148
    138 * -- * d 138

    139 _ -- 0 i 149
    139 * -- * d 139

    140 _ -- 1 i 149
    140 * -- * d 140

    141 _ -- 2 i 149
    141 * -- * d 141

    142 _ -- 3 i 149
    142 * -- * d 142

    143 _ -- 4 i 149
    143 * -- * d 143

    144 _ -- 5 i 149
    144 * -- * d 144

    145 _ -- 6 i 149
    145 * -- * d 145

    146 _ -- 7 i 149
    146 * -- * d 146

    147 _ -- 8 i 149
    147 * -- * d 147

    148 _ -- 9 i 149
    148 * -- * d 148

    149 # -- * i 128
    149 * -- * e 149

    150 _ -- * d 150
    150 # -- * i 151

    151 _ -- * e 152
    151 * -- * d 151

    152 0 -- _ e 153
    152 1 -- _ e 154
    152 2 -- _ e 155
    152 3 -- _ e 156
    152 4 -- _ e 157
    152 5 -- _ e 158
    152 6 -- _ e 159
    152 7 -- _ e 160
    152 8 -- _ e 161
    152 9 -- _ e 162
    152 # -- _ i pare
    
    153 _ -- 0 d 151
    153 * -- * e 153

    154 _ -- 1 d 151
    154 * -- * e 154

    155 _ -- 2 d 151
    155 * -- * e 155

    156 _ -- 3 d 151
    156 * -- * e 156

    157 _ -- 4 d 151
    157 * -- * e 157

    158 _ -- 5 d 151
    158 * -- * e 158

    159 _ -- 6 d 151
    159 * -- * e 159

    160 _ -- 7 d 151
    160 * -- * e 160

    161 _ -- 8 d 151
    161 * -- * e 161

    162 _ -- 9 d 151
    162 * -- * e 162

    ; Este caso específico trata caso tenha sobrado um + que significa vai um e nao foi somado, ele transforma em 1
    163 _ -- # i 128
    163 + -- 1 d 127
    163 * -- * d 163

    ; Esta parte cuida do +, vai um, que sempre adiciona um valor, onde nas operacoes dos resultados, tem um tratamentoe especial para cada soma, caso ache o +
    164 _ -- + i 1
fim ; main
