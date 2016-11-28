import tvm

def test_const():
    x = tvm.const(1)
    assert x.dtype == 'int32'
    assert isinstance(x, tvm.expr.IntImm)

def test_make():
    x = tvm.const(1)
    y = tvm.make.IntImm('int32', 1)
    z = x + y
    print(z)

def test_ir():
    x = tvm.const(1)
    y = tvm.make.IntImm('int32', 1)
    z = x + y
    stmt = tvm.make.Evaluate(z)
    assert isinstance(stmt, tvm.stmt.Evaluate)

def test_let():
    x = tvm.Var('x')
    y = tvm.Var('y')
    stmt = tvm.make.LetStmt(
        x, 10, tvm.make.Evaluate(x + 1), y, "stride")
    assert stmt.attr_of_node == y
    print(stmt)


def test_basic():
    a = tvm.Var('a')
    b = tvm.Var('b')
    c =  a + b
    assert str(c) == '(%s + %s)' % (a.name, b.name)

def test_array():
    a = tvm.convert([1,2,3])

def test_stmt():
    x = tvm.make.Evaluate(0)
    tvm.make.For(tvm.Var('i'), 0, 1,
                 tvm.stmt.For.Serial, 0,
                 x)


if __name__ == "__main__":
    test_const()
    test_make()
    test_ir()
    test_basic()
    test_stmt()
    test_let()