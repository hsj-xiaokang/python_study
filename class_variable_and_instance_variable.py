#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
"""
python的类变量和成员变量
类似于JavaScript方式，类属性和类方法就在prototype上面
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title>JavaScript测试类属性和实例对象属性</title>
	</head>
	<body>
	<script type="text/javascript">
		function test(){
           //TODO
		}
       test.prototype.nameTest = 'hsj-create-2019/06/03';
	   //undefined
	   console.log(test.nameTest);
	   var instanceTest = new test();
	   //hsj-create-2019/06/03
	   console.log(instanceTest.nameTest);
	   instanceTest.nameTest = 'hsj-create-2019/06/03-new';
	   //hsj-create-2019/06/03-new
	   console.log(instanceTest.nameTest);
	   //hsj-create-2019/06/03
	   console.log(instanceTest.__proto__.nameTest);
	</script>
</html>

"""


class TestClass(object):
    val1 = 'name class'
    val2 = []

    def __init__(self):
        self.name = 'name class - init'
        self.addr = [8]


if __name__ == '__main__':
    inst = TestClass()
    inst1 = TestClass()

    print(TestClass.val1)
    print(inst.val1)
    print(inst1.val1)

    print(TestClass.val2)
    print(inst.val2)
    print(inst1.val2)

    # print(inst.name)
    # print(inst1.name)
    # print(inst.addr)
    # print(inst1.addr)

    print('=======================')

    TestClass.val1 = 'name class v1'
    print(TestClass.val1)
    print(inst.val1)
    print(inst1.val1)

    TestClass.val2.append(1)
    print(TestClass.val2)
    print(inst.val2)
    print(inst1.val2)

    # inst.name = 'name class -init -change'
    # print(inst.name)
    # print(inst1.name)
    # print(inst.addr)
    # print(inst1.addr)

    print('=======================')

    inst.val1 = 'name class v2'
    print(TestClass.val1)
    print(inst.val1)
    print(inst1.val1)

    inst.val2.append(2)
    print(TestClass.val2)
    print(inst.val2)
    print(inst1.val2)

    # inst.addr.append(9)
    # print(inst.name)
    # print(inst1.name)
    # print(inst.addr)
    # print(inst1.addr)
