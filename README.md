# Translator App
Translator App is a web application built using Django framework that allows users to translate text from one language to another. It utilizes Azure services including Azure Virtual Network, Azure Web App, Key Vault, and Blob Storage for various functionalities.

# Features
Translate text from one language to another.
User-friendly interface with Bootstrap and custom CSS styles.
Secure storage of sensitive information using Azure Key Vault.
Storage of translated text and other data in Azure Blob Storage.
Seamless integration with Azure services for a reliable and scalable experience.

# Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.x installed on your system.

Django framework installed. You can install it using pip:

** pip install django

Azure account with necessary resources provisioned (Virtual Network, Key Vault, Blob Storage, etc.).

# lone the repository:

** git clone <repository-url>

Install project dependencies:

** cd translatorApp

** pip install -r requirements.txt

Configure Azure services credentials and endpoints in the Django settings file (settings.py).
Run the Django development server:

** python manage.py runserver
Access the application at http://localhost:8000 in your web browser.


# Configuration
AZURE_STORAGE_CONNECTION_STRING: Connection string for Azure Blob Storage.
AZURE_KEY_VAULT_URL: URL of the Azure Key Vault.In Python Module


# Usage
Access the Translator App at the provided URL.
Enter the text you want to translate and select the source and target languages.
Click the "Translate" button to view the translated text.


# Configure Azure servies 

# Create Resource Group "TranslatorApp"

# 1.Sign in to Azure Portal:

Go to Azure Portal and sign in with your Azure account credentials.

# 2.Create a Resource Group:

Click on the "Create a resource" button (+).

Select "Resource group".

Subscription: Choose your Azure subscription.

Resource group: Enter the name "TranslatorApp".

Region: Choose the appropriate region.

Click on "Review + create" and then "Create" to create the resource group.


# Create Virtual Network (VNet) in "TranslatorApp"
In the Resource Group "TranslatorApp":

Click on the "Add" button.

Search for "Virtual Network" and select it from the results.

# 3. Configure Virtual Network:

Name: Enter a unique name for your VNet.

Address space: Enter the address space for your VNet in CIDR notation (e.g., 10.0.0.0/16).

Subnet: Add a subnet within your VNet if needed.

Configure other settings based on your requirements.

Click on "Review + create" and then "Create" to create the Virtual Network.

# 4.Create Web App and Integrate with VNet

In the Resource Group "TranslatorApp":

Click on the "Add" button.

Search for "Web App" and select it from the results.

# 5.Configure Web App:

App name: Enter a unique name for your Web App.

Publish: Choose your publishing method (code, container, etc.).

Operating System: Choose the appropriate OS.

Region: Choose the same region as your VNet for optimal performance.

Configure other settings based on your requirements.

Click on "Next: Networking".

# 6.Networking Settings:
Connect to virtual network: Select "Add VNet connection".

Choose a virtual network: Select the VNet you created earlier.

Configure other networking settings as needed.

Click on "Next: Monitoring" and complete the setup.

# 7.Access the Web App

Once the deployment is complete, you can access your Web App at the provided URL. Ensure that your Web App is integrated with the VNet for secure communication and optimal performance.



# demo Video  Url

# Demo Url project
