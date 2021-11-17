from enum import Enum

# Indicates the program shift value in units of 1/6 EV
# From -30 [-5 EV] to +30 [+5 EV]
# 20 or 30 values are valid epending on EVStep (1/2 or 1/3)
class FlexibleProgram(Enum):
    Minus30SixthEV  = -30
    Minus29SixthEV  = -29
    Minus28SixthEV  = -28
    Minus27SixthEV  = -27
    Minus26SixthEV  = -26
    Minus25SixthEV  = -25
    Minus24SixthEV  = -24
    Minus23SixthEV  = -23
    Minus22SixthEV  = -22
    Minus21SixthEV  = -21
    Minus20SixthEV  = -20
    Minus19SixthEV  = -19
    Minus18SixthEV  = -18
    Minus17SixthEV  = -17
    Minus16SixthEV  = -16
    Minus15SixthEV  = -15
    Minus14SixthEV  = -14
    Minus13SixthEV  = -13
    Minus12SixthEV  = -12
    Minus11SixthEV  = -11
    Minus10SixthEV  = -10
    Minus9SixthEV   = -9
    Minus8SixthEV   = -8
    Minus7SixthEV   = -7
    Minus6SixthEV   = -6
    Minus5SixthEV   = -5
    Minus4SixthEV   = -4
    Minus3SixthEV   = -3
    Minus2SixthEV   = -2
    Minus1SixthEV   = -1
    ZeroEV          = 0
    Plus1SixthEV    = 1
    Plus2SixthEV    = 2
    Plus3SixthEV    = 3
    Plus4SixthEV    = 4
    Plus5SixthEV    = 5
    Plus6SixthEV    = 6
    Plus7SixthEV    = 7
    Plus8SixthEV    = 8
    Plus9SixthEV    = 9
    Plus10SixthEV   = 10
    Plus11SixthEV   = 11
    Plus12SixthEV   = 12
    Plus13SixthEV   = 13
    Plus14SixthEV   = 14
    Plus15SixthEV   = 15
    Plus16SixthEV   = 16
    Plus17SixthEV   = 17
    Plus18SixthEV   = 18
    Plus19SixthEV   = 19
    Plus20SixthEV   = 20
    Plus21SixthEV   = 21
    Plus22SixthEV   = 22
    Plus23SixthEV   = 23
    Plus24SixthEV   = 24
    Plus25SixthEV   = 25
    Plus26SixthEV   = 26
    Plus27SixthEV   = 27
    Plus28SixthEV   = 28
    Plus29SixthEV   = 29
    Plus30SixthEV   = 30
