# GET AIRFOIL .DAT FILES FROM UIUC AIRFOIL SITE
# Python Installation Requirements:
# beautfilsoup4
# lxml

# Importing
from bs4 import BeautifulSoup																	# Import the BeautifulSoup library
import re	
import pdb																					# Import regular expressions

try:																							# Import urllib
    import urllib.request as urllib2
except ImportError:
    import urllib2

# Base filepath for the UIUC airfoil website (used for accessing .dat files)
# http://airfoiltools.com/polar/details?polar=xf-a18-il-1000000
baseFlpth = "http://airfoiltools.com"
indexpth = baseFlpth + "/search/airfoils"

polarpath = baseFlpth + "/polar/details?polar=xf-" 
Re = "1000000" # Reynolds number
suffix = "-" + Re

basedir =  'airfoils_csv/'


# Open the webpage and create the soup
html_page = urllib2.urlopen(indexpth)			# Open the URL		
soup      = BeautifulSoup(html_page,'lxml')		# Create the soup

# Loop over all relevant files and save each one
ind   = 1																						# Iteration counter

    
links = soup.select("a[href*=airfoil\/details]")

print('Airfoils found: '+str(len(links)))
for link in links : 
      
    airfoilname =  re.findall('(?<=airfoil=).*' , link.get('href') )[0]
    
    html_page  = urllib2.urlopen(polarpath + airfoilname + suffix )			# Open the URL	
    soup2      = BeautifulSoup( html_page , 'lxml')
    csvlink    = soup2.select("a[href*=polar\/csv]")[0]
    #urllib2.urlretrieve(baseFlpth + csvlink.get('href'), csvlink.get('href').rsplit('/',1)[-1] )
    urllib2.urlretrieve( baseFlpth + csvlink.get('href'), basedir+airfoilname+suffix+'.csv' )
    ind = ind + 1	
    print('Downloaded: '+ basedir+airfoilname+suffix+'.csv')
    
pdb.set_trace()