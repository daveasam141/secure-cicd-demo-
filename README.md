###  Secure CI/CD Demo 
1. Add vulnerable app 
vi app.py 
![alt text](<screenshots/Screenshot 2025-04-13 at 5.35.02 PM.png>)

2. Add a requirements.txtg 
vi requirements.txt
![alt text](<screenshots/Screenshot 2025-04-13 at 5.37.31 PM.png>)

## Step 2: Set up GitHub Actions pipeline 
1. create .github/workflows/devsecops.yml 
![alt text](<screenshots/Screenshot 2025-04-13 at 5.53.54 PM.png>)

2. Add a Dockerfile (for Trivy scanning)
vi dockerfile 
![alt text](<Screenshot 2025-04-13 at 5.58.54 PM.png>)
