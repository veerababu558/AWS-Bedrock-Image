import json
import boto3
import base64
import datetime

def lambda_handler(event, context):
    print("Boto 3 version:", boto3.__version__)
    
    bedrock_client = boto3.client('bedrock-runtime');
    s3_client      = boto3.client('s3');
    
    input_prompt = event["prompt"];

    bedrock_response =  bedrock_client.invoke_model(body=json.dumps({"text_prompts":
        [{"text": input_prompt}],"cfg_scale": 10, "steps": 30,
        "seed": 0
    }),
    contentType='application/json',
    accept='application/json',
    modelId='stability.stable-diffusion-xl-v0'
    );

    print('Bedrock response', bedrock_response)
    
    bedrock_byte_response = json.loads(bedrock_response['body'].read());
      
    print('bedrock_byte_response', bedrock_byte_response)
    
    bedrock_image_base64 = bedrock_byte_response['artifacts'][0]['base64'];
    bedrock_image_final  = base64.b64decode(bedrock_image_base64)
    
    imagename = 'image' + datetime.datetime.today().strftime('%Y-%M-%D-%M-%S')
    
    s3_client.put_object(Bucket='s3-bedrock-bucket',Body=bedrock_image_final, 
    Key=imagename)
    print('bedrock_image_final', bedrock_image_final)

    s3_pre_signed_url = s3_client.generate_presigned_url('get_object',
        Params={'Bucket':'s3-bedrock-bucket','Key':imagename}, ExpiresIn=3600)
    print('s3_pre_signed_url', s3_pre_signed_url)

    # TODO implement
    return {
        'statusCode': 200,
        'body': s3_pre_signed_url
    }
