import boto3, logging
import pandas as pd
logger = logging.getLogger()
logger.setLevel(logging.INFO)

from io import BytesIO 
from botocore.exceptions import ClientError


def save_json_to_s3(pDf:pd.DataFrame, pKey:str, pBucket:str) -> None:
  s3 = boto3.resource("s3").Bucket(pBucket)
  out_buffer = BytesIO()
  df_ = pDf.reset_index()
  df_.to_json(out_buffer, orient='records', compression='gzip')
  s3.Object(key=pKey).put(Body=out_buffer.getvalue())


def get_df_from_s3_parquets(prefix:str, pBucket:str) -> pd.DataFrame:
  bucket = pBucket
  result_df = pd.DataFrame()
  s3 = boto3.resource('s3').Bucket(bucket)

  for obj in s3.objects.filter(Prefix=prefix):
    try:
      body = obj.get()['Body'].read()
      temp = pd.read_parquet(BytesIO(body))
      result_df = pd.concat([result_df, temp])
    except:
      continue
  
  return result_df


def get_df_from_dynamodb(pTableNm:str, pColumns:list=None) -> pd.DataFrame:
  result = None

  try:
    dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2', endpoint_url='http://dynamodb.ap-northeast-2.amazonaws.com')
    table = dynamodb.Table(pTableNm)

    if isinstance(pColumns, list):
      select_cols = ''
      for col in pColumns:
        select_cols += col + ','
      select_cols = select_cols[:-1]
      response = table.scan(ProjectionExpression=select_cols)
    else:
      response = table.scan()

    result = pd.json_normalize(response['Items'])
  except (ClientError, Exception) as e:
    logger.exception(f'[get_data_from_dynamdb] pTableNm: {str(pTableNm)}')
    logger.exception(f'[get_data_from_dynamdb] error: {str(e)}')
  return result
