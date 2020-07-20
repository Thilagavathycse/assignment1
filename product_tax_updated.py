class ProductTaxCalculation:
    rule1=5/100#if the product price > 500
    rule2=2/100#if the product price <500
    rule3=3/100#if the product category is diary and price > 1000
    def __init__(self,product_id,product_name,product_price,product_category):
        self.id=product_id
        self.name=product_name
        self.price=product_price
        self.category=product_category.lower()
    def calculate_tax_and_print(self):
        if self.price>500 and self.category!="diary" and self.category!="textile":
            print("Product name:{} which has no VAT tax:{}".format(self.name,self.rule1*self.price))
        elif self.price < 500 and self.category!="diary" and self.category!="textile":
            print("Product name:{} which  has no VAT tax:{}".format(self.name,self.rule2*self.price))
        elif self.category=="diary" and self.price>1000:
            print("Product name:{} and additonal tax:{}".format(self.name,self.rule3*self.price))
        elif self.category=="diary" and self.price<1000:
            print("product name:{} and tax:{}".format(self.name,self.price))
def additional_tax(*ProductTaxCalculation):
    for item in ProductTaxCalculation:
        if item.category=="textile" and item.price>500:
            print("product name:{} and tax(VAT included):{}".format(item.name,(item.rule1*item.price+((1/100)*item.price))))
        elif item.category =="textile" and item.price<500:
            print("product name:{} and tax(VAT included):{}".format(item.name,(item.rule2*item.price+((1/100)*item.price))))
        else:
            pass#future implementation when rules are added
product1=ProductTaxCalculation(11,"fresh juice",1200,"produce")
product2=ProductTaxCalculation(11,"Tshirt",1200,"textile")
product3=ProductTaxCalculation(13,"cheese",1200,"Diary")
product4=ProductTaxCalculation(14,"door mat",200,"Homeneeds")
product5=ProductTaxCalculation(15,"jeans",250,"textile")
product6=ProductTaxCalculation(16,"kitkat",120,"diary")
product1.calculate_tax_and_print()
product2.calculate_tax_and_print()
product3.calculate_tax_and_print()
product4.calculate_tax_and_print()
product5.calculate_tax_and_print()
product6.calculate_tax_and_print()
additional_tax(product1,product2,product3,product4,product5,product6)
