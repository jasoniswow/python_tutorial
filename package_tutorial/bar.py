# script to test package "bar"

from bar.bar_tab import Tab


table1 = Tab()
table1.add('soft')
table1.add('chicken')
table1.add('desert')
table1.print_bill(5,15) # tax and tip


table2 = Tab()
table2.add('beef')
table2.add('wine')
table2.print_bill(5,20)


