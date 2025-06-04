def extract_invoice_details(invoice):
    parts = invoice.split()

    prod_start_idx = parts.index("for") + 1
    prod_end_idx = parts.index("of")
    product = " ".join(parts[prod_start_idx:prod_end_idx])

    price = int(parts[parts.index("USD") - 1])
    date = parts[-1][:-1]

    return {
        "product": product,
        "amount": price,
        "date": date
    }


print(extract_invoice_details("Invoice for Macbook Pro of amount 1200 USD issued on 2024-05-01."))