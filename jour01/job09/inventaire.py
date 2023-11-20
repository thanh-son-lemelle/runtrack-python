nom="pâte panzani"
prix_unit="1.26"
before_stock=100
ask_quantity=0
input( __prompt:renseigner la quantité demandé: ask_quantity =" ")
after_stock=(before_stock - ask_quantity)
print(after_stock)