from pyscript import display

shop_name = "cosmic veil jewelry" # string
owner_name = "apky" # string
year_established = 2025 # integer
popular_item_price = 50.00 # float
delivery_serv = True # boolean
product_names = ["silver sparkle earrings", "simple star necklace", "gothic silver ring set"] #list
product_prices = {"earrings": 50, "necklace": 80, "ring set": 42} # dictionary
common_allergens = ["nickel", "copper", "lead"] # list
tax_rate = 0.08 # float


display(f'welcome to {shop_name}',target='div1')
display(f'im {owner_name} the owner of this establishment', target='div1')
display(f'established on {year_established}', target='footer')

