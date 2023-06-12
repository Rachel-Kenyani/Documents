import datetime

# Get current date
current_date = datetime.datetime.now()
# datetime is a python module that workss with dates and times
# datetime.datetime.now() creates a new datetime object that contains the current date and time
# at the moment when the code is executed. 

# Add 2 days
shelf_life = datetime.timedelta(days=2)
expiration_date = current_date + shelf_life

# Format expiration date by using strftime
formatted_date = expiration_date.strftime("%A, %B %d, %Y")

# Display expiration date
print(f"The watermelon will expire on {formatted_date}")