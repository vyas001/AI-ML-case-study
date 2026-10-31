# quickmart_billing.py - QuickMart Billing System
cart = [
{"name": "Notebook", "category": "Stationery", "price": 40, "qty": 5},
{"name": "Pen", "category": "Stationery", "price": 10, "qty": 11},
{"name": "Biscuits", "category": "Snacks", "price": 25, "qty": 4},
{"name": "Juice", "category": "Drinks", "price": 45, "qty": 3},
{"name": "Chips", "category": "Snacks", "price": 20, "qty": 6},
]

def line_total(item):
    return item["price"] * item["qty"]

def subtotal(cart):
    sum=0
    for i in range(len(cart)) :
        sum+=line_total(cart[i])
    return sum

def apply_discount(amt,per=0):
    dis=amt*per/100
    return amt-dis

def gst(amt,per=18):
    tax=amt*per/100
    return tax

def category_totals(cart):
    totals = {}
    for item in cart:
        totals[item["category"]] = totals.get(item["category"], 0) + line_total(item)
    return totals

def top_items(cart,n=2):
    sorted_cart=sorted(cart,key=line_total,reverse=True)
    return [item['name'] for item in sorted_cart[:n]]

def print_bill(cart,disc_per=0):
    print(f'{'Item':<10}{'Price':>6}{'Qty':>5}{'Total':>8}')
    print('-'*29)
    for items in cart:
        print(f'{items['name']:<10}{items['price']:>6}{items['qty']:>5}{line_total(items):>8}')
    print('-'*29)
    print(f'Subtotal{subtotal(cart):>21.2f}')
    print(f'Discount 10% {subtotal(cart)/10:>16.2f}')
    print(f'GST 18% {gst(apply_discount(subtotal(cart),10),18):>21.2f}')
    print(f'Grand total{apply_discount(subtotal(cart),10)+gst(apply_discount(subtotal(cart),10),18):>18.2f}')


def main():
    print("Task 1: Line total")
    print(line_total(cart[0]))
    print("\nTask 2: Subtotal")
    print(subtotal(cart))
    print("\nTask 3: Discount")
    print(apply_discount(500))
    print(apply_discount(500, 10))
    print("\nTask 4: GST")
    print(gst(100))
    print(gst(100, 5))
    print("\nTask 5: Category totals")
    for cat, total in sorted(category_totals(cart).items()):
        print(f"{cat:<12}{total}")
    print("\nTask 6: Top items")
    print(top_items(cart))
    print(top_items(cart, 3))
    print("\nTask 7: Bill")
    print_bill(cart, 10)
    
main()


