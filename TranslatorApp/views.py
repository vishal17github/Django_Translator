import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import User
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import uuid
from django.http import JsonResponse


def index(request):
    context = {
        'variable_name': 'value',  # Pass any data you want to display in the template
    }
    return render(request, 'index.html', context)


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Hash the password
        hashed_password = make_password(password)

        # Create a dictionary with the form data
        user_data = {
            'name': name,
            'email': email,
            'password': hashed_password
        }

        # Store the data in a JSON file (for demonstration purposes)
        with open('user_data.json', 'a') as json_file:
            json.dump(user_data, json_file)
            json_file.write('\n')
            
        account_name = 'demoprojectazure'
        account_key = 'zCqa9umdyKIfOR0/o1tFdA0vR6RhnW1aU8ibPmjaUY6AIVoTLJLCV4Uu6wAqpseVI6y9YXF1Nfr2+AStj1D/1A=='
        container_name = 'azureuser'
        local_file_path = 'C:\\Users\\magic\\OneDrive\\Desktop\\Batch3\\Translator\\user_data.json'
        
        # Generate a unique blob name using uuid
        blob_name = 'blob_' + str(uuid.uuid4())

        blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

        # Get a container client
        container_client = blob_service_client.get_container_client(container_name)

        # Delete the existing blob if it exists
        try:
            blob_client = container_client.get_blob_client(blob_name)
            blob_client.delete_blob()
        except Exception as e:
            # Handle the exception if the blob does not exist
            pass

        # Upload a file to Azure Blob Storage
        with open(local_file_path, "rb") as data:
            blob_client = container_client.get_blob_client(blob_name)
            blob_client.upload_blob(data)

        return render(request, 'index.html')
    else:
        # Handle GET request if needed
        return render(request, 'signup.html')
