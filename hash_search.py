from attr import has
from defines import getCreds, makeApiCall
import sys
import pandas as pd
import os as o
import webbrowser


def getHashtagInfo( params ) :
	

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['user_id'] = params['instagram_account_id'] # user id making request
	endpointParams['q'] = params['hashtag_name'] # hashtag name
	endpointParams['fields'] = 'id,name' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + 'ig_hashtag_search' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

def getHashtagMedia( params ) :
	

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['user_id'] = params['instagram_account_id'] # user id making request
	endpointParams['fields'] = 'id,children,caption,comment_count,like_count,media_type,media_url,permalink' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + params['hashtag_id'] + '/' + params['type'] # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call





hashtag = input() # hashtag to get info on

params = getCreds() # params for api call
params['hashtag_name'] = hashtag # add on the hashtag we want to search for
hashtagInfoResponse = getHashtagInfo( params ) # hit the api for some data!
params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id']; # store hashtag id


params['type'] = 'top_media' # set call to get top media for hashtag
hashtagTopMediaResponse = getHashtagMedia( params ) # hit the api for some data!

 #subcategories in which the trands are divided
columns = ['category','sub-category','vertical','trending attribute value','link']
data = []

#trending topic conditions
if 'croptop' in hashtag:
    c=0
    for post in hashtagTopMediaResponse['json_data']['data']:
        if(c<6):
         data.append(["fashion","western","women dresses",hashtag,post['permalink']])
         c+=1

elif 'slingbag' in hashtag:
    c=0
    for post in hashtagTopMediaResponse['json_data']['data']:
        if(c<6):
          data.append(["fashion","western","women accessories",hashtag,post['permalink']])
          c+=1 
         
elif 'floralprint' in hashtag:
    c=0
    for post in hashtagTopMediaResponse['json_data']['data']:
        if(c<6):
         data.append(["fashion","western","women dresses",hashtag,post['permalink']])
         c+=1 
        
         
elif 'sharara' in hashtag:
    c=0
    for post in hashtagTopMediaResponse['json_data']['data']:
        if(c<6):
         data.append(["fashion","ethnic","women dresses",hashtag,post['permalink']])
         c+=1 
         
elif 'puffsleaves' in hashtag:
    c=0
    for post in hashtagTopMediaResponse['json_data']['data']:
        if(c<6):
         data.append(["fashion","western","women dresses",hashtag,post['permalink']])
        c+=1 
         
    
         
elif 'bellbottoms' in hashtag:
    c=0
    for post in hashtagTopMediaResponse['json_data']['data']:
        if(c<6):
         data.append(["fashion","western","women dresses",hashtag,post['permalink']])
         c+=1 
         
elif 'graphictees' in hashtag:
    c=0
    for post in hashtagTopMediaResponse['json_data']['data']:
        if(c<6):
         data.append(["fashion","western","women dresses",hashtag,post['permalink']])
         c+=1 
         
elif 'animalprint' in hashtag:
    c=0
    for post in hashtagTopMediaResponse['json_data']['data']:
        if(c<6):
         data.append(["fashion","western","women dresses",hashtag,post['permalink']])
         c+=1 
         
elif 'offshoulder' in hashtag:
    c=0
    for post in hashtagTopMediaResponse['json_data']['data']:
        if(c<6):
         data.append(["fashion","western","women dresses",hashtag,post['permalink']])
        
         c+=1 
         

elif 'chikankari' in hashtag:
    c=0
    for post in hashtagTopMediaResponse['json_data']['data']:
        if(c<6):
         data.append(["fashion","ethnic","women dresses",hashtag,post['permalink']])
         c+=1 
         
elif 'lehengacholi' in hashtag:
    c=0
    for post in hashtagTopMediaResponse['json_data']['data']:
        if(c<6):
          data.append(["fashion","ethnic","women dresses",hashtag,post['permalink']])
          c+=1 

#if wrong keyword entered    
else:   
     c=0
     for post in hashtagTopMediaResponse['json_data']['data']:
         if(c<6):
          data.append([post['permalink'],hashtag,"Not found","Not found","Not found"])
          c+=1
 
 



#saving data in dataframes
df = pd.DataFrame(data, columns=columns)




# Function to convert file path into clickable form.
def fun(path):
    
    # returns the final component of a url
    f_url = o.path.basename(path)
      
    # convert the url into link
    return '<a href="{}" target="_blank">click the link for the post</a>'.format(path, f_url)
   
df = df.style.format({'link' : fun})










html = df.to_html()
  
# write html to file
text_file = open("table.html", "w")
text_file.write(html)
text_file.close()


webbrowser.open('table.html')






