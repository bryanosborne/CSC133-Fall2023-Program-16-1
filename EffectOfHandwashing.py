######################################################
#  Your info here
######################################################
# Dr. Ignaz Semmelweis was a Hungarian physician born in 1818 and active at the Vienna General Hospital.
# in the early 1840s at the Vienna General Hospital as many as 10% of the women giving birth were dying.
# An overwhelming number of women were dying from childbed fever, a deadly disease affecting women that
# just have given birth. Semmelweis suspected the cause was the contaminated hands of the doctors
# delivering the babies. An examination of data from clinics in Vienna helped him to prove his hypothesis
# and save lives. Let’s look at the data ourselves.

#Import pandas, numpy, matplotlib.pyplot, and seaborn


###### Variables ######
# yearly data filename
yearly_dataset:str = ...
# monthly data filename
monthly_dataset:str ...

# Use pandas read_csv() to read the yearly dataset
yearly_df = ...
# Use pandas read_csv() to read the monthly dataset
monthly_df = ...

###### Initial look at the yearly dataset ######
# Print the dataset
print(...)

###### Visualizations of the yearly dataset ######
# Plot the deaths by year and by clinic
# Create a dodged bar graph of the number of deaths by year by clinic using Seaborn barplot()
sns.barplot(...)
plt.title(...)
plt.xlabel(...)
plt.ylabel(...)
plt.show()

# The table above shows the number of women giving birth at the two clinics
# at the Vienna General Hospital for the years 1841 to 1846. You'll notice that
# giving birth was very dangerous; an alarming number of women died as the
# result of childbirth, most of them from childbed fever.

# To make the analysis easier, we can calculate the proportion of deaths.
# Add a new feature, "Percentage of Deaths" to the dataframe which is the 
# number of deaths divided by the sum of the births and deaths
yearly_df["Percentage of Deaths"] = ...
print(yearly_df)

# Create a dodged bar graph of the percentage of deaths by year by clinic using Seaborn barplot()
sns.barplot(...)
plt.title(...)
plt.xlabel(...)
plt.ylabel(...)
plt.show()

# Compare the proportion of deaths between the two clinics. What do you notice?
# Semmelweis saw the same pattern and was puzzled and distressed. The only difference
# between the clinics was that many medical students served at Clinic 1, while mostly
# midwife students served at Clinic 2. While the midwives only tended to the women giving
# birth, the medical students also spent time in the autopsy rooms examining corpses.

# Semmelweis started to suspect that something on the corpses spread from the hands of
# the medical students, caused childbed fever. So in a desperate attempt to stop the
# high mortality rates, he decreed: Wash your hands! This was an unorthodox and controversial
# request, nobody in Vienna knew about bacteria at this point in time.

# Let's load in monthly data from Clinic 1 to see if the handwashing had any effect.

###### Initial look at the monthly dataset ######
# Print the dataset
print(...)
 
###### Visualizations of the monthly dataset ######
# As before, add a new feature, "Percentage of Deaths" to the dataframe which is the 
# number of deaths divided by the sum of the births and deaths
monthly_df["Percentage of Deaths"]= ...

# Change the data type of "date" column from string to datetime
# print(monthly_df.dtypes)
monthly_df['date'] =  pd.to_datetime(monthly_df['date'])

# Print the dataset again to make sure looks OK
print(...)

# Create a line graph of the percentage of deaths for Clinic 1 using Seaborn lineplot()
sns.lineplot(...)
plt.title(...)
plt.xlabel(...)
plt.ylabel(...)
plt.show()

# With the data loaded we can now look at the proportion of deaths over time.
# In the plot below we haven't marked where obligatory handwashing started,
#  but it reduced the proportion of deaths to such a degree that you should be able to spot it!


# Split monthly into two dataframes, i.e., create one dataframe with data before handwashing,
# and another dataframe with data from after handwashing
before_washing = ...
after_washing = ...

# Create a line graph of the two datasets just created to highlight the decrease in deaths using Seaborn lineplot()
sns.lineplot(...)
sns.lineplot(...)
plt.title(...)
plt.xlabel(...)
plt.ylabel(...)
plt.show()

# The graph shows that handwashing had a huge effect. How much did it reduce the monthly
# proportion of deaths on average? Calculate the decrease in the deaths of women in childbirth
# due to handwashing as a percentage, i.e., 100*(afterHW - beforeHW)/beforeHW
percentage_decrease = ...
print(...)

# So it would seem that Semmelweis had solid evidence that handwashing was a simple but highly effective
# procedure that could save many lives. The tragedy is that, despite the evidence, Semmelweis' theory —
# that childbed fever was caused by some "substance" (what we today know as bacteria) from autopsy room
# corpses — was ridiculed by contemporary scientists. The medical community largely rejected his discovery
# and in 1849 he was forced to leave the Vienna General Hospital for good.

# One reason for this was that statistics and statistical arguments were uncommon in medical science in
# the 1800s. Semmelweis only published his data as long tables of raw data, but he didn't show any graphs.
# Maybe if he had access to the analysis you've just put together he might have been more successful in
# getting the Viennese doctors to wash their hands.

