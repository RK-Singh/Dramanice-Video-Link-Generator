# web scraping with python
# get video download link from dramanice.to
# supports only html5 video player
from bs4 import BeautifulSoup
import urllib.request

def open_url(url):
	req = urllib.request.Request(
    	url, 
    	data=None, 
    	headers={
        	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    	})
	return BeautifulSoup(urllib.request.urlopen(req),"html.parser")

def get_video_url(url):
    soup = open_url(url)
    retvalue = []
    for video in soup.find_all('video'):
        for source in video.find_all('source'):
            retvalue.append([source['src'],source['data-res'],source['type']])
    return retvalue

def main():
    episodes = []
    # enter the details page of the drama
    # eg. url = 'http://dramanice.to/drama/kill-me-heal-me-detail'
    print("\n    Damanice.to Video Download Generator\n")
    print("Enter URL containing drama details")
    print("eg. url = 'http://dramanice.to/drama/kill-me-heal-me-detail'")
    url = input();
    try:
    	soup = open_url(url)
    except:
    	print("Error opening url. Abort.")
    	return
    # printing the name of the drama
    print(soup.find('h1',{'class':'title'}).string)
    for div in soup.find_all('div',{'class':'item-episode'}):
        episodes.append(div.find('a')['href'])
    # now episodes contains links to each episode
    print('total ', len(episodes), 'episodes')
    i = 1
    for episode in reversed(episodes):
        link = get_video_url(episode)
        print('episode:',i)
        if link == []:
        	print("html5 video player not found! Skipping")
        else:
        	print(link[0][0])
        i+=1

if __name__ == '__main__':
    main()
