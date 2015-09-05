This script will generate the complete code neccessary for creating a city page like found on the regions section.

## Preparing the Code
The code had a lot of things to fix

#### Purge RTF Punctuation and Escape Quotes
Typographer's quotes are teh suck. This query will find all those pesky buggers as well as all double quotes and replace them with an escaped double quote, thus preparing it to be a Python string.

* Search:`[“”’‘""]`
* Replace:`\\""`

#### Purge the Weird Invisible Character
I don't know what this is, but Python won't recognize it.

* Search:`\x{A0}`
* Replace:` `

#### Put Breaks Before Links
This was an aesthetic choice to have the person's name, a break, and then a link to their org.

* Search:`(<a hr)`
* Replace:`<br>\1`