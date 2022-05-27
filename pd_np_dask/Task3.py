import pandas as pd
import numpy as np
from icecream import ic

df1 = pd.DataFrame(
    index=["Moscow", "Tula", "Yaroslavl", "Tver"],
    data={
        "report": np.random.randint(1, 11, 4),
        "sample": np.random.randint(100, 1001, 4),
    },
)
df2 = pd.DataFrame(
    index=["Moscow", "Tula", "Volgograd", "Novgorod"],
    data={
        "report": np.random.randint(1, 11, 4),
        "sample": np.random.randint(100, 1001, 4),
    },
)

ic(df1, df2, df1.add(df2, fill_value=0))

# ic| df1:            report  sample
#          Moscow          7     943
#          Tula            4     225
#          Yaroslavl       1     454
#          Tver            3     827
#     df2:            report  sample
#          Moscow          6     828
#          Tula            6     524
#          Volgograd      10     193
#          Novgorod        3     175
#     df1.add(df2, fill_value=0):            report  sample
#                                 Moscow       13.0  1771.0
#                                 Novgorod      3.0   175.0
#                                 Tula         10.0   749.0
#                                 Tver          3.0   827.0
#                                 Volgograd    10.0   193.0
#                                 Yaroslavl     1.0   454.0
