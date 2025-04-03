# app.py
# # app.py
print("Hello, World!")
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import importlib

# def get_data():
#     # This function can be replaced with any data fetching logic you want to use in your app.
#     return {'Date': [datetime.now(), datetime.now() - timedelta(days=1)],
#             'Value': [10.0, 20.0]}

# st.title('My Streamlit App')

# # Create a sidebar
# st.sidebar.header('Sidebar Content')
# option = st.sidebar.selectbox('Select an option', ['Option 1', 'Option 2'])

# # Get the data from our function
# data = get_data()
# df = pd.DataFrame(data)

# # Display the dataframe in the main content area.
# if st.checkbox('Show DataFrame'):
#     if df.empty:
#         st.error("No data available")
#     else:
#         st.write(df)

# st.header('Plotting Data')
# chart_type = st.selectbox(
#     'Select a chart type',
#     ['Line Chart', 'Bar Chart'])

# if chart_type == 'Line Chart':
#     line_chart(df, 'Value')
# elif chart_type == 'Bar Chart':
#     bar_chart(df)

# def line_chart(data, x_label):
#     # Create line chart
#     fig = plt.Figure(figsize=(6, 4), dpi=100)
#     ax = fig.add_subplot(111)
#     ax.plot(data[x_label])
#     st.pyplot(fig)

# def bar_chart(data):
#     # Create bar chart
#     fig = plt.Figure(figsize=(6, 4), dpi=100)
#     ax = fig.add_subplot(111)
#     ax.bar(data['Date'], data['Value'])
#     st.pyplot(fig)
