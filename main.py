import requestgs

def get_info_by_ip ( ip Any'):22
try:
    response = requests. get(url=F'http://ip.api.com/json/') 
    #print (response)
    data={
        '[IP]':response.get('query'),
    '[Int prov]':response.get('isp'),
     '[org]'  esponse.get('org'),
    '[coutry]'':response.get('coutry'),
                      
    }

except  requests.exceptions.ConnectionError:
   print('[!]Please check your coneection!')
    
    
    
def main():
    ip=input('Please enter a target IP:')
    get_info_by_ip(ip=ip)
    
    if _name_=='_main_':
        if __name__ == '__main__':
            main()
            
            
    