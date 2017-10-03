import scrapy

#First spider class
class firstSpider(scrapy.Spider):
    name = "FTO_spider"
    start_urls = ['https://www.state.gov/j/ct/rls/other/des/123085.htm']
    
    #Parse function for the spider class
    def parse(self, response):
        orgList = {}
        SET_SELECTOR = 'td'  #The organization names are in the <td> tags
        count = 1  #Counter token
        for org in response.css(SET_SELECTOR):
            key = 'Org ' + str(count)
                
            NAME_SELECTOR = 'p ::text' #The selector in which the text is pulled from <p>
            CATCH_SELECTOR = '::text' #This is the next selector if the cell entry is just in the <td>
            entry = {key : org.css(NAME_SELECTOR).extract_first(default='Not-found').strip()} #Do the initial pull of data
            
            if len(orgList) == 0: #the first item in the dictionary, this first if statement may not be necessary, need to revisit
                orgList.update(entry)
                count += 1

            elif 'Not-found' not in entry[key]: #If it pulled legit data, and not a blank, then add it to the dict
                orgList.update(entry)
                count += 1
            
            else: #Else use the second selector to pull the text name out of the <td> (stupid website isn't standard)
                orgList.update({key : org.css(CATCH_SELECTOR).extract_first(default='Not-found').strip()})
                count += 1

            #This is the last name on the current list, hardcoded in but need to figure out the best way to update this
            #incase another group is added
            if 'Hizbul Mujahideen' in orgList[key]:
                break
        
        return orgList

    #TODO:
    #1) Text processing on the list of orgs that are gotten when the webpage is crawled
    #2) Start to map out each organization and research crawling the TOR network
    #3) Setup the parser to handle user input as well as multiple webpages with links 
