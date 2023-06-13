# selenium-youtube-scraper-live
Scrape Top Trending videos on YouTube using Selenium and AWS Lambda 

# Objectives

1.  Scrape top 10 Trending Videos on YouTube using Selenium.
2.  Setup a recurring job on AWS Lambda to scrape every 30 min.
3.  Send the results as a CSV attachment over a mail.

**Topics Covered in this web-scrapping projects are:**
1. GitHub 
2. Replit platform 
3. Selenium
4. AWS Lmabda
5. SMTP for email 

**Steps executed in detail to achive the objective.**

**Step-1: Create a GitHub Repo**

**Step-2: Launch repo on Replit**

  - a. Create & Excecute Python script 
  
  - b. Attempt to scrape the page using requests and Beautiful Suoup
  
**Step-3: Selenium**

 - a. Install Selenium and create a browser driver
  
 - b. Load the page and extract information.
  
 - c. Create CSV file of results using Pandas
  
**Step-4 Setup rexurring Job on AWS Lambda**

- a. Create AWS Lambda Python function
  
- b. Deploy the sample script and observe the output
  
- c. Add layers for selenium and chromium
  
- d. Setup recurring job using AWS cloudwatch
  
**Step-5 Send result over email using SMTP**
-  a. Create email client using SMTP lib
  
-  b. Setup SSL, TLS and authenticate using password
  
-  c. Send sample email with just text
  
- d. Send an email with text and attachment.
  
  
Special Thanks to jovian.ai and Akash N S for guiding through this workshop.

