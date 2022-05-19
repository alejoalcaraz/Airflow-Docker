from utils.file_util import cargar_datos

# city insertion
def insert_query_city(**kwargs):
    
    insert = f"INSERT INTO city (City_Key,City,State_Province,Country,Continent,Sales_Territory,Region,Subregion,Latest_Recorded_Population) VALUES "
    insertQuery = ""
    dataframe =cargar_datos(kwargs['csv_path'])
    for index, row in dataframe.iterrows():
        insertQuery += insert + f"({row.City_Key},\'{row.City}\',\'{row.State_Province}\',\'{row.Country}\',\'{row.Continent}\',\'{row.Sales_Territory}\',\'{row.Region}\',\'{row.Subregion}\',{row.Latest_Recorded_Population});\n"
    return insertQuery

# customer insertion
def insert_query_customer(**kwargs):
    insert = f"INSERT INTO customer (Bill_To_Customer,Buying_Group,Category,Customer,Customer_Key,Postal_Code,Primary_Contact) VALUES "
    insertQuery = ""
    dataframe =cargar_datos(kwargs['csv_path'])
    for index, row in dataframe.iterrows():
        insertQuery += insert + f"(\'{row.Bill_To_Customer}\',\'{row.Buying_Group}\',\'{row.Category}\',\'{row.Customer}\',{row.Customer_Key},{row.Postal_Code},\'{row.Primary_Contact}\');\n"
    return insertQuery

# date insertion
def insert_query_date(**kwargs):
    insert = f"INSERT INTO date_table (Calendar_Month_Number,Calendar_Year,Date_key,Day_Number,Day_val,Fiscal_Month_Number,Fiscal_Year,Month_val,Short_Month) VALUES "
    insertQuery = ""
    dataframe =cargar_datos(kwargs['csv_path'])
    for index, row in dataframe.iterrows():
        insertQuery += insert + f"({row.Calendar_Month_Number},{row.Calendar_Year},\'{row.Date_key}\',{row.Day_Number},{row.Day_val},{row.Fiscal_Month_Number},{row.Fiscal_Year},\'{row.Month_val}\',\'{row.Short_Month}\');\n"
    return insertQuery

# employee insertion
def insert_query_employee(**kwargs):
    insert = f"INSERT INTO employee (Employee,Employee_Key,Is_Salesperson,Preferred_Name) VALUES "
    insertQuery = ""
    dataframe =cargar_datos(kwargs['csv_path'])
    for index, row in dataframe.iterrows():
        insertQuery += insert + f"(\'{row.Employee}\',{row.Employee_Key},{row.Is_Salesperson},\'{row.Preferred_Name}\');\n"
    return insertQuery

# stock item insertion
def insert_query_stock(**kwargs):
    insert = f"INSERT INTO stockitem (Brand,Buying_Package,Color,Is_Chiller_Stock,Lead_Time_Days,Quantity_Per_Outer,Recommended_Retail_Price,Selling_Package,Size_val,Stock_Item,Stock_Item_Key,Tax_Rate,Unit_Price,Typical_Weight_Per_Unit) VALUES "
    insertQuery = ""
    dataframe =cargar_datos(kwargs['csv_path'])
    for index, row in dataframe.iterrows():
        insertQuery += insert + f"(\'{row.Brand}\',\'{row.Buying_Package}\',\'{row.Color}\',{row.Is_Chiller_Stock},{row.Lead_Time_Days},{row.Quantity_Per_Outer},{row.Recommended_Retail_Price},\'{row.Selling_Package}\',\'{row.Size_val}\',\'{row.Stock_Item}\',{row.Stock_Item_Key},{row.Tax_Rate},{row.Unit_Price},{row.Typical_Weight_Per_Unit});\n"
    return insertQuery
    
# fact order insert
def insert_query_fact_order(**kwargs):
    insert = f"INSERT INTO fact_order (city_key,customer_key,order_date_key,order_key,package,picked_date_key,picker_key,quantity,salesperson_key,stock_item_key,tax_amount,unit_price,tax_rate,total_excluding_tax,total_including_tax) VALUES "
    insertQuery = ""
    dataframe =cargar_datos(kwargs['csv_path'])
    for index, row in dataframe.iterrows():
        insertQuery += insert + f"({row.city_key},{row.customer_key},\'{row.order_date_key}\',{row.order_key},\'{row.package}\',\'{row.picked_date_key}\',{row.picker_key},{row.quantity},{row.salesperson_key},{row.stock_item_key},{row.tax_amount},{row.unit_price},{row.tax_rate},{row.total_excluding_tax},{row.total_including_tax});\n"
    return insertQuery
