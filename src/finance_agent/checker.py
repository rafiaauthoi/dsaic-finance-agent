def check_line_items(items):
    accumulator = 0
    list_errors = []
    for line_item in items:
        item, vendor, cost, amount = [line_item["item"], line_item["vendor"], line_item["cost"], line_item["amount"]]
        accumulator += 1

        # SUB 26
        if item == "" and amount != "":
            list_errors.append(f"#SUB 26:\nLine {accumulator} requests ${amount} but has no item description. Fill in Item Requesting to explain what this amount is for, or remove the request.\n")
        
        #SUB 28
        elif item != "":
            if vendor == "" and amount == "":
                list_errors.append(f"#SUB 28:\nLine {accumulator} item '{item}' is missing Vendor Name. Enter the vendor name for this item.\n"
                                   f"Line {accumulator} item '{item}' is missing Amount Requesting. Enter the amount you want WSAAC to fund.\n")
            elif vendor == "" and amount != "":
                list_errors.append(f"#SUB 28:\nLine {accumulator} item '{item}' is missing Vendor Name. Enter the vendor name for this item.\n")
            elif amount == "" and vendor != "":
                list_errors.append(f"#SUB 28:\nLine {accumulator} item '{item}' is missing Amount Requesting. Enter the amount you want WSAAC to fund.\n")
        
    return list_errors

if __name__ == "__main__":
    test_items = [
        # SUB-26: Breaks the rule
        {"item": "", "vendor": "Example Supply Shop", "cost": "20", "amount": "20"},

        # SUB-26: Follows the rule
        {"item": "Dry-erase markers", "vendor": "Example Supply Shop", "cost": "20", "amount": "20"},

        # SUB-28: Breaks the rule (missing amount)
        {"item": "Poster printing", "vendor": "Example Print Shop", "cost": "40", "amount": ""},

        # SUB-28: Follows the rule
        {"item": "Poster printing", "vendor": "Example Print Shop", "cost": "40", "amount": "40"},

        # Additional SUB-28 test: missing vendor
        {"item": "Club banners", "vendor": "", "cost": "60", "amount": "60"},
    ]
    
    errors = check_line_items(test_items)
    for error in errors:
        print(error)