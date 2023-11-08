
# Language-Translator

## Overview

This project demonstrates the creation of a language translator web application using HTML, CSS, JavaScript, and Azure services. The application allows users to input text in one language and obtain a translation into another language. It leverages Azure services to perform the actual translation and incorporates additional services for enhanced functionality and security.

## Technologies Used

- **HTML:** For the structure of the web page.
- **CSS:** For styling and layout.
- **JavaScript:** For client-side logic and interactions.
- **Azure Services:** To provide translation capabilities.
- **Azure Virtual Network (VNet):** For secure network connectivity and isolation.
- **Azure Virtual Machine (VM):** To host the server-side code.
- **Domain Name System (DNS):** To associate a domain name with the VM's IP address custom DNS.
- **Azure Monitor:** For monitoring and analyzing application performance.
- **Azure Backup:** To safeguard data with automated backups.
- **Azure Site Recovery:** For disaster recovery and business continuity.

## Prerequisites

Before setting up the project, ensure you have the following:

- **An Azure account:** You'll need an Azure account to create and manage Azure services.
- **An Azure Virtual Machine:** Set up an Azure VM to host the server-side code for your application.
- **A registered domain:** Register a domain name (e.g., transapp.com) with a domain registrar and configure the DNS settings to point to your Azure VM's IP address.

## Setup Instructions

### Front-end (HTML, CSS, JavaScript)

1. Place your HTML, CSS, and JavaScript files in a directory on a web server or hosting service. You can use any web hosting service for this purpose.
2. Ensure you have a form for users to input text to be translated and a display area for the translated text.
3. In your JavaScript code, use the Azure Translator API to send translation requests to your Azure server.

### Back-end (Azure VM)

1. Set up an Azure Virtual Machine (VM) with your preferred operating system (e.g., Ubuntu, Windows).
2. Install a web server (e.g., IIS) and configure it to serve the back-end code.
3. Configure Azure Virtual Network (VNet) for secure communication between components.

### Azure Services Configuration

1. **Azure Monitor:**
   - Configure Azure Monitor to collect telemetry data from your application.
   - Set up alerts and notifications for monitoring critical metrics.

2. **Azure Backup:**
   - Configure automated backups for your application data to ensure data safety.
   - Implement a backup and recovery strategy for your database and application files.

3. **Azure Site Recovery:**
   - Set up Azure Site Recovery to create a disaster recovery plan for your application.
   - Test the recovery process to ensure business continuity in case of a failure.

## DNS Configuration

Configure your DNS settings for your registered domain name to point to the IP address of your Azure VM.

## Usage

1. Visit your website using your registered domain (e.g., transapp.com).
2. Enter text in the source language and select the target language.
3. Click the translate button to send the translation request to your Azure server.
4. Display the translation result on the web page.


## Demo Url : http://transapp.eastus.cloudapp.azure.com/
## Demo Video Url : https://www.youtube.com/watch?v=6blx23Uqdvk
## Demo Images :

![1](https://github.com/vishal17github/Django_Translator/assets/145033609/19b01437-3f6f-4236-b98f-f0dfc0dda8ec)
![2](https://github.com/vishal17github/Django_Translator/assets/145033609/f6979b2d-1897-49cc-bbae-87ce3b228c9e)
![3](https://github.com/vishal17github/Django_Translator/assets/145033609/13d3041b-6603-4072-b050-3c000ecf5c08)
![4](https://github.com/vishal17github/Django_Translator/assets/145033609/0f7b920d-98e5-433c-92ba-d44370242f7b)










