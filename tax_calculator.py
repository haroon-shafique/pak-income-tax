#!/usr/bin/python3

print("Income Tax Calculation on Salaries in Pakistan")

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

monthly_taxable_income = int(input("Input Monthly Salary (Taxable): "))
yearly_taxable_income  = 12 * monthly_taxable_income

current_slab        = 0
current_tax_percent = 0
current_base_tax    = 0
for slab_value in tax_slabs_dict.values():
  slab        = slab_value[0]
  tax_percent = slab_value[1]
  base_tax    = slab_value[2]

  if (yearly_taxable_income > current_slab and yearly_taxable_income <= slab):
    print("")
    print("Tax Slab:",       current_slab)
    print("Tax Percentage:", current_tax_percent)
    print("Base Tax:",       current_base_tax)
    break
  else:
    current_slab        = slab
    current_tax_percent = tax_percent
    current_base_tax    = base_tax

yearly_income_tax  = current_base_tax + (yearly_taxable_income - current_slab) * (current_tax_percent / 100)
monthly_income_tax = yearly_income_tax / 12

yearly_income_after_tax  = yearly_taxable_income - yearly_income_tax
monthly_income_after_tax = monthly_taxable_income - monthly_income_tax

print("")
print("Monthly Income (Taxable):", monthly_taxable_income)
print("Monthly Income Tax:", monthly_income_tax)
print("Monthly Income (Taxable) after Tax:", monthly_income_after_tax)
print("")
print("Yearly Income (Taxable):", yearly_taxable_income)
print("Yearly Income Tax:", yearly_income_tax)
print("Yearly Income (Taxable) after Tax:", yearly_income_after_tax)
