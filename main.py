# Convert timedelta64 column to Seconds in Pandas DataFrame

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'job': ['dev', 'web dev', 'accountant', 'dev'],
    'task_duration': [
        np.timedelta64(1, "D"),
        np.timedelta64(30, "m"),
        np.timedelta64(90, "s"),
        np.timedelta64(1, "h")
    ],
})

print(df)

print('-' * 50)

print(df['task_duration'].dt.total_seconds())

