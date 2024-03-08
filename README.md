## Image Generation using Amazon Bedrock

## Project Overview:

This project demonstrates the Image generation using Amazon Bedrock using Stability AI foundation model.

## Prerequisites:

AWS Account 

## AWS Services:

1.  API Gateway

2. Lambda 

3. Amazon Bedrock

4. S3

## Project Architecture:

![image](https://github.com/veerababu558/AWS-Bedrock-Image/assets/44125493/52f8ab6a-b93c-4dc2-81e4-16bfe34af88f)

Steps:

1. Created an S3 bucket “s3-bedrock-bucket”  to store images. Below is the screen shot.
   
![Image Generation using Amazon Bedrock-Page-2 drawio](https://github.com/veerababu558/AWS-Bedrock-Image/assets/44125493/d07be35b-5809-418f-bbf2-ddbdce1d09d0)

2. Developed a Lambda function to receive prompts and utilize Amazon Bedrock for Image Generation, using the Stability.AI foundation model. The Lambda then saves the generated image to the S3 bucket and generates a pre-signed URL.

![Image Generation using Amazon Bedrock-Page-3 drawio](https://github.com/veerababu558/AWS-Bedrock-Image/assets/44125493/5647c2c6-d99f-4fd6-83f0-c6da854e9115)
![Image Generation using Amazon Bedrock-Page-4 drawio](https://github.com/veerababu558/AWS-Bedrock-Image/assets/44125493/e7623929-3865-4f1d-acb1-3a9f58d3f740)

3. Configured an API Gateway with URL query parameters and Mapping templates.
   
![Image Generation using Amazon Bedrock-Page-5 drawio](https://github.com/veerababu558/AWS-Bedrock-Image/assets/44125493/2acd5354-bb6b-431c-b207-46b585d8a22d)
![Image Generation using Amazon Bedrock-Page-6 drawio](https://github.com/veerababu558/AWS-Bedrock-Image/assets/44125493/45342754-c454-4c3d-8de5-99c5504ca502)
![Image Generation using Amazon Bedrock-Page-8 drawio](https://github.com/veerababu558/AWS-Bedrock-Image/assets/44125493/339b2c18-0b97-4244-94da-c7ccc9b2a299)
   
4. Using Postman, invoked the API with the prompt "Picture of Running Tiger," which returned the pre-signed URL of the image stored in the S3 bucket.

![Image Generation using Amazon Bedrock-Page-9 drawio](https://github.com/veerababu558/AWS-Bedrock-Image/assets/44125493/3669517d-328f-402b-8c02-6a464b3df7c1)

5. Finally, I downloaded the image using the pre-signed URL and viewed it using the Paint application

![Image Generation using Amazon Bedrock-Page-11 drawio](https://github.com/veerababu558/AWS-Bedrock-Image/assets/44125493/b1869d04-80ce-4997-b620-1de643d6951c)
![Image Generation using Amazon Bedrock-Page-12 drawio](https://github.com/veerababu558/AWS-Bedrock-Image/assets/44125493/17e155ee-851a-4195-a594-90200b05582f)


