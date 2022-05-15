#!/usr/bin/python3

print("Income Tax Calculation on Salaries in Pakistan")

print("")
print("Usage:")
print("You'll need to input taxable income for each month separately in the current version")
print("")

# Set to True for Verbose Printing
debug = False

months_dict = {
  0 : "Jul",
  1 : "Aug",
  2 : "Sep",
  3 : "Oct",
  4 : "Nov",
  5 : "Dec",
  6 : "Jan",
  7 : "Feb",
  8 : "Mar",
  9 : "Apr",
  10: "May",
  11: "Jun",
}


#               [slab, tax_percent, base_tax]
tax_slabs_dict = {
  "slab_5"    : [600000,   5,    0       ],
  "slab_10"   : [1200000,  10,   30000   ],
  "slab_15"   : [1800000,  15,   90000   ],
  "slab_17.5" : [2500000,  17.5, 195000  ],
  "slab_20"   : [3500000,  20,   370000  ],
  "slab_22.5" : [5000000,  22.5, 670000  ],
  "slab_25"   : [8000000,  25,   1345000 ],
  "slab_27.5" : [12000000, 27.5, 2345000 ],
  "slab_30"   : [30000000, 30,   7295000 ],
  "slab_32.5" : [50000000, 32.5, 13295000],
  "slab_35"   : [75000000, 35,   21420000]
}

tax_deduction_dict = {}
total_taxable_income = 0
total_tax_deducted = 0

for n_month in range(0, 12):
  this_month_taxable_income = int(input("Input Taxable Salary for %s: " % (months_dict[n_month])))
  yearly_taxable_income     = total_taxable_income + ((12 - n_month) * this_month_taxable_income)

  current_slab        = 0
  current_tax_percent = 0
  current_base_tax    = 0

  for slab_value in tax_slabs_dict.values():
    slab        = slab_value[0]
    tax_percent = slab_value[1]
    base_tax    = slab_value[2]

    if (yearly_taxable_income > current_slab and yearly_taxable_income <= slab):
      if (debug):
        print("")
        print("Tax Slab:",       current_slab)
        print("Tax Percentage:", current_tax_percent)
        print("Base Tax:",       current_base_tax)
      break
    else:
      current_slab        = slab
      current_tax_percent = tax_percent
      current_base_tax    = base_tax

  yearly_income_tax     = current_base_tax + (yearly_taxable_income - current_slab) * (current_tax_percent / 100)
  this_month_income_tax = (yearly_income_tax - total_tax_deducted) / (12 - n_month)

  yearly_income_after_tax  = yearly_taxable_income - yearly_income_tax
  monthly_income_after_tax = this_month_taxable_income - this_month_income_tax

  print("")
  print("%s Income (Taxable): Rs." % (months_dict[n_month]), this_month_taxable_income)
  print("%s Income Tax: Rs." % (months_dict[n_month]), this_month_income_tax)
  print("%s Income (Taxable) after Tax: Rs." % (months_dict[n_month]), monthly_income_after_tax)
  if (debug):
    print("")
    print("Yearly Income (Taxable): Rs.", yearly_taxable_income)
    print("Yearly Income Tax: Rs.", yearly_income_tax)
    print("Yearly Income (Taxable) after Tax: Rs.", yearly_income_after_tax)

  total_taxable_income += this_month_taxable_income
  total_tax_deducted   += this_month_income_tax

  if (n_month < 11):
    print("")
    do_calculate_next = input("Want to calculate for next month (y/n)? ").lower()
    print("")
    if (do_calculate_next == "n"):
      break
    else:
      continue

print("")
print("Total Income (Taxable): Rs.", total_taxable_income)
print("Total Tax Deducted: Rs.", total_tax_deducted)
