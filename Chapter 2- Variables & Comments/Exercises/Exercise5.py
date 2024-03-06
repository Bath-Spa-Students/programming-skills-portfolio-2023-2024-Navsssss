total_budget = 50

usb_cost = 6

num_usb_sticks = total_budget // usb_cost

remaining_money = total_budget % usb_cost

print(f"With £{total_budget}, she can buy {num_usb_sticks} USB sticks and will have £{remaining_money} left.")
