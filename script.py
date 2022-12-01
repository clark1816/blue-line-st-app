import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st


#start connecting to google scheet 
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("pythonsheet-355816-fd29616eb852.json", scope)

client = gspread.authorize(creds)

inv_tracker = client.open("blue-line-armory").sheet1

order_tracker = client.open("blue-line-armory").worksheet('Sheet2')

inv_data = inv_tracker.get_all_records()

order_data = order_tracker.get_all_records()

row = inv_tracker.get_values(0)

#create streamlit page with a sidebar
st.sidebar.header("Blue-Line-Armory")
option = st.sidebar.selectbox("", ('Inventory Editor','Order Tracker'),0)

if option == "Inventory Editor":
    st.header('Enter Inventory Information')
    #get appropiate inputs from the user
    item_number = st.number_input(label='Item Number', min_value=0)
    item_description = st.text_input(label='Description')
    item_quantity = st.number_input(label='Quantity')
    item_location = st.text_input(label='Location')
    item_cost = st.number_input(label='Product Cost')
    item_price = st.number_input(label='Product Price')
    
    #display all the data for the user to see changes real time
    st.dataframe(inv_data)
    if item_price:
        insertRow = [item_number,item_description, item_quantity, item_location, item_cost, item_price]
        inv_tracker.insert_row(insertRow, 2)
        
if option == "Order Tracker":
    st.header('Enter Order Information')
    #get appropiate inputs from the user
    item_number = st.number_input(label='order number', min_value=0,step=1)
    customer_name = st.text_input(label='Description')
    customer_address = st.text_input(label='Customers Address')
    tracking_number = st.text_input(label='Enter the Tracking Number')
    package_description = st.text_input(label='Package Description')
    est_arrival = st.text_input(label='Est Arrival')
    
    st.dataframe(order_data)
    if est_arrival:
        insertRow = [item_number, customer_name, customer_address, tracking_number, package_description, est_arrival
                     ]
        order_tracker.insert_row(insertRow, 2)
