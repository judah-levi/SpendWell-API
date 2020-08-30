# SpendWell-API

SpendWell was my team's submission to a local sustainability-oriented hackathon. I wrote the API, containerized with Docker, deployed on Heroku including the provisioning and connection of a Heroku-hosted postgres database. 


Deployed at:
https://spendwell-api.herokuapp.com/


<ins>**SpendWell**</ins>

**Product Summary:**

SpendWell gamifies and incentivizes the change of purchasing behavior from products that are environmentally taxing to those which are less so. 

**MVP Core functionality:**

User scans barcode of any product while grocery shopping
App loads a suggestion page that will present a product that is less environmentally taxing. It will perform this by a clustering algorithm to see which products are similar and then by a linear regression to compute the most environmental product possible. The user manually closes the suggestion page => app presents the main page. 
Each product is rated by weighted environment tax score: 
Packaging type
Carbon footprint (travel distance)
Product type (i.e. meat > veggies)
Checkout Button => user scans receipt
App parses the receipt and gives points based off the total summed environmental tax score of the receipt
App redirects to the “awards” page where the user sees how many points they earned for this purchase. 
Awarded points are accrued in the user account and represent discounts on further purchases

**Extended Functionality:**

Over time the app uses machine learning to classify the Consumer Habit Rigidity Index that predicts which factors are necessary to incentivize purchasing changes amongst various classes of consumers. Special attention will be placed on those consumers which are rated as being both rigid in their purchasing habits as well as often purchasing products that are environmentally taxing. 

**Business Case:**

SpendWell attempts to solve the issue of changing consumer behavior for the good of the planet. It aims to do so as close to the moment of purchase as possible and specifically in a market that is still heavily dependent upon brick and mortar shopping experiences. For the brands that benefit from the apps’ product suggestions, we anticipate that the opportunity for targeted, incentivized marketing will provide sufficient ROI to ensure that they will support loyalty-based  promotions rather than placing the cost of such incentives upon the retailer itself. 
