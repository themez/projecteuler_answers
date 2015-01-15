isMultipleOf x y = (mod y x == 0)
--main = print ( sum (filter (\x->(isMultipleOf 5 x || isMultipleOf 3 x)) [1..999]) )

main = print ([x| xs <- [1..999], (isMultipleOf 5 x || isMultipleOf 3 x)==True <- xs])