class ProductTaxCalculation:
    available_category=["textile"," diary","Produce","Homeneeds"]

    def __init__(self,product_id,product_name,product_price,product_category):
        self.id=product_id
        self.name=product_name
        self.price=product_price
        self.category=product_category.lower()
    def calculate_tax_and_print(self):
        if self.price > 500 and self.category!="textile" and self.category!="diary":
            self.tax=(5/100)*self.price
            print("Product name:{} has no VAT tax:{}".format(self.name,str(self.tax)))
        elif self.price < 500 and self.category!="textile" and self.category!="diary":
            self.tax=(2/100)*self.price
            print("Product name:{} has no VAT tax:{}".format(self.name,str(self.tax)))
        else:
            pass
def additional_tax(*ProductTaxCalculation):
    for item in ProductTaxCalculation:
        if item.category=="textile" and item.price>500:
            add_tax=(5/100)*item.price+((1/100)*item.price)
            print("product name:{} and tax(VAT included):{}".format(item.name,str(add_tax)))
        elif item.category =="textile" and item.price<500:
            add_tax=(2/100)*item.price+((1/100)*item.price)
            print("product name:{} and tax(VAT included):{}".format(item.name,str(add_tax)))
        elif item.category =="diary" and item.price>1000:
            add_tax=(5/100)*item.price+((3/100)*item.price)
            print("product name:{} and tax(VAT included):{}".format(item.name,str(add_tax)))
        else:
            pass
product1=ProductTaxCalculation(11,"fresh juice",1200,"produce")
product2=ProductTaxCalculation(11,"Tshirt",1200,"textile")
product3=ProductTaxCalculation(13,"cheese",1200,"Diary")
product4=ProductTaxCalculation(14,"door mat",200,"Homeneeds")
product5=ProductTaxCalculation(14,"jeans",200,"textile")
product1.calculate_tax_and_print()
product2.calculate_tax_and_print()
product3.calculate_tax_and_print()
product4.calculate_tax_and_print()
product5.calculate_tax_and_print()
additional_tax(product1,product2,product3,product4,product5)
