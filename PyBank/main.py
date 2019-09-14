import os
import csv
PyBank_budget = os.path.join('..', 'budget_data.csv')
with open (PyBank_budget, newline='') as csvfile:
    csv_file = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    date = []
    profit_loss = []
    for row in csv_file:
        date.append(row[0])
        profit_loss.append(row[1])

#print(date)
#print(profit_loss)

#PART 1
date2 = [x[:3] for x in date]
#print(date2)
number_months= len(date2)
#print(number_months)

#PART 2
newlist = []
for i in profit_loss:
    x = int(i)
    newlist.append(x)
#print(newlist)


profit_loss_int = [int(x) for x in profit_loss]
#print(profit_loss_int)
net_profit_loss=sum(profit_loss_int)
print(net_profit_loss)

average_change = []
#print(range(len(profit_loss) - 1))

#PART 3
a = range(len(profit_loss) - 1)
for i in a:
    x = profit_loss_int[i]
    y = profit_loss_int[i+1]
    change = y - x
    average_change.append(change)
average_change_2=sum(average_change)
average_change_pl=(average_change_2)/int(number_months-1)
#print(average_change_pl)

#PART 4 + 5
change_dates = date[1:]


zipped = list(zip(change_dates, average_change))
max_month = max(average_change)
min_month = min(average_change)
print(zipped)
for i in zipped:
    if i[1] == max_month:
        max_both = [i[0], i[1]]
       
    if i[1] == min_month:
        min_both = [i[0], i[1]]
        
#print(max_both[0], max_both[1])
#print(min_both[0], max_both[1])

print("Financial Analysis")
print("______________________________________________________________________")
print("Total Months: " + str(number_months))
print("Total Profit/Loss: " + "$" + str(net_profit_loss))
print("Average Change: " + "$" + str(average_change_pl))
print("Greatest Increase in Profits: " + str(max_both[0]) + "($" + str(max_both[1]) + ")")
print("Greatest Increase in Profits: " + str(min_both[0]) + "($" + str(min_both[1]) + ")")

with open("outputPyBank.txt","w") as csv_output:
    output = csv.writer(csv_output, delimiter=",")
    output.writerow(["Financial Analysis"])
    output.writerow(["______________________________________________________________________"])
    output.writerow(["Total Months: " + str(number_months)])
    output.writerow(["Total Profit/Loss: " + "$" + str(net_profit_loss)])
    output.writerow(["Average Change: " + "$" + str(average_change_pl)])
    output.writerow(["Greatest Increase in Profits: " + str(max_both[0]) + "($" + str(max_both[1]) + ")"])
    output.writerow(["Greatest Increase in Profits: " + str(min_both[0]) + "($" + str(min_both[1]) + ")"])

# file.close()


    




    
    