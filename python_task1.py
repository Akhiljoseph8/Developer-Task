giftA = 0
giftB = 0
giftC = 0

productA = int(input("Enter Number of Product A: "))
if productA > 0:
    giftA = int(input("How many Product A wrapped as gift: "))
    if giftA > productA:
        giftA = int(input("Number of product A as gift is greater than total Product A\nHow many Product A wrapped as gift: "))

productB = int(input("Enter Number of Product B: "))
if productB > 0:
    giftB = int(input("How many Product B wrapped as gift: "))
    if giftB > productB:
        giftB = int(input("Number of product B as gift is greater than total Product B\nHow many Product B wrapped as gift: "))

productC = int(input("Enter Number of Product C: "))
if productC > 0:
    giftC = int(input("How many Product C wrapped as gift: "))
    if giftC > productC:
        giftC = int(input("Number of product C as gift is greater than total Product C\nHow many Product C wrapped as gift: "))

wrap = giftA + giftB + giftC

def total_price(a, b, c):
    return (a * 20) + (b * 40) + (c * 50)

def flat_ten_discount(total):
    if total > 200:
        total -= 10
    return total

def bulk_five_discount(a, b, c, total):
    if a > 10:
        total -= (a * 20) * 0.05
    if b > 10:
        total -= (b * 40) * 0.05
    if c > 10:
        total -= (c * 50) * 0.05
    return total

def bulk_ten_discount(a, b, c, total):
    if a + b + c > 20:
        total -= total * 0.1
    return total

def tiered_fifty_discount(a, b, c, total):
    total_quantity = a + b + c
    if total_quantity > 30:
        if a > 15:
            m = a - 15
            total -= (m * 20) * 0.5
        if b > 15:
            m = b - 15
            total -= (m * 40) * 0.5
        if c > 15:
            m = c - 15
            total -= (m * 50) * 0.5
    return total

def shipping_fee(a, b, c):
    t = (a + b + c) / 10
    ship = (t * 5) if t.is_integer() else (int(t) + 1) * 5
    return ship

total = total_price(productA, productB, productC)
flatTen = flat_ten_discount(total)
bulkFive = bulk_five_discount(productA, productB, productC, total)
bulkTen = bulk_ten_discount(productA, productB, productC, total)
tiredTen = tiered_fifty_discount(productA, productB, productC, total)
shippingFee = shipping_fee(productA, productB, productC)

discountName = ''
if flatTen == total and bulkFive == total and bulkTen == total and tiredTen == total:
    discountName = "No discount"
    discountPrice = total
elif flatTen <= bulkFive and flatTen <= bulkTen and flatTen <= tiredTen:
    discountName = "flat_10_discount"
    discountPrice = flatTen
elif bulkFive <= flatTen and bulkFive <= bulkTen and bulkFive <= tiredTen:
    discountName = "bulk_5_discount"
    discountPrice = bulkFive
elif bulkTen <= flatTen and bulkTen <= bulkFive and bulkTen <= tiredTen:
    discountName = "bulk_10_discount"
    discountPrice = bulkTen
else:
    discountName = "tiered_50_discount"
    discountPrice = tiredTen

print(f"Product A : {productA}   {productA * 20}$ ")
print(f"Product B : {productB}   {productB * 40}$ ")
print(f"Product C : {productC}   {productC * 50}$ ")
print(f"Subtotal  :     {total}$")
print(f"Discountname   : {discountName}")
print(f"DiscountAmuont : {total - discountPrice}$")
print(f"Shipping Fee   : {shippingFee}$")
print(f"Wrap Fee       : {wrap}$")
print(f"Total          : {discountPrice + shippingFee + wrap}$")