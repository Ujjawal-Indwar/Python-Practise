print("Welcome to the love calculator ")
name1 = input("What is your name? \n").lower()
name2 = input("What is your crush's name \n").lower()

var_t = name1.count('t')+name2.count('t');
var_r = name1.count('r')+name2.count('r');
var_u = name1.count('u')+name2.count('u');
var_e = name1.count('e')+name2.count('e');

var_l = name1.count('l')+name2.count('l');
var_o = name1.count('o')+name2.count('o');
var_v = name1.count('v')+name2.count('v');
var_ee = name1.count('e')+name2.count('e');

var_per=(var_t+var_r+var_u+var_e);
var_centage=(var_l+var_o+var_v+var_ee);

print(var_per,var_centage,'%');