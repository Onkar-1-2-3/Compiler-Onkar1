from start import *

def test_typecheck():
    import pytest
    te = typecheck(BinOp("+", NumLiteral(2), NumLiteral(3)))
    assert te.type == NumType
    te = typecheck(BinOp("<", NumLiteral(2), NumLiteral(3)))
    assert te.type == BoolType
    # with pytest.raises(TypeError):
    #     typecheck(BinOp("+", BinOp("*", NumLiteral(2), NumLiteral(3)), BinOp("<", NumLiteral(2), NumLiteral(3))))

def test_div_operator():
    a  = Variable("a")
    n1= NumLiteral(5)
    e2 = BinOp("/", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == 1

    b = Variable("b")
    n2 = NumLiteral(10)
    e2 = BinOp("/", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == 2

    """
    should show error if divided by zero. 
    """
    # c = Variable("c")
    # n0 = NumLiteral(0)
    # e2 = BinOp("/", b, c)
    # e  = Let(c, n0, Let(b, n2,e2 ))
    # assert eval(e) == InvalidProgram


def test_modulus_operator():
    a  = Variable("a")
    n1= NumLiteral(5)
    e2 = BinOp("%", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == 0

    b = Variable("b")
    n2 = NumLiteral(11)
    e2 = BinOp("%", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == 1

def test_floor_div_operator():
    a  = Variable("a")
    n1= NumLiteral(5)
    e2 = BinOp("//", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == 1

    b = Variable("b")
    n2 = NumLiteral(15)
    e2 = BinOp("//", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == 3

def test_power_operator():
    a  = Variable("a")
    n1= NumLiteral(3)
    e2 = BinOp("**", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == 27

    b = Variable("b")
    n2 = NumLiteral(10)
    e2 = BinOp("**", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == 1000

    """ Show an error of Invalid program from line 136"""
    # c = Variable("c")
    # n3 = NumLiteral(0)
    # e2 = BinOp("**", a, c)
    # e  = Let(a, n1, Let(b, n2,e2 ))
    # assert eval(e) == 0

    
def test_equal_operator():
    a  = Variable("a")
    n1= NumLiteral(3)
    e2 = BinOp("==", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == True

    b = Variable("b")
    n2 = NumLiteral(10)
    e2 = BinOp("==", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == False

def test_not_equal_operator():
    a  = Variable("a")
    n1= NumLiteral(3)
    e2 = BinOp("!=", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == False

    b = Variable("b")
    n2 = NumLiteral(10)
    e2 = BinOp("!=", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == True

def test_greter_than_operator():
    a  = Variable("a")
    n1= NumLiteral(3)
    e2 = BinOp(">", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == False

    b = Variable("b")
    n2 = NumLiteral(10)
    e2 = BinOp(">", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == True

def test_greter_than_equal_operator():
    a  = Variable("a")
    n1= NumLiteral(3)
    e2 = BinOp(">=", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == True

    b = Variable("b")
    n2 = NumLiteral(10)
    e2 = BinOp(">=", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == True

    c = Variable("c")
    n3 = NumLiteral(9)
    e2 = BinOp(">=", c, b)
    e  = Let(c, n3, Let(b, n2,e2 ))
    assert eval(e) == False

def test_less_than_operator():
    a  = Variable("a")
    n1= NumLiteral(3)
    e2 = BinOp("<", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == False

    b = Variable("b")
    n2 = NumLiteral(10)
    e2 = BinOp("<", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == False

    c = Variable("c")
    n3 = NumLiteral(9)
    e2 = BinOp("<", c, b)
    e  = Let(c, n3, Let(b, n2,e2 ))
    assert eval(e) == True

def test_less_than_equal_operator():
    a  = Variable("a")
    n1= NumLiteral(3)
    e2 = BinOp("<=", a, a)
    e  = Let(a, n1, e2)
    assert eval(e) == True

    b = Variable("b")
    n2 = NumLiteral(10)
    e2 = BinOp("<=", b, a)
    e  = Let(a, n1, Let(b, n2,e2 ))
    assert eval(e) == False

    c = Variable("c")
    n3 = NumLiteral(9)
    e2 = BinOp("<=", c, b)
    e  = Let(c, n3, Let(b, n2,e2 ))
    assert eval(e) == True

def test_unop():
    
    a=Variable("a")
    e1=NumLiteral(1) 
    e2=UnOp("++",e1)
    e3=UnOp("-",e1)
    e4=UnOp("--",e1)
    assert eval(e3)== -1
    assert eval(e2)==2
    assert eval(e4)== 0

    a=Variable("a")
    e1=NumLiteral(2)
    b=NumLiteral(1)
    e2=BinOp("+",b,BinOp("*",UnOp("--",e1),e1))     #1+((2--)*2) = 3
    assert eval(e2)==3
    
    
    e1=NumLiteral(10)
    b=NumLiteral(5)
    c=NumLiteral(2)
    e2=BinOp("+",UnOp("++",e1),BinOp("*",UnOp("-",c),b))     #(10++) + ((-2)*5) = 1
    assert eval(e2)==1

    a  = Variable("a")
    e1 = NumLiteral(5)
    e2 = BinOp("+", a, a)
    e3 = UnOp("++",Let(a, e1, BinOp("+", a, Let(a, e2, e2))))
    assert eval(e3)==26

def test_bit():
    # "Bitwise AND"
    a=NumLiteral(15)
    b=NumLiteral(4)
    c=BinOp("&",a,b)   
    assert eval(c)==4

    # "Bitwise OR"
    a=NumLiteral(12)
    b=NumLiteral(20)
    c=BinOp("|",a,b)
    assert eval(c)==28

    # "Bitwise XOR"
    a=NumLiteral(34)
    b=NumLiteral(41)
    c=BinOp("^",a,b)
    assert eval(c)==11

def test_ls_rs():
    
    # "Bitwise Right Shift"
    a=NumLiteral(10)
    b=NumLiteral(1)
    c=BinOp(">>",a,b)
    assert eval(c)==5

    # "Bitwise Left Shift"
    a=NumLiteral(8)
    b=NumLiteral(3)
    c=BinOp("<<",a,b)
    assert eval(c)==64

def test_printop():
    PrintOp(a>b)
    a=1
    b=PrintOp(a)
    assert eval(b)==1
    
    a=3
    b=2
    c=PrintOp(a>b)
    # d=eval(c)
    # print(d)              //True
    assert eval(c)== True

    c=PrintOp(a<b)
    # d=eval(c)
    # print(d)             //False
    assert eval(c)== False
    
    c=("This is an input string where a is ",a," b is ",b)
    d=PrintOp(c)
    assert eval(d) == ('This is an input string where a is ', 3, ' b is ', 2)
    # e=eval(d)
    # print(e)             //('This is an input string where a is ', 3, ' b is ', 2)

    #PrintOp()              //print operation without input will give TypeError

def test_division():
    a=FracLiteral(2)               #using FracLiteral We will always get a fraction output
    b=FracLiteral(4)
    c=BinOp("/",a,b)
    print(c)
    assert eval(c)== 1/2

    a=IntLiteral(9)                 #using IntLiteral We will always get an Integer output
    b=IntLiteral(4)
    c=BinOp("/",a,b)
    print(c)
    assert eval(c)== 2

    a=NumLiteral(5)                 #Using Numliteral We can get float values
    b=NumLiteral(2)
    c=BinOp("/",a,b)
    print(c)
    assert eval(c)== 2.5

    # a=IntLiteral(5)               #//If the opreands have different type Like Int and Fraction 
    # b=FracLiteral(2)
    # c=BinOp("/",a,b)
    # print(c)
    # assert eval(c)== 2.5

def test_string():

    a=StringLiteral("hello ")
    b=StringLiteral("world! ")
    c=StringOp("add",a,b)
    print(eval(c))
    print(eval(StringOp('length',c)))
   
    
    #concatenation of 3 words
    d=StringLiteral("This ")
    e=StringLiteral("is ")
    f=StringOp("add",d,e)
    g=StringLiteral("string")
    h=StringOp("add",f,g)
    print(eval(h))
    print(eval(StringOp('length',h)))

    #concatenation using Numliteral and Let should show error
    # a1=StringLiteral("dsdsd")
    # b1=NumLiteral(2)
    # c1=StringOp("add",a1,b1)
    # d1=Let(a1,b1,c1)
    # print(eval(d1))
    # print(eval(StringOp('length',d1)))

    #concatenation of a string with a empty string 
    a2=StringLiteral("Hello")
    b2=StringLiteral("")
    x=StringOp("add",a2,b2)
    print(eval(x))
    print(eval(StringOp('length',x)))

    y=StringLiteral("Welcome")
    slice = StringSlice("slice",y,1,5)
    print(eval(slice))
    assert eval(slice)=="elco"

    z=StringLiteral("HelloWorld")
    slice1=StringSlice("slice",z,3,8)
    print(eval(slice1))
    assert eval(slice1)=="loWor"

    y1=StringLiteral("Hello World")
    slice2=StringSlice("slice",y1,5,6)
    print(eval(slice2))
    assert(eval(slice2))==" "

    y2=StringLiteral("Rishi123")
    slice3=StringSlice("slice",y2,5,8)
    print(eval(slice3))
    assert(eval(slice3))=="123"

    #It gives error
    # y2=NumLiteral(2)
    # slice3=StringSlice("slice",y1,2,5)
    # print(eval(slice2))

def test_if_Else():

    a=NumLiteral(3)
    b=NumLiteral(4)
    condition=BinOp("<",a,b)
    conditonalBlock=IfElse(condition,NumLiteral(30),NumLiteral(12))
    print(eval(conditonalBlock))
    assert eval(conditonalBlock)==30

    a1=NumLiteral(10)
    b1=NumLiteral(6)
    condition1=BinOp("<",a1,b1)
    conditonalBlock=IfElse(condition1,StringLiteral("Ten is greater"),StringLiteral("Six is greater"))
    print(eval(conditonalBlock))
    assert eval(conditonalBlock)=="Six is greater"

    a=NumLiteral(0)
    b=NumLiteral(0)
    condition=BinOp("==",a,b)
    conditonalBlock=IfElse(condition,StringLiteral("Equal"),StringLiteral("Not Equal"))
    print(eval(conditonalBlock))
    assert eval(conditonalBlock)=="Equal"

    a=NumLiteral(10)
    b=NumLiteral(35)
    condition=BinOp("!=",a,b)
    conditonalBlock=IfElse(condition,StringLiteral("Not Equal"),StringLiteral("Equal"))
    print(eval(conditonalBlock))
    assert eval(conditonalBlock)=="Not Equal"

    a=NumLiteral(2)
    b=NumLiteral(3)
    e=BinOp("+",UnOp("-",a),BinOp("*",UnOp("++",a),b))
    condition=BinOp("==",e,NumLiteral(7))
    conditonalBlock=IfElse(condition,StringLiteral("Equal"),StringLiteral("Not Equal"))
    print(eval(conditonalBlock))
    assert eval(conditonalBlock)=="Equal"

    a=NumLiteral(4)
    b=NumLiteral(6)
    e1=BinOp("*",b,UnOp("++",BinOp("+", a,b)))
    condition1=BinOp("==",e1,NumLiteral(66))
    e2=BinOp("*",b,BinOp("-",UnOp("++",a),UnOp("--",b)))
    condition2=BinOp("==",e2,NumLiteral(0))
    conditonalBlock=IfElse(condition1,IfElse(condition2,StringLiteral("Equal To Zero"),StringLiteral("Not Equal To Zero")),StringLiteral("Not Equal to 66"))
    print(eval(conditonalBlock))
    assert eval(conditonalBlock)=="Equal To Zero"

test_div_operator()
test_modulus_operator()
test_power_operator()
test_floor_div_operator()
test_equal_operator()
test_not_equal_operator()
test_greter_than_operator()
test_less_than_operator()
test_less_than_equal_operator()

