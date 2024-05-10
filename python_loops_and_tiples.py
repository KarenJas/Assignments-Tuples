#3. Python Loops and Tuples in Analytical Applications

#Function to calculate average closing price
def average_closing_price(stock_data, symbol, start_date, end_date):
    #Initialize variables
    total_closing_price = 0
    #Represents the number of days 
    #closing prices were recorded
    count = 0 
    #Itterate through stock data
    for data_point in stock_data:
        #Extract data
        stock_symbol, date, closing_price = data_point
        if stock_symbol == symbol and start_date <= date <= end_date:
            #Calculate total closing price
            total_closing_price += closing_price
            count += 1
    #Return none if no data found for the specified stock and period 
    if count == 0:
        return None  
    #Return the average closing price    
    return total_closing_price / count

#Test
#stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
#]
#print(average_closing_price(stock_data, "AAPL", "2021-01-01", "2021-01-02"))
