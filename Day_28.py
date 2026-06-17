'''
   MATPLOTLIB
   ----------
   --> this is a library in python for data visuailzation ,allowing users to create a variety of plots

   ##basic structure of matplotlib:
   1.figure
   2.axis
   3.grid
   4.title
   5.legend (used only in piechart
   
##bar graph
import matplotlib.pyplot as plt
sales=['A','B','C']
values=[25,30,45]
plt.bar(sales,values,color='purple',edgecolor='black')
plt.xlabel('CAR MODELS')
plt.ylabel('VALUES')
plt.title('BMW SALES')
plt.show()

##line graph
import matplotlib.pyplot as plt
overs=[1,2,3,4,5]
score=[4,9,17,20,8]
plt.plot(overs,score,color='purple')
plt.title('SCORE CARD')
plt.xlabel('OVERS')
plt.ylabel('SCORE')
plt.show()

##piechart
import matplotlib.pyplot as plt
subjects=['python','java','c']
students=[35,7,15]
plt.pie(students,labels=subjects,autopct='%1.1f%%')
plt.legend(subjects)
plt.title('STUDENTS IN DIFFERENT COURSES')
plt.show()

##scatterplot
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,15,18,20,13]
plt.scatter(x,y,color='purple')
plt.title('SCATTER PLOT')
plt.xlabel('X VALUES')
plt.ylabel('Y VALUES')
plt.show()

##histogram
import matplotlib.pyplot as plt
y=[10,15,18,20,13]
plt.hist(y,color='purple')
plt.title('HISTOGRAM')
plt.xlabel('X VALUES')
plt.ylabel('Y VALUES')
plt.show()

##task bar graph
import matplotlib.pyplot as plt
year=[2022,2023,2024,2025,2026]
sales=[200,345,465,543,1240]
plt.bar(year,sales,color='purple',edgecolor='black')
plt.xlabel('YEARS')
plt.ylabel('SALES')
plt.title('HYUNDAI')
plt.show()

##task pie chart
import matplotlib.pyplot as plt
companies=['HYUNDAI','KIA','BMW','SUZUKI']
sales=[5554,756,1523,4567]
plt.pie(sales,labels=companies,autopct='%1.1f%%')
plt.legend(companies)
plt.title('DIFFERENT COMPANY SALES')
plt.show()
'''
