import testmod

test_class_1 = testmod.TestClass()
test_class_1.test_method('1')

from testmod import TestClass

test_class_2 = TestClass()
test_class_2.test_method('2')

from datetime import datetime

print(datetime.today())

from datetime import datetime as d

print(d.today())
