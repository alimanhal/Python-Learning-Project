import urllib.request as urlib

def main(url):
    print('Checkking connectivit...')
    try:
        response = urlib.urlopen(url)
        print("Connected to", url , "succesfully")
        print("This response code was : ", response.getcode())
    except:
         print(f"Failed to connect to {url}. Error: {e.reason}")

print('This is a site connectiviy checker program')
input_url = input('Input the url of the site you want to check: ').strip()

main(input_url)