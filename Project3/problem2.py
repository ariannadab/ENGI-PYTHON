# Market class

class Market:

              

    def __init__(self,state,market_name,street_address,city,zip_code):

        self.state = state
        self.market_name = market_name
        self.street_address = street_address
        self.city = city
        self.zip_code = zip_code                        
                             

    def __str__(self):

        return(self.market_name+'\n'+self.street_address+'\n'+self.city+', '+self.state+' '+str(self.zip_code))

                             

# function to read markets from a file and create a dictionary, where keys are zip codes and values are list of markets                  

def read_markets(filename):

    market_dict = {}
    try:
        with open(filename) as fp:
            content = fp.readlines()
            for line in content:
                line_list = line.strip().split('#')
                zip_code = (line_list[4])
                if zip_code in market_dict.keys():
                    market_dict[zip_code].append(Market(line_list[0],line_list[1],line_list[2],line_list[3],zip_code))
                else:
                    market_dict[zip_code] = [Market(line_list[0],line_list[1],line_list[2],line_list[3],zip_code)]
            fp.close()
    except IOError:
        print(filename+" doesn't exist")
    return market_dict          
                             

# main function to create a market dictionary and then search for markets given the zip code

def main():

    market_dict = read_markets('markets.txt')
    zip_code = (input('Enter the zip code : '))
    if zip_code in market_dict.keys():
        market_list = market_dict[zip_code]
        for market in market_list:
            print(market)
    else:
        print('No farmers markets in your zip code.')

# call the main function                

main()                  

#end of program