import pandas as pd
import json
def lambda_handler(event, context):

    d= {'col1':[1,2,3], 'col2':[4,5,6], 'col3':[7,8,9]}
    df = pd.DataFrame(d)
    print(df)
    print('Done')
