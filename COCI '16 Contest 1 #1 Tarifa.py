'''
Solution by Tuan Vuong
Pero has negotiated a Very Good data plan with his internet provider. The provider will let Pero use up X megabytes to surf the internet per month. Each megabyte that he doesn't spend in that month gets transferred to the next month and can still be spent. Of course, Pero can only spend the megabytes he actually has.

If we know how many megabytes Pero has spent in each of the first  months of using the plan, determine how many megabytes Pero will have available in the  month of using the plan
'''

monthly_mb = int(input())
n = int(input())
total_mb = monthly_mb * (n + 1)
for i in range(n):
    used = int(input())
    total_mb = total_mb - used
    
print(total_mb)

'''
Sample Input 1
10
3
4
6
2
Sample Output 1
28
Explanation for Sample Output 1
In the first month, out of  total megabytes, Pero has spent  and transferred  into the next month. In the second month, out of   total megabytes, Pero has spent  and transferred . In the third month, out of   total megabytes, Pero has spent  and transferred . In the fourth month, he had a total of  megabytes to spend.

Sample Input 2
10
3
10
2
12
Sample Output 2
16
Sample Input 3
15
3
15
10
20
Sample Output 3
15
'''
