import xlsxwriter

# Data from the schedule table
data = [
    ['Mon Sep 9', '8:00am - 10:00am', 'Read Notes/Cases & T2 Ch0-1; Install/practice Power Query basics', 'MSBA602', '2hrs', 'Start with intro video (R1) for context.'],
    ['Mon Sep 9', '10:00am - 11:00am', 'Workout (modified from calendar slot)', 'N/A', '1hr', 'Keep green; energize for day.'],
    ['Mon Sep 9', '11:00am - 1:00pm', 'Read What is Audit Quality; Start AAC2 (intro activities)', 'MACC611', '2hrs', 'Tie to class today; take notes.'],
    ['Mon Sep 9', '1:00pm - 1:30pm', 'Lunch/break', 'N/A', '30min', 'Override yellow if needed.'],
    ['Mon Sep 9', '1:30pm - 3:30pm', 'Read Ch3 & 5; Review ERD concepts for Quiz #2 prep (Day 3 of 4)', 'MSBA606', '2hrs', '+1hr extra for quiz.'],
    ['Mon Sep 9', '3:35pm - 4:50pm', 'Class: Audit Analytics', 'MACC611', 'Class', 'Fixed.'],
    ['Mon Sep 9', '5:00pm - 6:00pm', 'Post-class review: Notes from Audit Analytics; Continue AAC2 if needed', 'MACC611', '1hr', 'Quick debrief.'],
    ['Mon Sep 9', '6:30pm - 9:00pm', 'Class: Intro to Business Analytics', 'MSBA602', 'Class', 'Fixed.'],
    ['Mon Sep 9', '9:00pm - 9:30pm', 'Post-class review: Notes from Intro BA', 'MSBA602', '30min', 'Wind down.'],
    ['Tue Sep 10', '8:00am - 10:00am', 'Practice Power Query intro & use cases (hands-on with sample data)', 'MSBA602', '2hrs', 'Build on Mon reading.'],
    ['Tue Sep 10', '10:00am - 11:00am', 'Workout (shifted slightly)', 'N/A', '1hr', 'Keep green.'],
    ['Tue Sep 10', '11:00am - 1:00pm', 'Read PQ Ch2-4 & PBI Ch3-4; Practice data acquisition/connect sources', 'MSBA626', '2hrs', 'Install Power BI if not done.'],
    ['Tue Sep 10', '1:00pm - 1:30pm', 'Lunch/break', 'N/A', '30min', '-'],
    ['Tue Sep 10', '1:30pm - 3:30pm', 'Assignment #3; Project Milestone #1 (start drafting)', 'MSBA606', '2hrs', 'Tie to readings.'],
    ['Tue Sep 10', '3:30pm - 5:00pm', 'Class: Data Management SQL', 'MSBA606', 'Class', 'Assumed time; fixed.'],
    ['Tue Sep 10', '5:00pm - 6:00pm', 'Post-class review: Notes from Data Mgmt; Quiz #2 prep (Day 4 of 4, +extra hr)', 'MSBA606', '1hr', 'Final quiz study.'],
    ['Tue Sep 10', '6:30pm - 9:00pm', 'Class: Descriptive Analytics', 'MSBA626', 'Class', 'Fixed.'],
    ['Tue Sep 10', '9:00pm - 9:30pm', 'Post-class review: Notes from Descriptive', 'MSBA626', '30min', '-'],
    ['Wed Sep 11', '6:30am - 3:00pm', 'Work', 'N/A', 'Work', 'Fixed blue.'],
    ['Wed Sep 11', '3:35pm - 4:50pm', 'Class: Audit Analytics', 'MACC611', 'Class', 'Fixed.'],
    ['Wed Sep 11', '5:00pm - 6:00pm', 'Workout (as per calendar preference)', 'N/A', '1hr', 'Keep green; post-class.'],
    ['Wed Sep 11', '6:00pm - 6:30pm', 'Drive home, shower, eat', 'N/A', '30min', 'As requested.'],
    ['Wed Sep 11', '6:30pm - 8:30pm', 'Continue/finish AAC2; Review Audit Quality reading', 'MACC611', '2hrs', 'Evening slot; lighter day.'],
    ['Wed Sep 11', '8:30pm - 9:30pm', 'Light review: Quiz #2 practice questions (if needed after Tue)', 'MSBA606', '1hr', 'Ensure ready for potential in-class quiz.'],
    ['Thu Sep 12', '8:00am - 6:00pm', 'Work', 'N/A', 'Work', 'Fixed blue.'],
    ['Thu Sep 12', '6:00pm - 6:30pm', 'Drive home, eat/break', 'N/A', '30min', 'Transition.'],
    ['Thu Sep 12', '6:30pm - 8:30pm', 'Continue data acquisition practice; Connect sources hands-on', 'MSBA626', '2hrs', 'Build on Tue.'],
    ['Thu Sep 12', '8:30pm - 9:30pm', 'Workout (shifted from calendar if needed)', 'N/A', '1hr', 'Keep green; end day active.'],
    ['Fri Sep 13', '8:00am - 6:00pm', 'Work', 'N/A', 'Work', 'Fixed blue.'],
    ['Fri Sep 13', '6:00pm - 6:30pm', 'Drive home, eat/break', 'N/A', '30min', '-'],
    ['Fri Sep 13', '6:30pm - 8:30pm', 'Finalize Assignment #3 & Project Milestone #1; Submit if due', 'MSBA606', '2hrs', 'Wrap up week.'],
    ['Fri Sep 13', '8:30pm - 9:30pm', 'Weekly review: Scan notes from all classes', 'All', '1hr', 'Prep for next week.'],
    ['Sat Sep 14', '9:00am - 11:00am', 'Quiz #2 (if not taken); Light review of Week 3 readings', 'MSBA606', '2hrs', 'Max Sat limit; Quiz prep started earlier (extra hrs on Mon/Tue). Workout if missed earlier.'],
    ['Sun Sep 15', '10:30am - 12:30pm', 'Catch-up: Any unfinished MSBA602 practice/use cases', 'MSBA602', '2hrs', 'Flexible start.'],
    ['Sun Sep 15', '12:30pm - 1:00pm', 'Lunch/break', 'N/A', '30min', '-'],
    ['Sun Sep 15', '1:00pm - 3:00pm', 'Catch-up: MSBA626 data connect practice', 'MSBA626', '2hrs', 'If needed.'],
    ['Sun Sep 15', '3:00pm - 4:00pm', 'Workout', 'N/A', '1hr', 'Keep green.'],
    ['Sun Sep 15', '4:00pm - 6:00pm', 'Preview Week 4: Read ahead for MSBA606 Ch3/5 if time', 'MSBA606', '2hrs', 'Proactive for A+.'],
    ['Sun Sep 15', '6:00pm - 9:30pm', 'Free/flex (rest or overflow)', 'N/A', '-', 'Buffer for any extras.'],
]

# Create the workbook
workbook = xlsxwriter.Workbook('Success plan.xlsx')
worksheet = workbook.add_worksheet('Week 3')

# Write headers
headers = ['Day', 'Time Slot', 'Task/Activity', 'Checkbox', 'Course', 'Duration', 'Notes']
for col, header in enumerate(headers):
    worksheet.write(0, col, header)

# Write data and add checkboxes for tasks (skip non-task rows like classes, work, breaks, workouts)
row = 1
for entry in data:
    # Write the data
    for col, value in enumerate(entry):
        worksheet.write(row, col, value)
    
    # Add checkbox in column D (index 3) if it's a task (not Class, Work, Lunch/break, Workout, Free/flex, Drive, Post-class)
    task = entry[2]  # Task/Activity column
    if not any(word in task.lower() for word in ['class', 'work', 'lunch', 'break', 'workout', 'drive', 'free', 'post-class']):
        worksheet.insert_checkbox(row, 3, {'checked': False, 'x_scale': 0.8, 'y_scale': 0.8})
    
    row += 1

# Adjust column widths for readability
worksheet.set_column(0, 0, 12)  # Day
worksheet.set_column(1, 1, 20)  # Time Slot
worksheet.set_column(2, 2, 50)  # Task/Activity
worksheet.set_column(3, 3, 10)  # Checkbox
worksheet.set_column(4, 4, 15)  # Course
worksheet.set_column(5, 5, 10)  # Duration
worksheet.set_column(6, 6, 40)  # Notes

# Close the workbook
workbook.close()

print('Excel file "Success plan.xlsx" created successfully with checkboxes for tasks.')