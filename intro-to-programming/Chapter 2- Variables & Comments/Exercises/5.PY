
total_money = 50
usb_price = 6


num_usb_sticks = total_money // usb_price


money_left = total_money % usb_price


print(f"The girl can buy {num_usb_sticks} USB sticks.")
print(f"She will have £{money_left} left.")
