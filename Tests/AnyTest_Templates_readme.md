# Write AnyScript Tests

This class template makes it easy to add different kind of assertions and tests to AnyScript. 

## To use:
```c++
#include "AnyTest_Templates.any"

Main = 
{
AnyVar t1 = 1;
AnyVar t2 = 2;

AnyIntVar Condition = eqfun(t1,t2);
ASSERT_TRUE(Val1=Condition);

ASSERT_EQ(Val1=t1, Val2=t2, Err="t1 and t2 are not equal");

};
```

## Available options:


|  Fatal assertion                             |  Nonfatal assertion                         | Verifies
| -------------------------------------------- | ------------------------------------------- | ----------------------------------------
|  ASSERT_TRUE(condition);                     |  EXPECT_TRUE(condition);                    | condition is true
|  ASSERT_FALSE(condition);                    |  EXPECT_FALSE(condition);                   | 


|  Fatal assertion                             |  Nonfatal assertion                         | Verifies
| -------------------------------------------- | ------------------------------------------- | ----------------------------------------
|  ASSERT_EQ(expected, actual);                |  EXPECT_EQ(expected, actual);               | expected == actual
|  ASSERT_NE(val1, val2);                      |  EXPECT_NE(val1, val2);                     | val1 != val2
|  ASSERT_LT(val1, val2);                      |  EXPECT_LT(val1, val2);                     | val1 < val2
|  ASSERT_LE(val1, val2);                      |  EXPECT_LE(val1, val2);                     | val1 <= val2
|  ASSERT_GT(val1, val2);                      |  EXPECT_GT(val1, val2);                     | val1 > val2
|  ASSERT_GE(val1, val2);                      |  EXPECT_GE(val1, val2);                     | 

## Some possible strings assertions that we haven't impletemented yet. 

|  Fatal assertion                             |  Nonfatal assertion                         | Verifies
| -------------------------------------------- | ------------------------------------------- | ----------------------------------------
|  ASSERT_STREQ(expected_str, actual_str);     |  EXPECT_STREQ(expected_str, actual_str);    | the two strings have the same content
|  ASSERT_STRNE(str1, str2);                   |  EXPECT_STRNE(str1, str2);                  | the two strings have different content
|  ASSERT_STRCASEEQ(expected_str, actual_str); |  EXPECT_STRCASEEQ(expected_str, actual_str);| the two strings have the same content, ignoring case
|  ASSERT_STRCASENE(str1, str2);               |  EXPECT_STRCASENE(str1, str2)               | 
