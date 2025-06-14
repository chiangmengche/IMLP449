import pandas as pd
from pycaret.regression import *

# Load資料
df = pd.read_csv("data/usedcar_data.csv")
features = ['years', 'km', 'rating', 'condition', 'economy', 'top speed', 'hp', 'torque', 'current price']
df = df[features].dropna()

# 設定 PyCaret 環境
reg_setup = setup(data=df, 
                  target='current price', 
                  session_id=42, 
                  normalize=True, 
                  polynomial_features=False,
                  silent=True, 
                  verbose=False)

# 顯示相關係數矩陣
print("\\n=== 特徵相關性矩陣 ===")
corr_matrix = df.corr(numeric_only=True)
print(corr_matrix['current price'].sort_values(ascending=False))

# 比較模型
best_models = compare_models(n_select=3, sort='R2')

# 選擇Linear Regression做分析
lr_model = create_model('lr')
print("\\n=== 線性回歸模型建立完成 ===")
print(lr_model)

# 輸出模型係
print("\\n=== 模型係數 ===")
coef_df = pd.DataFrame({'Feature': get_config('X_train').columns,
                        'Coefficient': lr_model.coef_})
print(coef_df)

# 預測與評估
predict_model(lr_model)

# 儲存模型
 save_model(lr_model, 'pycaret_lr_model')