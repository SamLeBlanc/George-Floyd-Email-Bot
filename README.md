# George Floyd Email Bot 🤖

### Context
On May 25th, 2020, [George Floyd was murdered](https://en.wikipedia.org/wiki/Murder_of_George_Floyd) by four members of the Minneapolis Police Department. Officer Derek Chauvin killed Floyd by kneeling on his neck for almost 9 minutes. In response, the general public participated in the [largest protests](https://en.wikipedia.org/wiki/2020%E2%80%932021_United_States_racial_unrest) in the history of the United States. Despite the COVID pandemic, people took to the streets to protest police brutality and systemic racism. 

In my hometown of Seattle, the mayor and city council found themselves under [tremendous pressure](https://www.forbes.com/sites/jackbrewster/2020/06/10/seattle-protesters-take-over-city-hall-demand-mayors-resignation/?sh=1c2b425b3caf) from both protestors and police unions. Caught in the middle, there began a mass email campaign to convince municipal leaders to act. Through my research, I learned that these leaders did not actually read any of those emails, which is not surprising considering they received thousands per day. Instead, leaders fed these messages through keyword searches to understand the general sentiment of a large mass of emails.

### Basics
Upon learning this, I created a Python-based email bot that messages the mayor and city council once every 8 mins and 46 seconds, the amount of time George Floyd spent with a knee on his neck. These emails reiterated the calls for police accountability, redistribution of funds to communities, and the resignation of the mayor, who ordered the police to use [illegal chemical weapons on protestors](https://www.forbes.com/sites/jemimamcevoy/2020/06/08/seattle-police-use-tear-gas-against-protestors-despite-city-ban/?sh=749f44e25b4b). 

The code for this email bot is very simple and just involves setting up SMTP SSL for server connection and MIME for email formatting. The bot is capable of sending multiple emails from different accounts simultaneously, with dynamic use of different email bodies and subject lines.

### Usage
To use the bot, clone the repository with `$ git clone https://github.com/SamLeBlanc/George-Floyd-Email-Bot`. Then, update `info.csv` with the required information, and finally run `main.py`.
