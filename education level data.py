//frequency distribution of 'Education_Level'

education_level_counts = df['Education_Level'].value_counts()
print(education_level_counts)

//pie Chart based on Education level 

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8))
plt.pie(education_level_counts, labels=education_level_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribution of Education Level')
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
