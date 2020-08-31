import requests


on = 1

while on:
  print('Please write a URL or URLs you want to check. (seperated by comma)')
  urls = input().lower().split(',')

  for i in range(len(urls)):
    url = urls[i].strip()
    url = url.replace(' ', '')
    
    if not '.' in url:
      print('{} is a not valid URL.'.format(url))
      continue
    if not 'http' in url:
      url = 'http://' + url
    try:
      r = requests.get(url)
      if r.status_code == 200:
        print('{} is up!'.format(url))
      else:
        print('{} is down!'.format(url))
    except:
      print('{} is down!'.format(url))
      
  while 1:
    print('Do you want to restart? y/n ', end='')
    answer = input().lower()
    if answer == 'y':
      break
    elif answer == 'n':
      on = 0
      break
    else:
      print('{} is a not valid answer.'.format(answer))