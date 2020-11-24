from nsetools import Nse
import json
nse = Nse()
print(nse)

while True:
	main_input = int(input("\nWhat You Want To Do\n\nPress 1 to Get The List Of Todays Top Gainers\n\nPress 2 to Get The List Of Todays Top Losers\n\nPress 3 to Get index Quote\n\nPress 4 to Get the Information About The Company Stock by Providing the Symbol Of The Stock\n\nPress 5 To Get the List Of Symbols of Every Stock\n\nPress 6 To Get The List Of Advances Declines\n\nPress 7 to get the list of F&O Lot Sizes: "))
	
	index_quote_list = nse.get_index_list()
	top_gainers = nse.get_top_gainers()
	top_losers = nse.get_top_losers()
	all_stock_codes = nse.get_stock_codes()
	adv_dec = nse.get_advances_declines()
	lot_sizes = nse.get_fno_lot_sizes()

	if main_input == 1:
		print(json.dumps(top_gainers,sort_keys=True,indent=4))

	if main_input == 2:
		print(json.dumps(top_losers,sort_keys=True,indent=4))

	if main_input == 3:
		x = int(input("\nWhich Type Of Index Quote You Want To See\nPress 1 to get the List Of Index Quote\nPress 2 to Search The Index Quote: "))
		if x == 1:
			print(json.dumps(index_quote_list,sort_keys=True,indent=4))

		if x == 2:
			index_quote_search = nse.get_index_quote(input("Search A Index Quote: "))
			print(json.dumps(index_quote_search,sort_keys=True,indent=4))

	if main_input == 4:
		Quote = nse.get_quote(input("\nPlease Enter The Stock Symbol (For Example: Infosys Technologies = 'infy') To Get The Information About The Company Stock: ")) 
		print(json.dumps(Quote,sort_keys=True,indent=4))

	if main_input == 5:
		print(json.dumps(all_stock_codes,sort_keys=True,indent=4))

	if main_input == 6:
		print(json.dumps(adv_dec,sort_keys=True,indent=4))

	if main_input == 7:
		print(json.dumps(lot_sizes,sort_keys=True,indent=4))


	con = int(input("\nDo You Want to Continue\nPress 1 For Yes\nPress 2 For No: "))

	if con == 2:
		break






