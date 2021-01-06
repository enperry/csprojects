# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None


def create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, "%Y-%m-%d")
    entry.description = description
    entry.change = change
    return entry

def change_str(entry, currency, locale):
    currency_signs = {"USD": "$", "EUR": u"€"}
    separators = {"nl_NL": ",", "en_US": "."}
    part_join = {"nl_NL": ".", "en_US": ","}
    currency_sign = currency_signs[currency]
    res = currency_sign + " "
    start_str = end_str = ""
    if(locale == "nl_NL" and entry.change < 0):
        res = res + "-"
    elif(locale == "en_US"):
        res = ""
        if(entry.change < 0):
            start_str = "("
            end_str = ")"
        res = res + currency_sign
    change = abs(int(entry.change / 100.0))
    res = res + f"{change:,}".replace(",", part_join[locale])
    res = res + separators[locale]
    change_cents = str(abs(entry.change) % 100)
    if(len(change_cents) < 2):
        change_cents = "0" + change_cents
    res = res + change_cents
    if(locale == "nl_NL" or entry.change >= 0):
        res = res + " "
    res = start_str + res + end_str
    res = " " * (13 - len(res)) + res
    return res

def gen_entry_description(entry):
    # Truncate if necessary
    if(len(entry.description) > 25):
        desc = entry.description[:22] + "..."
    else:
        desc = entry.description + " " * (25 - len(entry.description))
    desc = desc + " | "
    return desc

def gen_date(entry, locale):
    if(locale == "en_US"):
        return entry.date.strftime("%m/%d/%Y")
    elif(locale == "nl_NL"):
        return entry.date.strftime("%d-%m-%Y")
    else:
        raise ValueError("Invalid locale")

def format_entries(currency, locale, entries):
    headers = {"en_US": "Date" + (" " * 7) + "| Description" + " " * 15 + "| Change" + " " * 7,
               "nl_NL": "Datum" + 6 * " " + "| Omschrijving" + 14 * " " + "| Verandering" + 2 * " "}
    table = headers[locale]
    sorted_entries = sorted(entries, key = lambda e: (e.date, e.change, e.description))
    for entry in sorted_entries:
        table = table + "\n"
        table = table + gen_date(entry, locale)
        table = table + " | "
        table = table + gen_entry_description(entry)
        table = table + change_str(entry, currency, locale)
    return table