# st='photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png,'
st= 'photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\ng.jpg, Warsaw, 2016-02-29 22:13:11'
def solution(st):
  sts=st.split("\n")
  cities=[s.split(",")[1] for s in sts]
  suff=[s.split(",")[0][-4:] for s in sts]

  cities_=cities[:]
  reform=[]
  ind=0
  for city in cities:
    num=str(cities.count(city)-cities_.count(city)+1)
    num=num.zfill(2)
    cities_.remove(city)
    # print(city+num+".jpg")
    reform.append(city+num+suff[ind])
    ind+=1

  return reform

#>solution(st)
# [' Warsaw01.jpg',
#  ' London01.png',
#  ' Warsaw02.png',
#  ' Paris01.jpg',
#  ' Paris02.jpg',
#  ' London02.jpg',
#  ' Paris03.png',
#  ' Warsaw03.jpg',
#  ' Warsaw04.png',
#  ' Warsaw05.jpg',
#  ' Warsaw06.jpg',
#  ' Warsaw07.jpg',
#  ' Warsaw08.png',
#  ' Warsaw09.png',
#  ' Warsaw10.jpg']