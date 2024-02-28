# import class Lotto
from lotto import Lotto

# create an instance of class Lotto
lotto1 = Lotto()
# object lotto1 calls setter method for its attribute __lotto_set
lotto1.set_lotto()
# print first lotto set
print("\nlotto set 1:", lotto1.get_lotto())
# prints no. of objects created so far
print("Objects created =", Lotto.obj_count)

# create another instance
lotto2 = Lotto()
# object lotto2 calls setter method
lotto2.set_lotto()
# print second lotto set
print("\nlotto set 2:", lotto2.get_lotto())
# prints no. of objects created
print("Objects created =", Lotto.obj_count)
