def LinearSearchProduct(ProductList,targetProduct):
 indices=[]
 for index,Product in
enumerate(ProductList):
  if Product==targetProduct:
     indices.append(index)
    return indices
#example usage
Products=["shoes","boat","loafer","shoes","sandal","shoes"]
target="shoes"
target2="apple"
result=LinearSerachProduct(Products, target)
print(result)
 